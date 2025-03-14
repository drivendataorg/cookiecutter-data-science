{
  description = "{{ cookiecutter.description }}";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
    nix-bundle.url = "github:matthewbauer/nix-bundle";
  };

  outputs =
    {
      self,
      nixpkgs,
      flake-utils,
      nix-bundle,
    }:
    flake-utils.lib.eachDefaultSystem (
      system:
      let
        pkgs = nixpkgs.legacyPackages.${system};
      in
      {
        packages = rec {
          {{ cookiecutter.module_name }} = pkgs.callPackage ./default.nix { };
          default = {{ cookiecutter.module_name }};
          bundle = nix-bundle.bundlers.${system}.bundle self.packages.${system}.default;
        };

        apps = rec {
          {{ cookiecutter.module_name }} = flake-utils.lib.mkApp { drv = self.packages.${system}.{{ cookiecutter.module_name }}; };
          default = {{ cookiecutter.module_name }};
        };
      }
    );
}
