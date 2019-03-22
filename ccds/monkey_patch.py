from collections import OrderedDict
import json

import click
from past.builtins import basestring

from future.utils import iteritems

from jinja2.exceptions import UndefinedError

from cookiecutter.exceptions import UndefinedVariableInTemplate
from cookiecutter.environment import StrictEnvironment


from cookiecutter.prompt import (prompt_choice_for_config, render_variable, read_user_variable, read_user_choice)

def _prompt_choice_and_subitems(cookiecutter_dict, env, key, options, no_input):
    result = {}
    
    # first, get the selection
    rendered_options = [
        render_variable(env, list(raw.keys())[0], cookiecutter_dict) for raw in options
    ]

    if no_input:
        selected = rendered_options[0]
    
    selected = read_user_choice(key, rendered_options)
    
    selected_item = [list(c.values())[0] for c in options if list(c.keys())[0] == selected][0]

    result[selected] = {}

    # then, fill in the sub values for that item
    for subkey, raw in selected_item.items():
        # We are dealing with a regular variable
        val = render_variable(env, raw, cookiecutter_dict)

        if not no_input:
            val = read_user_variable(subkey, val)

        result[selected][subkey] = val

    return result


def prompt_for_config(context, no_input=False):
    """
    Prompts the user to enter new config, using context as a source for the
    field names and sample values.
    :param no_input: Prompt the user at command line for manual configuration?
    """
    cookiecutter_dict = OrderedDict([])
    env = StrictEnvironment(context=context)

    # First pass: Handle simple and raw variables, plus choices.
    # These must be done first because the dictionaries keys and
    # values might refer to them.
    for key, raw in iteritems(context[u'cookiecutter']):
        if key.startswith(u'_'):
            cookiecutter_dict[key] = raw
            continue

        try:
            if isinstance(raw, list):
                if isinstance(raw[0], dict):
                    val = _prompt_choice_and_subitems(
                        cookiecutter_dict, env, key, raw, no_input
                    )
                    cookiecutter_dict[key] = val
                else:
                    # We are dealing with a choice variable
                    val = prompt_choice_for_config(
                        cookiecutter_dict, env, key, raw, no_input
                    )
                    cookiecutter_dict[key] = val
            elif not isinstance(raw, dict):
                # We are dealing with a regular variable
                val = render_variable(env, raw, cookiecutter_dict)

                if not no_input:
                    val = read_user_variable(key, val)

                cookiecutter_dict[key] = val
        except UndefinedError as err:
            msg = "Unable to render variable '{}'".format(key)
            raise UndefinedVariableInTemplate(msg, err, context)

    # Second pass; handle the dictionaries.
    for key, raw in iteritems(context[u'cookiecutter']):

        try:
            if isinstance(raw, dict):
                # We are dealing with a dict variable
                val = render_variable(env, raw, cookiecutter_dict)

                if not no_input:
                    val = read_user_dict(key, val)

                cookiecutter_dict[key] = val
        except UndefinedError as err:
            msg = "Unable to render variable '{}'".format(key)
            raise UndefinedVariableInTemplate(msg, err, context)

    return cookiecutter_dict

# from cookiecutter.main import cookiecutter
# from cookiecutter import prompt
# from cookiecutter.cli import main as cc_main

# class NestedQuestion:
#     ''' [{'a': {'val1': 'default1', 'val2': 'default2'}}]
    
#         Interprets lists as questions with multiple options, where the
#         and dictionaries as single questions with defaults values.
#     '''
#     @classmethod
#     def update_context(cls, context, question_structure):
#         qd = question_structure
#         if isinstance(qd, list):
#             selection = cls.get_user_option(qd)
            
#             name, vals = list(selection.items())[0]
            
#             context[name] = {}
#             cls.update_context(context[name], vals)

#         elif isinstance(qd, dict):
#             for k, v in qd.items():
#                 context[k]= {}
                
#                 if isinstance(v, (dict, list)):
#                     context[k] = cls.update_context(context[k], v)
#                 else:
#                     context[k] = cls.get_user_input(k, v)
            
#         return context

#     @staticmethod
#     def get_user_input(key, default):
#         return prompt.read_user_variable(key, default)
#         # return input(f"{key} [{default}]: ") or default

#     @staticmethod
#     def get_user_option(options):
#         prompt.read_user_choice()
        
#         # input_msg = '\n'.join(
#         #     f" [{ix + 1}] - {list(value.keys())[0]}" for ix, value in enumerate(options)
#         # )

#         # prepend = 'Select an item:\n'
#         # postpend = "\n - Enter number [1]: "
        
#         # ix = int(input(prepend + input_msg + postpend) or 1) - 1
#         # return options[ix]
