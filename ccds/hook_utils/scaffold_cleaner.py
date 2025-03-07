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

    def __init__(self, root: Path, module_name: str, project_short_description: str = "") -> None:
        """Returns new scaffolding cleaner with a set root."""
        self.root = root
        self.module_name = module_name
        self.project_short_description = project_short_description

    def __call__(self, cleaning_options: list[CleaningOption] | None = None) -> None:
        """Removes unnecessary files and simplifies scaffold based on options given."""
        ## Collect cleaning operations to perform w/o duplicates

        if cleaning_options is None:
            self._remove_all_scaffolding()
            return

        cleaning_ops = {self._remove_experimental}
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
                cleaning_ops.add(lambda: self._remove_dir(self.root / ".devcontainer"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / ".github"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "data"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "docker"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "docs"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "logs"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "notebooks"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "out"))
                continue

        ## Execute cleaning operations
        for op in cleaning_ops:
            op()

    def _remove_all_scaffolding(self) -> None:
        # remove everything except __init__.py so result is an empty package
        self._create_blank_module()
        self._remove_dir(self.root / ".devcontainer")
        self._remove_experimental()

    def _create_blank_module(self) -> None:
        """Remove everything except __init__.py so result is an empty package."""
        for generated_path in (self.root / self.module_name).iterdir():
            if generated_path.is_dir():
                shutil.rmtree(generated_path)
            elif generated_path.name != "__init__.py":
                generated_path.unlink()
            elif generated_path.name == "__init__.py":
                # remove any content in __init__.py since it won't be available
                generated_path.write_text(
                    f'"""{self.module_name}: {self.project_short_description}."""\n',
                )

    def _remove_experimental(self) -> None:
        """Removes experimental files and features."""
        self._remove_file(self.root / "Taskfile.yml")

    def _remove_file(self, path: Path) -> None:
        """Remove file at specified path."""
        path.unlink()

    def _remove_dir(self, dir_path: Path) -> None:
        """Removes specified high-level directory and subfiles."""
        if not (dir_path.exists() and dir_path.is_dir()):
            err_msg = f"{dir_path} is fake news"
            raise Exception(err_msg)
        shutil.rmtree(dir_path)
