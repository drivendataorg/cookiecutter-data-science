import pytest

from ccds.monkey_patch import prompt_for_config


@pytest.mark.parametrize(
    "response, expected",
    [("", {"project": "demo"}), ('{"project": "custom"}', {"project": "custom"})],
)
def test_interactive_dictionary_prompt(monkeypatch, response, expected):
    responses = iter(["", response])
    monkeypatch.setattr("builtins.input", lambda *args: next(responses))
    context = {
        "cookiecutter": {
            "project_name": "demo",
            "metadata": {"project": "{{ cookiecutter.project_name }}"},
        }
    }

    result = prompt_for_config(context)

    assert result["metadata"] == expected


def test_dictionary_prompt_without_input():
    context = {
        "cookiecutter": {
            "project_name": "demo",
            "metadata": {"project": "{{ cookiecutter.project_name }}"},
        }
    }

    result = prompt_for_config(context, no_input=True)

    assert result["metadata"] == {"project": "demo"}
