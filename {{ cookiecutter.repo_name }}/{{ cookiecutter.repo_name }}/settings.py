'''
Stores re-usable settings for this module. If you need them, just import this file.

It is important that you should use these settings only on an entry layer of your code. If you would use them
in a domain layer, then it would be really hard to test that code in many cases.

These settings should be set to work out of the box on a development environment.
Production settings will be injected by Environment varaibles.

If you want to customize these settings, create a .env file instead of editing them here.
This will ensure that you won't by mistake commit your own settings to a repository.
'''
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE = os.path.dirname(__file__)

DATA_PATH = os.getenv("DATA_PATH", Path(BASE) / '..' / 'data')
