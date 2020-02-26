#!/usr/bin/env python
import subprocess
import sys

try:
    subprocess.run(["make", "execute_init_test"], check=True)
except subprocess.CalledProcessError:
    sys.exit(1)
