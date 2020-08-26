"""Utilities for internal and external html reports.

Top level function :func:`src.reports.make_report` writes a report to disk. It
can leverage any reporting function that takes a file-like object ``f`` and
returns a string with an html report.

Run this module as a script to create project reports.

"""
from src import utils


# Paths to inputs (i.e. templates) and outputs (i.e. reports).
PATHS = {
    "basic-table": utils.PATHS["templates"] / "basic-table.html",
}


def make_report(template_path, report_path, function, *args, **kwargs):
    """Make and save a report from a template and a ``report_*`` function.

    Args:
        template_path (str, path): The path to the report template.
        report_path (str, path): The path at which to save the report.
        function (callable): The function to create the report html.
        args: Positional arguments passed to ``function``.
        kwargs: Keyword arguments passed to ``function``.

    Returns:
        str: The path to the report.

    """
    # Create the report content.
    with open(template_path) as f:
        content = function(*args, f=f, **kwargs)

    # Write to the target directory.
    with open(report_path, "w+") as f:
        f.write(content)

    return report_path


if __name__ == "__main__":

    # Add make_report calls to create reports.
    pass
