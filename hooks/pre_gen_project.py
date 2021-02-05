def deprecation_warning():
    print("""

=============================================================================
*** DEPRECATION WARNING ***

Cookiecutter data science is moving to V2 soon, which will entail using
the command `ccds ...` rather than `cookiecutter ...`. The cookiecutter command
will continue to work and this version of the template will still be available,
but you will need to explicitly use the @v1 git tag to select it.

Please update any scripts/automation you have to append the @v1 tag, which is
available now.

For example:
    cookiecutter https://github.com/drivendata/cookiecutter-data-science@v1
=============================================================================

    """)


deprecation_warning()
