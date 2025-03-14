"""Removes unnecessary files and simplifies scaffold based on options given."""

import shutil
from collections.abc import Callable
from pathlib import Path
from typing import Literal

from loguru import logger

SecretManagers = Literal["none", "dot_env", "secrets_dir"]
CleaningOption = Literal["data", "paper", "app", "ml", "lib", "course"]
ScaffoldOptions = Literal["data", "backend", "course", "frontend"]
CleaningOperation = Callable[[Path], None]

ALL_SCAFFOLDS = {"data", "backend", "course", "frontend", "cli"}


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
                cleaning_ops.add(lambda: self._select_module_scaffolding({"data", "cli"}))
                cleaning_ops.add(lambda: self._select_secrets_manager("secrets_dir"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                continue
            if option == "ml":
                cleaning_ops.add(lambda: self._select_module_scaffolding({"data", "cli"}))
                cleaning_ops.add(lambda: self._select_secrets_manager("secrets_dir"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                continue
            if option == "lib":
                cleaning_ops.add(lambda: self._select_module_scaffolding("data"))
                cleaning_ops.add(lambda: self._select_secrets_manager("dot_env"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "out"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                continue
            if option == "app":
                cleaning_ops.add(
                    lambda: self._select_module_scaffolding({"backend", "frontend", "cli"}),
                )
                cleaning_ops.add(lambda: self._select_secrets_manager("dot_env"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "notebooks"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                continue
            if option == "paper":
                cleaning_ops.add(lambda: self._select_module_scaffolding("course"))
                cleaning_ops.add(lambda: self._select_secrets_manager("dot_env"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                continue
            if option == "course":
                cleaning_ops.add(lambda: self._select_module_scaffolding("course"))
                cleaning_ops.add(lambda: self._select_secrets_manager("dot_env"))
                # Dirs
                cleaning_ops.add(lambda: self._remove_dir(self.root / ".devcontainer"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / ".github"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "data"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "docker"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "docs"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "logs"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "notebooks"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "out"))
                cleaning_ops.add(lambda: self._remove_dir(self.root / "tests"))
                # Files
                cleaning_ops.add(lambda: self._remove_file(self.root / "biome.json"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "Taskfile.yml"))
                cleaning_ops.add(lambda: self._remove_file(self.root / "LICENSE"))
                continue

        ## Execute cleaning operations
        for op in cleaning_ops:
            op()

    def _remove_all_scaffolding(self) -> None:
        # remove everything except __init__.py so result is an empty package
        self._create_blank_module()
        self._remove_dir(self.root / ".devcontainer")
        self._remove_experimental()

    def _select_module_scaffolding(self, scaffold: ScaffoldOptions | set[ScaffoldOptions]) -> None:
        """Delete all config except for the config passed in."""
        selected_scaffolds = scaffold if isinstance(scaffold, set) else {scaffold}
        module_path = self.root / self.module_name
        for unselected_scaffold in ALL_SCAFFOLDS - selected_scaffolds:
            self._remove_dir(module_path / f"_{unselected_scaffold}")

        # Extract the remaining directory into the module directory
        if isinstance(scaffold, str):
            selected_scaffold_path = module_path / f"_{scaffold}"
            self._extract_dir(selected_scaffold_path)
            return

        # If scaffold was a set, rename the scaffold directories to not have the underscore
        for selected_scaffold in selected_scaffolds:
            scaffold_path = module_path / f"_{selected_scaffold}"
            if scaffold_path.exists() and scaffold_path.is_dir():
                target_path = module_path / selected_scaffold
                self._rename(scaffold_path, target_path)

    def _rename(self, src_path: Path, target_path: Path) -> None:
        """Renames a given path to that at the target path."""
        logger.debug(f"Renaming {src_path} to {target_path}")
        # If target already exists, remove it first
        if target_path.exists():
            if target_path.is_dir():
                shutil.rmtree(target_path)
            else:
                target_path.unlink()
        # Rename the directory
        src_path.rename(target_path)
        logger.info(f"Renamed {src_path} to {target_path}")

    def _extract_dir(self, path: Path) -> None:
        """Extracts the given path to the parent file and deletes the original directory."""
        if path.exists() and path.is_dir():
            # Copy all contents from the selected scaffold to the module directory
            for item in path.iterdir():
                target_path = path.parent / item.name
                logger.debug(f"Moving {item} to {target_path}")
                if item.is_dir():
                    if target_path.exists():
                        shutil.rmtree(target_path)
                    shutil.copytree(item, target_path)
                else:
                    if target_path.exists():
                        target_path.unlink()
                    shutil.copy2(item, target_path)

            # Remove the scaffold directory after extraction
            shutil.rmtree(path)
            logger.info(f"Extracted contents from _{path} scaffold into {target_path} directory")

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
        self._remove_nix()

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

    def _remove_nix(self) -> None:
        """Removes the nix flake install files."""
        self._remove_file(self.root / "default.nix")
        self._remove_file(self.root / "flake.nix")

    def _select_secrets_manager(self, secrets_manager: SecretManagers) -> None:
        """Removes the secrets directory, transferring example.env to project root."""
        if secrets_manager == "none":
            self._remove_dir(self.root / "secrets")
            return
        if secrets_manager == "dot_env":
            example_env_path = self.root / "secrets" / "schema" / "example.env"
            shutil.copy2(example_env_path, self.root / "example.env")
            self._remove_dir(self.root / "secrets")
            return
        if secrets_manager == "secrets_dir":
            return
