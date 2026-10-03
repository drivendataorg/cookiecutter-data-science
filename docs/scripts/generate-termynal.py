import json
import os
import re
import subprocess
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

from ansi2html import Ansi2HTMLConverter

CCDS_ROOT = Path(__file__).parents[2].resolve()


def execute_command_and_get_output(command, input_script, cwd, timeout=60):
    """Run the scripted CLI dialogue without requiring a pseudo-terminal.

    Rich's prompts accept piped stdin on Windows, macOS and Linux. Pipes do not
    echo input, so restore each answer after its prompt for the animation.
    """
    input_script = list(input_script)
    result = subprocess.run(
        command,
        input="".join(answer + "\n" for _, answer in input_script),
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        cwd=cwd,
        env={**os.environ, "PYTHONIOENCODING": "utf-8", "NO_COLOR": "1"},
        encoding="utf-8",
        timeout=timeout,
        check=False,
    )
    if result.returncode:
        raise RuntimeError(
            f"CCDS exited with status {result.returncode}:\n{result.stdout}"
        )

    transcript = []
    remaining = result.stdout
    for prompt, answer in input_script:
        match = re.search(re.escape(prompt) + r"[^\r\n]*?: ", remaining)
        if match is None:
            raise RuntimeError(
                f"Expected CCDS prompt {prompt!r} not found:\n{remaining}"
            )
        transcript.append(remaining[: match.end()] + answer + "\n")
        remaining = remaining[match.end() :]
    transcript.append(remaining)
    return [f"$ ccds {CCDS_ROOT}"] + [
        line.strip() for line in "".join(transcript).splitlines()
    ]


ccds_script = [
    ("project_name", "My Analysis"),
    ("repo_name", "my_analysis"),
    ("module_name", ""),
    ("author_name", "Dat A. Scientist"),
    ("description", "This is my analysis of the data."),
    ("python_version_number", "3.12"),
    ("Choose from", "3"),  # dataset_storage
    ("bucket", "s3://my-aws-bucket"),
    ("aws_profile", ""),
    ("Choose from", "2"),  # environment_manager
    ("Choose from", "1"),  # dependency_file
    ("Choose from", "2"),  # pydata_packages
    ("Choose from", "3"),  # testing_framework
    ("Choose from", "1"),  # linting_and_formatting
    ("Choose from", "2"),  # open_source_license
    ("Choose from", "1"),  # docs
    ("Choose from", "2"),  # include_code_scaffold
]


def run_scripts():
    # Never generate into (or delete a project from) the developer's directory.
    with TemporaryDirectory(prefix="ccds-docs-") as directory:
        return execute_command_and_get_output(
            [sys.executable, "-u", "-m", "ccds", str(CCDS_ROOT)],
            ccds_script,
            directory,
        )


def render_termynal():
    # actually execute the scripts and capture the output
    results = run_scripts()

    # watch for inputs and format them differently
    script = iter(ccds_script)
    expected_prompt, user_input = next(script)

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
        elif expected_prompt is not None and re.fullmatch(
            r".*" + re.escape(expected_prompt) + r".*?:\s*" + re.escape(user_input),
            result,
        ):
            # treat all the options that were output as a single block
            if result_collector:
                prev_results = conv.convert("\n".join(result_collector), full=False)
                html_lines.append(f"<span data-ty>{prev_results}</span>")

            # split the line up into the prompt text with options, the default, and the user input
            # Remove the known answer rather than splitting on colons, which
            # can occur in defaults and answers (e.g. s3://my-aws-bucket).
            prompt = result[: -len(user_input)] if user_input else result
            prompt = conv.convert(prompt.rstrip(), full=False)
            prompt = f'<span data-ty class="inline-input">{prompt}</span>'
            user_input = conv.convert(user_input, full=False)

            # treat the cookiecutter prompt as a shell prompt
            out_line = f"{prompt}"
            out_line += f'<span class="inline-input" data-ty="input" data-ty-delay="500" data-ty-prompt="">{user_input}</span>'
            html_lines.append(out_line)
            html_lines.append('<span data-ty class="newline"></span>')
            result_collector = []

            try:
                expected_prompt, user_input = next(script)
            except StopIteration:
                expected_prompt = None

        # collect all the other lines for a single output
        else:
            result_collector.append(result)

    if expected_prompt is not None:
        raise RuntimeError(f"Expected input for {expected_prompt!r} was not rendered.")

    if result_collector:
        remaining = conv.convert("\n".join(result_collector), full=False)
        html_lines.append(f"<span data-ty>{remaining}</span>")
    html_lines.append("</div>")
    output = "\n".join(html_lines)

    # Ensure that all options are contained in the output
    options = json.load((CCDS_ROOT / "ccds.json").open("r")).keys()
    for option in options:
        assert option in output, f'Option "{option}" not found in termynal output.'

    # replace local directory in ccds call with URL so it can be used for documentation
    output = output.replace(
        str(CCDS_ROOT), "https://github.com/drivendataorg/cookiecutter-data-science"
    )
    return output


# script entry point for debugging
if __name__ == "__main__":
    print(render_termynal())

# mkdocs-gen-files executes scripts with runpy.run_path. Normal imports should
# not launch a build, so that the capture and rendering functions can be tested.
elif __name__ == "<run_path>":
    import mkdocs_gen_files

    with mkdocs_gen_files.open("index.md", "r") as f:
        index = f.read()

    index = index.replace("<!-- TERMYNAL OUTPUT -->", render_termynal())

    with mkdocs_gen_files.open("index.md", "w") as f:
        f.write(index)
