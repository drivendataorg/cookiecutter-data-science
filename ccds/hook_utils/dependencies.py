packages = [
    "black",
    "flake8",
    "isort",
    "pip",
    "python-dotenv",
]

basic = [
    "ipython",
    "jupyterlab",
    "matplotlib",
    "notebook",
    "numpy",
    "pandas",
    "scikit-learn",
]

scaffold = [
    "typer",
    "loguru",
    "tqdm",
]


def write_dependencies(
    dependencies, packages, pip_only_packages, repo_name, module_name, python_version
):
    if dependencies == "requirements.txt" or dependencies == "requirements.in":
        with open(dependencies, "w") as f:
            lines = sorted(packages)

            # Only add -e . to requirements.txt, not requirements.in
            if dependencies == "requirements.txt":
                lines += ["", "-e ."]

            f.write("\n".join(lines))
            f.write("\n")

    elif dependencies == "environment.yml":
        with open(dependencies, "w") as f:
            lines = [
                f"name: {repo_name}",
                "channels:",
                "  - conda-forge",
                "dependencies:",
            ]

            lines += [f"  - python={python_version}"]
            lines += [f"  - {p}" for p in packages if p not in pip_only_packages]

            lines += ["  - pip:"]
            lines += [f"    - {p}" for p in packages if p in pip_only_packages]
            lines += ["    - -e ."]

            f.write("\n".join(lines))

    elif dependencies == "Pipfile":
        with open(dependencies, "w") as f:
            lines = ["[packages]"]
            lines += [f'{p} = "*"' for p in sorted(packages)]

            lines += [f'"{module_name}" ={{editable = true, path = "."}}']

            lines += ["", "[requires]", f'python_version = "{python_version}"']

            f.write("\n".join(lines))
