"""Removes unnecessary files and simplifies scaffold based on options given."""

from collections.abc import Callable
from pathlib import Path
import shutil
from typing import Literal
from loguru import logger

CleaningOption = Literal["data", "paper", "app", "ml", "lib", "course"]
CleaningOperation = Callable[[Path], None]


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
                cleaning_ops.add(lambda: self._select_module_scaffolding("ai"))
                continue
            if option == "paper":
                cleaning_ops.add(lambda: self._select_module_scaffolding("course"))
                continue
            if option == "app":
                cleaning_ops.add(lambda: self._remove_dir(self.root / "notebooks"))
                continue
            if option == "ml":
                cleaning_ops.add(lambda: self._select_module_scaffolding("ai"))
                continue
            if option == "lib":
                cleaning_ops.add(lambda: self._remove_dir(self.root / "out"))
                continue
            if option == "course":
                cleaning_ops.add(lambda: self._select_module_scaffolding("course"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "Taskfile.yml"))
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

    def _select_module_scaffolding(
        self,
        scaffold: Literal["ai", "backend", "course", "frontend"],
    ) -> None:
        """Delete all config except for the config passed in."""
        module_path = self.root / self.module_name
        all_scaffolds = {"ai", "backend", "course", "frontend"}
        for unselected_scaffold in all_scaffolds - {scaffold}:
            self._remove_dir(module_path / f"_{unselected_scaffold}")

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
        if not path.exists():
            logger.warning(f"Path does not exist: {path}")
            return
        path.unlink()

    def _remove_dir(self, dir_path: Path) -> None:
        """Removes specified high-level directory and subfiles."""
        if not (dir_path.exists() and dir_path.is_dir()):
            err_msg = f"{dir_path} is fake news"
            raise Exception(err_msg)
        shutil.rmtree(dir_path)
