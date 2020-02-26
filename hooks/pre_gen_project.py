#!/usr/bin/env python
import subprocess
import sys

try:
    subprocess.run(["py.test", "tests"], check=True)
except subprocess.CalledProcessError:
    sys.exit(1)
