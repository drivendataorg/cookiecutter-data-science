import os
import pytest
from pathlib import Path


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
        assert ("Learn more about the purpose and how to use this model [here](docs/index.md)" in lines)

    def test_requirements(self):
        reqs_path = self.path / "requirements.txt"
        assert reqs_path.exists()
        assert no_curlies(reqs_path)

        with open(reqs_path) as fin:
            lines = list(map(lambda x: x.strip(), fin.readlines()))
        assert "# Example: expackage==2.4.1" in lines

    def test_dockerfile(self):
        dockerfile_path = self.path / "Dockerfile"
        assert dockerfile_path.exists()
        assert no_curlies(dockerfile_path)
        with open(dockerfile_path) as fin:
            lines = list(map(lambda x: x.strip(), fin.readlines()))
        dockerfile_text = Path(dockerfile_path).read_text()

        assert lines[2] == "FROM registry.git.vgregion.se/aiplattform/images/r:0.1.1"
        assert "ADD http://aiav2.vgregion.se/VGC%20Root%20CA%20v2.crt /tmp/vgc_root.der" in lines
        assert "ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2.crt /tmp/vgc_issuing1.der" in lines
        assert "ADD http://aiav2.vgregion.se/VGC%20Issuing%202%20CA%20v2.crt /tmp/vgc_issuing2.der" in lines
        assert """RUN pip install -r requirements.txt \\
    && openssl x509 -inform der -in /tmp/vgc_root.der -out /usr/local/share/ca-certificates/vgc_root.crt \\
    && openssl x509 -inform der -in /tmp/vgc_issuing1.der -out /usr/local/share/ca-certificates/vgc_issuing1.crt \\
    && openssl x509 -inform der -in /tmp/vgc_issuing2.der -out /usr/local/share/ca-certificates/vgc_issuing2.crt \\
    && update-ca-certificates""" in dockerfile_text

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
