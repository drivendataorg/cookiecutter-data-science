# Commandline options

CCDS provides a number of choices that you can use to customize your project. The defaults work well for many projects, but lots of tooling choices are supported. Here are the options for tools that you can use:


<!-- configuration-table.py output -->

## Checking out other branches / using unreleased changes to the template

By default, `ccds` will download the most recently _released_ version of the template. If there are any _unreleased_ changes to the template (or changes in a separate branch) that you want to incorporate, you can do so by checking out whatever branch you'd like to use (checkout `master` for the latest changes):

```bash
ccds -c master
```
