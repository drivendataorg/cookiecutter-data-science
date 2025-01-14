# Containerization

______________________________________________________________________

## Containerization Platforms

- Docker Desktop
- OrbStack

### Docker

- `docker/` directory provides a sample Dockerfile (and `docker-compose.yml` file).

### Kubernetes (TODO)

- Not set up, unsure if it ever will be

### Nix (TODO)

______________________________________________________________________

## Uses

### Devcontainers

- Already set up via `.devcontainer`
- Heavy image meant for development

### Whalebrew

Users can install your docker image and run a command from within it as if it were local. This is paired with the Docker file in your project

______________________________________________________________________

## Image Registries

______________________________________________________________________

## Recommended Images

[uv images for Docker](https://docs.astral.sh/uv/guides/integration/docker/) are quite nice. I recommend using the heavier `bookworm` for easy development, then switching to the lighter `alpine` and install all other necessary packages for actual deployment.

______________________________________________________________________

## Misc

### VSCode Extensions

- [Better DockerFile Syntax](https://marketplace.visualstudio.com/items?itemName=jeff-hykin.better-dockerfile-syntax)
- [Hadolint](https://marketplace.visualstudio.com/items?itemName=exiasr.hadolint)
