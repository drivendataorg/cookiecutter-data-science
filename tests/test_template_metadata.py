import json
from itertools import product
from pathlib import Path

import jinja2
import pytest
import tomlkit

CCDS_ROOT = Path(__file__).parents[1]


@pytest.mark.parametrize("field", ["author_name", "description"])
@pytest.mark.parametrize(
    "value",
    [
        "Analysis \U0001f52c",
        "Analyse caf\u00e9",
        'A "quoted" analysis\\path\nsecond line',
    ],
)
def test_template_metadata_roundtrip(field, value):
    with (CCDS_ROOT / "ccds.json").open(encoding="utf-8") as f:
        options = json.load(f)
    context = {
        key: choices[0] if isinstance(choices, list) else choices
        for key, choices in options.items()
    }
    context["module_name"] = "analysis"
    context[field] = value
    template = jinja2.Environment().from_string(
        (CCDS_ROOT / "{{ cookiecutter.repo_name }}" / "pyproject.toml").read_text(
            encoding="utf-8"
        )
    )
    for license, linting in product(
        options["open_source_license"], options["linting_and_formatting"]
    ):
        context.update(open_source_license=license, linting_and_formatting=linting)
        metadata = tomlkit.parse(template.render(cookiecutter=context))["project"]
        actual = (
            metadata["authors"][0]["name"]
            if field == "author_name"
            else metadata[field]
        )
        assert actual == value
