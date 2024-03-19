import json
from pathlib import Path
import re

PROJECT_ROOT = Path(__file__).parents[2]


def _table_row(items, delimiter="|"):
    return f"| {' | '.join(items)} |"


def _ccds_help_to_lookups(help, prefix="", out=None):
    if out is None:
        out = {}

    for item in help:
        # add this item to the help
        item_name = item.get("field", item.get("choice"))
        item_key = item_name if not prefix else f"{prefix}.{item_name}"
        out[item_key] = item["help"]

        if choices := item.get("choices", None):
            out.update(_ccds_help_to_lookups(choices, prefix=item_key, out=out))

        if subfields := item.get("subfields", None):
            out.update(_ccds_help_to_lookups(subfields, prefix=item_key, out=out))

    return out


def build_help_table_rows(data, help_lookup, lookup_prefix=""):
    body_items = []
    for top_key, top_value in data.items():
        # top value is string, so it is just user entry
        if isinstance(top_value, str):
            item_help = help_lookup[f"{lookup_prefix}{top_key}"]

            #  simplify template render string
            if m := re.search(r"{{ cookiecutter\.(.*) }}", top_value):
                top_value = f"`{m.group(1)}`"

            body_items.append(
                _table_row(
                    (
                        top_key,
                        "string",
                        top_value,
                        "",
                        item_help["description"],
                        item_help["more_information"],
                    )
                )
            )
        elif isinstance(top_value, list):
            choices_help = help_lookup[f"{lookup_prefix}{top_key}"]
            body_items.append(
                _table_row(
                    (
                        top_key,
                        "choice",
                        "",
                        "",
                        choices_help["description"],
                        choices_help["more_information"],
                    )
                )
            )
            for ix, choice in enumerate(top_value):
                if isinstance(choice, str):
                    item_help = help_lookup[f"{lookup_prefix}{top_key}.{choice}"]
                    body_items.append(
                        _table_row(
                            (
                                " ",
                                "choice",
                                choice,
                                "",
                                item_help["description"],
                                item_help["more_information"],
                            )
                        )
                    )
                elif isinstance(choice, dict):
                    choice_key = list(choice.keys())[0]
                    item_help = help_lookup[f"{lookup_prefix}{top_key}.{choice_key}"]
                    body_items.append(
                        _table_row(
                            (
                                " ",
                                "choice",
                                choice_key,
                                "",
                                item_help["description"],
                                item_help["more_information"],
                            )
                        )
                    )

                    # subfields
                    if isinstance(choice[choice_key], dict):
                        for subfield_key, subfield_value in choice[choice_key].items():
                            subfield_help = help_lookup[
                                f"{lookup_prefix}{top_key}.{choice_key}.{subfield_key}"
                            ]
                            body_items.append(
                                _table_row(
                                    (
                                        " ",
                                        "choice",
                                        choice_key,
                                        subfield_key,
                                        subfield_help["description"],
                                        subfield_help["more_information"],
                                    )
                                )
                            )

    return body_items


def render_options_table():
    with (PROJECT_ROOT / "ccds.json").open() as f:
        data = json.load(f)

    with (PROJECT_ROOT / "ccds-help.json").open() as f:
        help = json.load(f)
        help_lookup = _ccds_help_to_lookups(help)

    header = [
        _table_row(
            (
                "Prompt",
                "Type",
                "Choice/Default",
                "Sub-choice",
                "Description",
                "More information",
            )
        ),
        _table_row(["---"] * 6),
    ]

    body_items = build_help_table_rows(data, help_lookup)

    output = "\n".join(header + body_items)
    return output


# script entry point for debugging
if __name__ == "__main__":
    print(render_options_table())

# mkdocs build entry point
else:
    import mkdocs_gen_files

    with mkdocs_gen_files.open("all-options.md", "r") as f:
        options_file = f.read()

    options_file = options_file.replace(
        "<!-- configuration-table.py output -->", render_options_table()
    )

    with mkdocs_gen_files.open("all-options.md", "w") as f:
        f.write(options_file)
