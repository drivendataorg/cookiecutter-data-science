import os
import pytest
from pathlib import Path
from subprocess import check_output
from conftest import system_check


def no_curlies(filepath):
    """Utility to make sure no curly braces appear in a file.
    That is, was Jinja able to render everything?
    """
    with open(filepath, "r") as f:
        data = f.read()

    template_strings = ["{{", "}}", "{%", "%}"]

    template_strings_in_file = [s in data for s in template_strings]
    return not any(template_strings_in_file)


@pytest.mark.usefixtures("pytorch_project")
class TestCookieSetup(object):
    def test_project_name(self):
        project = self.path
        if pytest.param.get("project_name"):
            name = system_check("DrivenData")
            assert project.name == name
        else:
            assert project.name == "project_name"

    def test_author(self):
        setup_ = self.path / "setup.py"
        args = ["python", str(setup_), "--author"]
        p = check_output(args).decode("ascii").strip()
        if pytest.param.get("author_name"):
            assert p == "DrivenData"
        else:
            assert p == "Your name (or your organization/company/team)"

    def test_readme(self):
        readme_path = self.path / "README.md"
        assert readme_path.exists()
        assert no_curlies(readme_path)
        if pytest.param.get("project_name"):
            with open(readme_path) as fin:
                assert "DrivenData" == next(fin).strip()

    def test_setup(self):
        setup_ = self.path / "setup.py"
        args = ["python", str(setup_), "--version"]
        p = check_output(args).decode("ascii").strip()
        assert p == "0.1.0"

    def test_license(self):
        license_path = self.path / "LICENSE"
        assert license_path.exists()
        assert no_curlies(license_path)

    def test_license_type(self):
        setup_ = self.path / "setup.py"
        args = ["python", str(setup_), "--license"]
        p = check_output(args).decode("ascii").strip()
        if pytest.param.get("open_source_license"):
            assert p == "MIT"
        else:
            assert p == "BSD-3"

    def test_requirements(self):
        reqs_path = self.path / "requirements.txt"
        assert reqs_path.exists()
        assert no_curlies(reqs_path)
        if pytest.param.get("image"):
            with open(reqs_path) as fin:
                lines = list(map(lambda x: x.strip(), fin.readlines()))
            assert "# Example: expackage==2.4.1" in lines

    def test_doitfile(self):
        doitfile_path = self.path / "dodo.py"
        assert doitfile_path.exists()
        assert no_curlies(doitfile_path)

    def test_dockerfile(self):
        dockerfile_path = self.path / "Dockerfile"
        assert dockerfile_path.exists()
        assert no_curlies(dockerfile_path)
        with open(dockerfile_path) as fin:
            lines = list(map(lambda x: x.strip(), fin.readlines()))
        dockerfile_text = Path(dockerfile_path).read_text()
        
        assert lines[1] == "FROM registry.git.vgregion.se/aiplattform/images/pytorch:0.3.2"
        assert lines[-1] == 'WORKDIR /workspace'
        assert "ADD http://aiav2.vgregion.se/VGC%20Root%20CA%20v2.crt /tmp/vgc_root.der" in lines
        assert "ADD http://aiav2.vgregion.se/VGC%20Issuing%201%20CA%20v2.crt /tmp/vgc_issuing1.der" in lines
        assert "ADD http://aiav2.vgregion.se/VGC%20Issuing%202%20CA%20v2.crt /tmp/vgc_issuing2.der" in lines
        assert "pip install -r requirements.txt"
        assert "openssl x509 -inform der -in /tmp/vgc_root.der -out /usr/local/share/ca-certificates/vgc_root.crt"
        assert "openssl x509 -inform der -in /tmp/vgc_issuing1.der -out /usr/local/share/ca-certificates/vgc_issuing1.crt"
        assert "openssl x509 -inform der -in /tmp/vgc_issuing1_2.der -out /usr/local/share/ca-certificates/vgc_issuing1_2.crt"
        assert "openssl x509 -inform der -in /tmp/vgc_issuing2.der -out /usr/local/share/ca-certificates/vgc_issuing2.crt"
        assert "update-ca-certificates"
        
    def test_folders(self):
        module_name = "project_name"
        if pytest.param.get("project_name"):
            module_name = "drivendata"

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
        module_name = "project_name"
        if pytest.param.get("project_name"):
            module_name = "drivendata"

        _, _, abs_files = list(
            zip(*os.walk(os.path.join(self.path, module_name, "data")))
        )

        assert len(abs_files[0]) == 3
        assert ".gitkeep" in abs_files[0]
        assert "__init__.py" in abs_files[0]
        assert "make_dataset.py" in abs_files[0]

    def test_gitlab_pipeline(self):
        _, _, abs_files = list(zip(*os.walk(self.path)))

        assert ".gitlab-ci.yml" in abs_files[0]