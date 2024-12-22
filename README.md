# Gatlen's Opinionated Template (GOTem)
**_A modern, opinionated full-stack [CookieCutter](https://www.cookiecutter.io/) project template that prioritizes developer experience and cutting-edge tools._**


![PyPI - Version](https://img.shields.io/pypi/v/gatlens-opinionated-template?style=flat)[![tests](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml/badge.svg)](https://github.com/GatlenCulp/gatlens-opinionated-template/actions/workflows/tests.yml) [![Uses the Cookiecutter Data Science project upstream](https://img.shields.io/badge/CCDS-Project%20fork-328F97?logo=cookiecutter)](https://cookiecutter-data-science.drivendata.org/) [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv) ![GitHub stars](https://img.shields.io/github/stars/gatlenculp/homebrew-vivaria?style=social)

> [!WARNING]
> Not yet ready for production!

<div align="center">
  <a href="https://gatlenculp.github.io/gatlens-opinionated-template/">
    <img src="./docs/docs/gotem.png" alt="GOTem Logo" style="max-width: 250px;"/>
  </a>
  <br/>
  <b>Gatlen's Opinionated Template</b>
  <br/>
  <small><i>(Logo = CookieCutter + Gatlen's Stylistic Motif - The Troublesome Goose)</i></small>
</div>
<br>


GOTem is forked from (and synced with) [CookieCutter Data Science (CCDS) V2](https://cookiecutter-data-science.drivendata.org/), one of the most popular, flexible, and well maintained Python templates out there. GOTem extends CCDS with carefully selected defaults, dependency stack, customizations, additional features (that I maybe should have spent time contributing to the original project), and contemporary best practices. Ready for not just data science but also general Python development, research projects, and academic work.


### Key Features
- **🚀 Modern Tooling** Get built-in support for UV, Ruff, FastAPI, Pydantic, Typer, Loguru, and Polars, so you’re ready to tackle cutting-edge Python.

- **🙌 Instant Git Setup** Start coding fast with automatic repo creation, branch protections, and sensible defaults out of the box.

- **🔧 Pre-Configured CI/CD** Ready-to-use GitHub Actions and QA checks save you from tedious setup, letting you focus on what matters—shipping quality code.

- **📦 Seamless Publishing** One-stop shop for PyPI uploads, Makefile-driven tasks, and MkDocs docs, all baked right in.

- **🤝 Small-Scale to Scalable** Perfect for solo devs yet robust enough to grow with your team or project scope.

- **🔄 Living Template** Frequently updated to stay in line with Python’s evolving best practices—never worry about missing the next great tool.

- **🏃‍♂️ Start Fast, Stay Strong** Encourages consistent structure, high-quality practices, and minimal friction from day one.

- **🌐 Full-Stack Focus** Covers DevOps, IDE configurations, version control, databases, and more—so you don’t have to piece together your ecosystem.

- **🥵 Rare Boilerplates** In addition to configuration for research, this also includes setup for LaTeX homework assignments, web apps, CLI tools, and more (not all at once of course). This is hopefully a one-stop-show of configurations.

### Who this is for

**CCDS** is white bread: simple, familiar, unoffensive, and waiting for your choice of toppings. **GOTem** is the expert-crafted and opinionated “everything burger,” fully loaded from the start for any task you want to do (so long as you want to do it in a specific way). Some of the selections might be an acquired taste and users are encouraged to leave them off as they start and perhaps not all will appreciate my tastes even with time, but it is the setup I find \*_delicious_\*.

<!-- TODO: Place the below side-by-side -->

#### ✅ Use this if...

- **🤖 Legacy-Tool Skeptics** If you frequently mutter, “There has to be a better way,” this template might be your aha moment.
- **🍔 The “Everything Burger” Crowd** Anyone who loves a fully loaded development setup and doesn’t mind removing foreign ingredients they don’t enjoy.
- **🎓 Learners and Perfectionists** Developers who want to explore new tools, master best practices, and produce sexy code and outputs. Those who are in it for the work as much as they are about the artform.
- **⚡ Performance Seekers** Crave modern, efficient libraries? This template prioritizes speed and powerful modern tools with simple syntax.
- **🏗️ Quick-Start Enthusiasts** Need a template that practically sets itself up? GOTem lets you jump straight into coding with minimal overhead.

#### ❌ Do NOT use this if...

- **🛣️ Minimalists** If you want a bare-bones or default setup, this template may seem too opinionated or “extra.”

- **🔎 Micro-Optimizers** If you feel compelled to dissect every customization before writing a single line of code, you might prefer a simpler starting point (though GOTem can be a great reverse-engineering exercise).

- **🕰️ Legacy Lovers** For anyone who prefers tried-and-true defaults to cutting-edge (sometimes experimental) tools. CCDS might be a more straightforward fit.

If you find yourself nodding to these “NOT for you” points, consider sticking with CCDS instead for that classic, “white bread” experience.


**[View the full documentation here](https://gatlenculp.github.io/gatlens-opinionated-template/) ➡️**

---

_The main functionality of this project is kept as close as possible to the CCDS template as to avoid additional maintenance on my end. This might mean a mismatch between practices I recommend and the ones they do. Ex: Makefiles on root, Taskfiles in template._

_See how CCDS compares with regular cookiecutter templates and my decisions [here](https://drivendata.co/blog/ccds-v2). For the most part, I look at CCDS as [Chesterton's Fence](https://www.lesswrong.com/tag/chesterton-s-fence), making sure to check my decisions against theirs before making changes. Still, the [CCDS team notes there's still some missing functionality](https://drivendata.co/blog/ccds-v2#whats-still-missing) including the [lack of a uv installer](https://github.com/drivendataorg/cookiecutter-data-science/discussions/403). The CCDS template still comes with some [nice features](https://drivendata.co/blog/ccds-v2#whats-new). CCDS has also considered [ruff as the default linting + formatting option](https://github.com/drivendataorg/cookiecutter-data-science/pull/387)_



<!-- _I'm looking for a way to use [Cruft](https://cruft.github.io/cruft/) over [CookieCutter](https://www.cookiecutter.io/) + CCDS, but for now, CCDS needs to be used due to their custom configuration_ -->



<!-- It is recommended to use [Cruft](https://cruft.github.io/cruft/) instead of [CookieCutter](https://www.cookiecutter.io/). The resulting project is the same, but with the added option of being able to sync your project with the original template if this repository updates as if it were an incomming commit.

Clone using Cruft
```bash
    cruft create https://github.com/GatlenCulp/gatlens-opinionated-template
``` -->

## Getting Started

<b>⚡️ With UV (Recommended)</b>

```bash
uv tool install gatlens-opinionated-template

# From the parent directory where you want your project
uvx --from gatlens-opinionated-template gotem
```

<details>
<summary><b>📦 With Pipx</b></summary>

```bash
pipx install gatlens-opinionated-template

# From the parent directory where you want your project
gotem
```
</details>

<details>
<summary><b>🐍 With Pip</b></summary>

```bash
pip install gatlens-opinionated-template

# From the parent directory where you want your project
gotem
```
</details>


### The resulting directory structure

The directory structure of your new project will look something like this (depending on the settings that you choose):

```
📁 .
├── ⚙️ .cursorrules                    <- LLM instructions for Cursor IDE
├── 💻 .devcontainer                   <- Devcontainer config
├── ⚙️ .gitattributes                  <- GIT-LFS Setup Configuration
├── 🧑‍💻 .github
│   ├── ⚡️ actions
│   │   └── 📁 setup-python-env       <- Automated python setup w/ uv
│   ├── 💡 ISSUE_TEMPLATE             <- Templates for Raising Issues on GH
│   ├── 💡 pull_request_template.md   <- Template for making GitHub PR
│   └── ⚡️ workflows                  
│       ├── 🚀 main.yml               <- Automated cross-platform testing w/ uv, precommit, deptry, 
│       └── 🚀 on-release-main.yml    <- Automated mkdocs updates
├── 💻 .vscode                        <- Preconfigured extensions, debug profiles, workspaces, and tasks for VSCode/Cursor powerusers
│   ├── 🚀 launch.json
│   ├── ⚙️ settings.json
│   ├── 📋 tasks.json
│   └── ⚙️ '{{ cookiecutter.repo_name }}.code-workspace'
├── 📁 data
│   ├── 📁 external                      <- Data from third party sources
│   ├── 📁 interim                       <- Intermediate data that has been transformed
│   ├── 📁 processed                     <- The final, canonical data sets for modeling
│   └── 📁 raw                           <- The original, immutable data dump
├── 🐳 docker                            <- Docker configuration for reproducability
├── 📚 docs                              <- Project documentation (using mkdocs)
├── 👩‍⚖️ LICENSE                           <- Open-source license if one is chosen
├── 📋 logs                              <- Preconfigured logging directory for
├── 👷‍♂️ Makefile                          <- Makefile with convenience commands (PyPi publishing, formatting, testing, and more)
├── 🚀 Taskfile.yml                    <- Modern alternative to Makefile w/ same functionality
├── 📁 notebooks                         <- Jupyter notebooks
│   ├── 📓 01_name_example.ipynb
│   └── 📰 README.md
├── 🗑️ out
│   ├── 📁 features                      <- Extracted Features
│   ├── 📁 models                        <- Trained and serialized models
│   └── 📚 reports                       <- Generated analysis
│       └── 📊 figures                   <- Generated graphics and figures
├── ⚙️ pyproject.toml                     <- Project configuration file w/ carefully selected dependency stacks
├── 📰 README.md                         <- The top-level README
├── 🔒 secrets                           <- Ignored project-level secrets directory to keep API keys and SSH keys safe and separate from your system (no setting up a new SSH-key in ~/.ssh for every project)
│   └── ⚙️ schema                         <- Clearly outline expected variables
│       ├── ⚙️ example.env
│       └── 🔑 ssh
│           ├── ⚙️ example.config.ssh
│           ├── 🔑 example.something.key
│           └── 🔑 example.something.pub
└── 🚰 '{{ cookiecutter.module_name }}'  <- Easily publishable source code
    ├── ⚙️ config.py                     <- Store useful variables and configuration (Preset)
    ├── 🐍 dataset.py                    <- Scripts to download or generate data
    ├── 🐍 features.py                   <- Code to create features for modeling
    ├── 📁 modeling
    │   ├── 🐍 __init__.py
    │   ├── 🐍 predict.py               <- Code to run model inference with trained models
    │   └── 🐍 train.py                 <- Code to train models
    └── 🐍 plots.py                     <- Code to create visualizations
```


## Philosophy 🧭
<!-- 
This project is more of a hobby and research project more than it is a practical template. Gatlen really enjoys the occasional research on the tooling ecosystem and understanding which tools solve what problems and how. He tends to have a very prefectionist perspective on projects beyond what is practical. Many of the packages included in this project, Gatlen has not yet used, but rather examined and compared against other tools and determined to be something to leverage once the need arises. The selection of packages and tools are in a way, a reminder of what resources he has have determined in advance to likely be helpful.

Here are a few guiding principles of this template to determine whether or not you should use it:
1. **Modern and Supported over Ubiquitous** -- Many of the packages and tools I have chosen for this package are NOT the defaults. (Another possible name for this template was "Everything but Defaults"). Unless I deem a built-in library to be the best of its type, it is likely unused. Instead of Logging I used Loguru. Instead of MatPlotLib I use Plotly. Instead of json I used orjson. Instead of pip I used UV. Instead of Django or Flask I used FastAPI. Instead of Argparse I use Typer.  Instead of Time, I use Arrow. Instead of Pandas I use Polars. It's not that these packages aren't used, they are extremely popular and indeed tend to offer better speed and functionality than the "defaults." Perhaps this is simply a selection of trendy packages that add unnecessary bloat and learning curves. But I think these packages can be a helpful learning experience that help me and others leverage the power this new rust-powered python ecosystem of tools that will become increasingly popular with time. Yes, these might not have as much developer documentation or extensions built up around it, but I think they important nonetheless and the novelty is also a plus in the sense that a lot of baggage and backwards-compatability that comes with an established package is not there. There aren't a lot of shitty tutorials from 15 years ago and a bloated API. Instead there is a very clear cut API with great defaults. Often times these packages work just with the sam syntax as the old greats do.
2. **Aspirational over Practical** --...
3. **Simplicity** -- I tend to pick packages that offer a lot of power with very simple and non-intrusive syntax. As an example, Django is a popular web framework that is very opinionated and requires a particular project structure and syntax to play nicely. Indeed, much of what it does is batteries-included best practice with tons of extensions made by the community, but it is also a very heavy library and once you start with a Django project, it is very hard to switch. I try to make it as easy as possible to switch in and out whatever you want to use.
4. **Good Defaults** -- To me, it's important to have good defaults on the packages I have set up so I can just import them and know I'm getting the best experience out of the box. A lot of this is the reason why I choose these modern packages -- because instead of having to bend over backwards to make things backwards compatible, the package can get a hard restart with decades of learning what the established greats did. I think about it this way: If The reset button were to be hit right now on the what tools and packages people used in Python, what do I wish they did?
5. **Customizability** -- I love customizing my tools and opt for tools where I can do a lot of customization and fiddling.
6. **Small Teams / Individual** -- As someone who personally tends to work by myself or with a few people on research projects, I gear this template towards iterating quickly and with high quality. If a tool requires such deep knowledge that someone has to spend a day researching it just to use, I don't want it.
7. **Scalable** -- As noted above, this is mainly geared to individuals and small teams. However, in the case you want to scale production or team size or even if you move to a new and larger organization, I want those skills to transfer and for there to be little more to learn and so that you don't have to learn an entirely new skillset or library. -->


This template is primarily a research and learning project that explores modern Python development tools and practices. Rather than focusing solely on practical, production-ready solutions, it represents an aspirational view of Python development that emphasizes cutting-edge tools and emerging best practices.

### Core Principles 🎯

1. **Reset-Button Development** 🔄
   - Reimagines Python tooling without legacy constraints
   - Selects tools leveraging decades of lessons from established tools while avoiding their compromises

2. **Research-Driven Exploration** 🔬
   - Functions as a living laboratory for modern Python development
   - No default goes unscruitinized, with curated promising technologies based on careful comparative analysis

3. **Individual and Small Team Focus with Scalability** 👥
   - Optimized for personal projects and small research teams
   - Maintains professional standards that scale to larger organizations
   - Prioritizes tools that don't require deep expertise to start using and are helpful at any scale.

4. **Aspirational Over Practical** 🌟
   - Embraces perfectionist ideals in tooling choices
   - Values learning opportunities over conventional solutions
   - Willing to trade immediate familiarity for better long-term solutions

5. **Thoughtfully Opinionated** 🤔
   - Provides carefully selected defaults based on extensive research
   - Maintains modularity and avoids vendor lock-in
   - Prefers simple, non-intrusive APIs over heavyweight frameworks
   - Examples: Loguru > logging, Polars > Pandas, UV > pip, FastAPI > Flask

6. **Quality Driven** ✨
   - Emphasizes clean, maintainable code
   - Incorporates professional-grade tooling and practices
   - Focuses on developer experience without sacrificing robustness

7. **Sexy**
    - Just because coding is work doesn't mean it can't be fun. Sometimes you need those `pretty colors` and fancy ~graphs~ if you want that ADHD brain of yours pumped full of happy juice. I want my code to be like the notes of your overachieving classmate with a bullet journal.

> ⚠️ Note: This template intentionally prioritizes exploration and learning over immediate practicality. While all included tools have been carefully researched, not all have been extensively tested in production environments. Users should view this as a forward-looking reference implementation rather than a production-ready solution.


## Contributing

If you plan major changes, consider upstreaming them to [CookieCutter Data Science (CCDS)](https://github.com/drivendataorg/cookiecutter-data-science). For minor fixes or adjustments to GOTem, submit an issue or pull request here. See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details.