import json
from pathlib import Path
import re
import sys

# 2/3 compat
try:
    input = raw_input
except NameError:
    pass

import click

# Monkey-patch jinja to allow variables to not exist, which happens with sub-options
import jinja2
jinja2.StrictUndefined = jinja2.Undefined


# Monkey-patch cookiecutter to allow sub-items
import cookiecutter
from cookiecutter import prompt 
from ccds.monkey_patch import prompt_for_config

prompt.prompt_for_config = prompt_for_config

from cookiecutter import cli
main = cli.main


if __name__ == "__main__":
    main()