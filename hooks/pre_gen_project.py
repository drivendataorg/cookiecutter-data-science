#!/usr/bin/env python
import subprocess
import sys

try:
    subprocess.run(["make", "test_remote_url"], check=True)
except subprocess.CalledProcessError:
    sys.exit(1)
