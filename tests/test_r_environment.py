import os
import pytest


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("r_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.path

        assert project.name == "r_project_name"

    def test_readme(self):
        readme_path = self.path / "README.md"
        assert readme_path.exists()
        assert no_curlies(readme_path)

        with open(readme_path) as fin:
            lines = list(map(lambda x: x.strip(), fin.readlines()))

        assert "r_project_name" in lines
        assert (
            "Visit [localhost:8787](http://localhost:8787) in your browser and log in with username ```rstudio``` and" +
            " the password you set when starting the container. Use the terminal in RStudio to run things like ```git``` and ```dvc```."
            in lines
        )

    def test_requirements(self):
        reqs_path = self.path / "requirements.txt"
        assert reqs_path.exists()
        assert no_curlies(reqs_path)

        with open(reqs_path) as fin:
            lines = list(map(lambda x: x.strip(), fin.readlines()))
        assert "dvc>=2.8.1" in lines
        assert "mlflow>=1.21.0" not in lines

    def test_folders(self):
        module_name = pytest.param.get("project_name")

        expected_dirs = [
            "data",
            "data/external",
            "data/interim",
            "data/processed",
            "data/raw",
            "docs",
            "models",
            "notebooks",
            "references",
            "reports",
            "reports/figures",
            f"{module_name}",
            f"{module_name}/data",
            f"{module_name}/features",
            f"{module_name}/models",
            f"{module_name}/visualization",
            "tests",
        ]

        abs_expected_dirs = [str(self.path / d) for d in expected_dirs]
        abs_dirs, _, _ = list(zip(*os.walk(self.path)))

        assert len(set(abs_expected_dirs) - set(abs_dirs)) == 0

    def test_files(self):
        module_name = pytest.param.get("project_name")

        _, _, abs_files = list(
            zip(*os.walk(os.path.join(self.path, module_name, "data")))
        )

        assert len(abs_files[0]) == 2
        assert ".gitkeep" in abs_files[0]
        assert "make_dataset.R" in abs_files[0]
