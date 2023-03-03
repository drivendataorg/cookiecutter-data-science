{
  inputs = {
    nixpkgs.url = "github:nixos/nixpkgs";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = {
    self,
    nixpkgs,
    flake-utils,
  }:
    flake-utils.lib.eachDefaultSystem (
      system: let
        pkgs = nixpkgs.legacyPackages.${system};
        python-packages = p:
          with p; [
            cookiecutter
            pytest
            setuptools
          ];
      in {
        devShell = pkgs.mkShell {
          buildInputs = with pkgs; [
            (python39.withPackages python-packages)
            black
            ruff
            nodePackages.pyright
            nodePackages.bash-language-server
            shellcheck
            checkbashisms
            shfmt
            hadolint
            nil
            alejandra
          ];
        };
      }
    );
}
