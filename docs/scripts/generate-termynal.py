import shutil
from pathlib import Path

import pexpect
from ansi2html import Ansi2HTMLConverter

CCDS_ROOT = Path(__file__).parents[2].resolve()


def execute_command_and_get_output(command, input_script):
    input_script = iter(input_script)
    child = pexpect.spawn(command, encoding="utf-8")

    interaction_history = [f"$ {command}\n"]

    prompt, user_input = next(input_script)

    try:
        while True:
            index = child.expect([prompt, pexpect.EOF, pexpect.TIMEOUT])

            if index == 0:
                output = child.before + child.after
                interaction_history += [line.strip() for line in output.splitlines()]

                child.sendline(user_input)

                try:
                    prompt, user_input = next(input_script)
                except StopIteration:
                    pass

            elif index == 1:  # The subprocess has exited.
                output = child.before
                interaction_history += [line.strip() for line in output.splitlines()]
                break
            elif index == 2:  # Timeout waiting for new data.
                print("\nTimeout waiting for subprocess response.")
                continue

    finally:
        return interaction_history


ccds_script = [
    ("project_name", "My Analysis"),
    ("repo_name", "my_analysis"),
    ("module_name", ""),
    ("author_name", "Dat A. Scientist"),
    ("description", "This is my analysis of the data."),
    ("python_version_number", "3.12"),
    ("Choose from", "3"),
    ("bucket", "s3://my-aws-bucket"),
    ("aws_profile", ""),
    ("Choose from", "2"),
    ("Choose from", "1"),
    ("Choose from", "2"),
    ("Choose from", "2"),
    ("Choose from", "1"),
]


def run_scripts():
    try:
        output = []
        output += execute_command_and_get_output(f"ccds {CCDS_ROOT}", ccds_script)
        return output

    finally:
        # always cleanup
        if Path("my_analysis").exists():
            shutil.rmtree("my_analysis")


def render_termynal():
    # actually execute the scripts and capture the output
    results = run_scripts()

    # watch for inputs and format them differently
    script = iter(ccds_script)
    _, user_input = next(script)

    conv = Ansi2HTMLConverter(inline=True)
    html_lines = [
        '<div id="termynal" data-termynal class="termy" data-ty-macos data-ty-lineDelay="100" data-ty-typeDelay="50" title="Cookiecutter Data Science">'
    ]
    result_collector = []

    for line_ix, result in enumerate(results):
        # style bash user inputs
        if result.startswith("$"):
            result = conv.convert(result.strip("$"), full=False)
            html_lines.append(
                f'<span data-ty="input" data-ty-prompt="$">{result}</span>'
            )

        # style inline cookiecutter user inputs
        elif ":" in result and user_input in result:
            # treat all the options that were output as a single block
            if len(result_collector) > 1:
                prev_results = conv.convert(
                    "\n".join(result_collector[:-1]), full=False
                )
                html_lines.append(f"<span data-ty>{prev_results}</span>")

            # split the line up into the prompt text with options, the default, and the user input
            prompt, user_input = result.strip().split(":", 1)
            prompt = conv.convert(prompt, full=False)
            prompt = f'<span data-ty class="inline-input">{result_collector[-1].strip()} {prompt}:</span>'
            user_input = conv.convert(user_input.strip(), full=False)

            # treat the cookiecutter prompt as a shell prompt
            out_line = f"{prompt}"
            out_line += f'<span class="inline-input" data-ty="input" data-ty-delay="500" data-ty-prompt="">{user_input}</span>'
            html_lines.append(out_line)
            html_lines.append('<span data-ty class="newline"></span>')
            result_collector = []

            try:
                _, user_input = next(script)
            except StopIteration:
                user_input = "STOP ITER"  # never true so we just capture the remaining rows after the script

        # collect all the other lines for a single output
        else:
            result_collector.append(result)

    html_lines.append("</div>")
    output = "\n".join(html_lines)

    # replace local directory in ccds call with URL so it can be used for documentation
    output = output.replace(
        str(CCDS_ROOT), "https://github.com/drivendataorg/cookiecutter-data-science"
    )
    return output


# script entry point for debugging
if __name__ == "__main__":
    print(render_termynal())

# mkdocs build entry point
else:
    import mkdocs_gen_files

    with mkdocs_gen_files.open("index.md", "r") as f:
        index = f.read()

    index = index.replace("<!-- TERMYNAL OUTPUT -->", render_termynal())

    with mkdocs_gen_files.open("index.md", "w") as f:
        f.write(index)
