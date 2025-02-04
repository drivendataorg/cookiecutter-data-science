# Package, Project, and Environment Management

Since this is derived from [CookieCutter Data Science](<>), this project supports multiple project managers but the one I specifically develop for is [uv](https://docs.astral.sh/uv/), an up-and-coming project, package, and virtual environment manager written in Rust which is extremely fast, developed by Astral, the same team behind the [Ruff linter](<>). It's really a modern, wonderful all-in-one tool.

It replaces `pip`, `pip-tools`, `pipx`, `poetry`, `pyenv`, `twine`, `virtualenv`, and more.

The [docs](https://docs.astral.sh/uv/) explain things better than I can and doesn't involve learning much additional syntax.

I swear, with uv you can go from a new project to a PyPi distribution in seconds.

The only thing uv is missing is a backend-build tool. Frankly, this isn't a huge deal and it works seamlessly with other build tools since it uses a pip-like syntax, but the team is currently working on Rye.

There's a ton of extra benefits as well, this is a very fleshed out and well documented tool that combines the functionality of multiple tools in a way that makes complete sense.

Speed is helpful for a few reasons.

- Image building (github actions, docker images, deployment, ci/cd tools, etc.)
- Easy of use.

## Alternatives

**Package Managers**

- pip - Old, slow, but universal. uv has you describe packages in a pip-compatible way unlike poetry.
- poetry - A wonderful tool for development, more mature than uv, has a number of features, but is overall slow and has you use a different syntax for specifying packages than pip.
- rye - A another great package manager, this was actually transferred to Astral and they are currently writing it from scratch. They recommend using uv if you're using rye.
- pdm - Also chill.

**Global pip tools**

- pipx
- pipenv

**Environment Mangers**
uv will set up your entire virtual environment for you in accordance with your specified packages

- venv - A bit older, built in, this is fine but your have to do everything manually
- virtualenv - uv is essentially virtualenv.
- conda - I lowkey dislike conda. I think it's slow, I have had plenty of conda-specific errors that are hard to resolve and more. I think it's also harder to natively make a distribution with conda(?)

**Build Tools**

- poetry - Also good ig

## Distributing

- PyPi is dirt easy with uv
- Whalebrew, read more on `./containerization.md`
- Homebrew, TODO
  (nbdev?)
