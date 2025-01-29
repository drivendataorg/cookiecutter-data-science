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

(build and publish with devcontainer cli

`devcontainer build --config devcontainer.json --workspace-folder ..`
`docker tag vsc-arena-2025-iap-e8296170ec1ad7a2b612bef7176ffc25df7a7352d1110da1cfb7c3cac7c89741-features ghcr.io/gatlenculp/arena-2025-iap-dev:latest`
`docker push ghcr.io/gatlenculp/arena-2025-iap-dev:latest`
)

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
