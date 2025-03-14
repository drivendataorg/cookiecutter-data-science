{
  lib,
  python3,
  python3Packages,
}:

python3Packages.buildPythonApplication rec {
  pname = "{{ cookiecutter.module_name }}";
  version = "0.0.1";

  src = ./.;

  format = "pyproject";

  nativeBuildInputs = with python3Packages; [
    hatchling
  ];

  propagatedBuildInputs = with python3Packages; [
    loguru
    pydantic
    rich
    numpy
    python-dotenv
    typer
  ];

  meta = with lib; {
    description = "{{ cookiecutter.description }}";
    homepage = "https://{{ cookiecutter._github_username }}.github.io/{{ cookiecutter.repo_name }}/";
    # {% if cookiecutter.open_source_license == 'MIT' %}
    license = licenses.mit;
    # {% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}
    license = licenses.bsd3
    # {% endif %}
    maintainers = with maintainers; [ "{{ cookiecutter.author_name }}" ];
  };
}
