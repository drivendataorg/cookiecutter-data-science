"""Removes unnecessary files and simplifies scaffold based on options given."""

from collections.abc import Callable
from pathlib import Path
import shutil
from typing import Literal

CleaningOption = Literal["data", "paper", "app", "ml", "lib", "course"]
CleaningOperation = Callable[[Path], None]
# cleaning_map: dict[CleaningOption, list[CleaningOperation]] = {"course": [_clean_devcontainer]}


class ScaffoldCleaner:
    """Removes unnecessary files and simplifies scaffold based on options given."""

    def __init__(self, root: Path) -> None:
        """Returns new scaffolding cleaner with a set root."""
        self.root = root

    def __call__(self, cleaning_options: list[CleaningOption] | None = None) -> bool:
        """Removes unnecessary files and simplifies scaffold based on options given."""
        ## Collect cleaning operations to perform w/o duplicates

        if cleaning_options is None:
            self._remove_all_scaffolding()

        cleaning_ops = {}
        for option in cleaning_options:
            if option == "data":
                continue
            if option == "paper":
                continue
            if option == "app":
                continue
            if option == "ml":
                continue
            if option == "lib":
                continue
            if option == "course":
                cleaning_ops.add(self._rename_devcontainer)
                continue

        ## Execute cleaning operations
        for op in cleaning_ops:
            op()

    def _remove_all_scaffolding(self) -> None:
        # remove everything except __init__.py so result is an empty package
        for generated_path in Path("{{ cookiecutter.module_name }}").iterdir():
            if generated_path.is_dir():
                shutil.rmtree(generated_path)
            elif generated_path.name != "__init__.py":
                generated_path.unlink()
            elif generated_path.name == "__init__.py":
                # remove any content in __init__.py since it won't be available
                generated_path.write_text(
                    '"""{{ cookiecutter.module_name }}: {{ cookiecutter.project_short_description }}."""\n',
                )

    def _rename_devcontainer(self) -> None:
        """Cleans devcontainer configuration."""
        # remove `.devcontainer` and subfiles
        print(self.root)
