import tomlkit

packages = [
    "pip",
    "python-dotenv",
]

flake8_black_isort = [
    "black",
    "flake8",
    "isort",
]

ruff = ["ruff"]

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


def resolve_compatible_python_version(python_version):
    """Resolves a Python version string to one that behaves as expected with the "compatible release"
    operator.

    Examples:
    - 3.13 should result in ~=3.13.0 which installs the latest version of Python that is compatible
      with 3.13, so the highest patch number for 3.13 (3.13.3 at the time of writing)
    - 3.13.2 should result in ~=3.13.2 which ensures Python 3.13.2 is used

    See https://packaging.python.org/en/latest/specifications/version-specifiers/#compatible-release
    """
    version_parts = python_version.split(".")
    if len(version_parts) == 2:
        major, minor = version_parts
        patch = "0"
    elif len(version_parts) == 3:
        major, minor, patch = version_parts
    else:
        raise ValueError(
            f"Invalid Python version specifier {python_version}. "
            "Please specify version as <major>.<minor> or <major>.<minor>.<patch>, "
            "e.g., 3.10, 3.10.1, etc."
        )

    resolved_python_version = ".".join((major, minor, patch))
    return f"~={resolved_python_version}"


def write_python_version(python_version):
    with open("pyproject.toml", "r") as f:
        doc = tomlkit.parse(f.read())

    doc["project"]["requires-python"] = resolve_compatible_python_version(python_version)
    with open("pyproject.toml", "w") as f:
        f.write(tomlkit.dumps(doc))


def write_dependencies(
    dependencies, packages, pip_only_packages, repo_name, module_name, python_version
):
    if dependencies == "requirements.txt":
        with open(dependencies, "w") as f:
            lines = sorted(packages)

            lines += ["" "-e ."]

            f.write("\n".join(lines))
            f.write("\n")

    elif dependencies == "pyproject.toml":
        with open(dependencies, "r") as f:
            doc = tomlkit.parse(f.read())
        doc["project"].add("dependencies", sorted(packages))
        doc["project"]["dependencies"].multiline(True)

        with open(dependencies, "w") as f:
            f.write(tomlkit.dumps(doc))

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
