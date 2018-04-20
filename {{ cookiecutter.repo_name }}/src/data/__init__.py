from os.path import dirname, basename, isfile
from importlib import import_module
import glob
modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [
    basename(f)[:-3]
    for f in modules
    if isfile(f) and not f.endswith('__init__.py')
]
for f in __all__:
    import_module("." + f, package='src.data')
del basename, dirname, isfile, import_module, glob, modules, f
