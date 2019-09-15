VERSION = (0, 1, 0)

__title__ = "project"
__description__ = "{{ cookiecutter.description }}"
__url__ = ""
__version__ = ".".join(map(str, VERSION))
__author__ = '{{ cookiecutter.author_name }}'
__author_email__ = ""
__licence__ = '{% if cookiecutter.open_source_license == 'MIT' %}MIT{% elif cookiecutter.open_source_license == 'BSD-3-Clause' %}BSD-3{% endif %}'
