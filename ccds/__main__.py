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
from ccds.monkey_patch import generate_context_wrapper, prompt_for_config

prompt.prompt_for_config = prompt_for_config


from cookiecutter import generate
from ccds.monkey_patch import generate_context_wrapper
generate.generate_context = generate_context_wrapper

# for use in tests need monkey-patched api main
from cookiecutter import main as api_main
from cookiecutter import cli
main = cli.main


if __name__ == "__main__":
    main()
