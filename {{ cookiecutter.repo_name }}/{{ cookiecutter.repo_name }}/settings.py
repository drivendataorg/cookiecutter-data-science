'''
Stores re-usable settings for this module. If you need them, just import this file.

It is important that you should use these settings only on an entry layer of your code. If you would use them
in a domain layer, then it would be really hard to test that code in many cases.

These settings should be set to work out of the box on a development environment.
Production settings will be injected by Environment variables.

If you want to customize these settings, create a .env file instead of editing them here.
This will ensure that you won't by mistake commit your own settings to a repository.
'''
from dataclasses import dataclass, field
import os
from pathlib import Path
from typing import TypedDict

from dotenv import load_dotenv

load_dotenv()

BASE = Path(__file__).parent.parent


class UpdateSettings(TypedDict, total=False):
    DATA_PATH: Path

@dataclass
class Settings:
    # pylint: disable=invalid-name
    DATA_PATH: Path
    # OTHER_PATH: Path = field(init=False)

    # def __post_init__(self):
    #     self.OTHER_PATH = Path(os.getenv("OTHER_PATH", self.PATH / "other_path"))

    def update(self, new_settings: UpdateSettings):
        for key, value in new_settings.items():
            setattr(self, key, value)

        # self.__post_init__()


settings = Settings(
    DATA_PATH=BASE / "data_path",
)


def update_settings(new_settings: UpdateSettings):
    settings.update(new_settings)
