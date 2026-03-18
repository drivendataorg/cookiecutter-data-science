from collections import OrderedDict

import pytest
from cookiecutter.exceptions import CookiecutterException

from ccds import monkey_patch


def test_fails_fast_if_repo_directory_already_exists(tmp_path, monkeypatch):
    existing_repo_name = "existing-repo"
    (tmp_path / existing_repo_name).mkdir()
    monkeypatch.chdir(tmp_path)

    prompts_seen = []

    def fake_read_user_variable(key, val):
        prompts_seen.append(key)
        if key == "project_name":
            return "My Project"
        if key == "repo_name":
            return existing_repo_name
        raise AssertionError("prompt_for_config should stop before this prompt")

    monkeypatch.setattr(monkey_patch, "read_user_variable", fake_read_user_variable)

    context = {
        "cookiecutter": OrderedDict(
            [
                ("project_name", "project_name"),
                ("repo_name", "repo_name"),
                ("module_name", "module_name"),
            ]
        )
    }

    with pytest.raises(CookiecutterException, match="already exists"):
        monkey_patch.prompt_for_config(context, no_input=False)

    assert prompts_seen == ["project_name", "repo_name"]
