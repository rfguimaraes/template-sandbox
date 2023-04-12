<!--
SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Template-Sandbox

This project is a simple template that I am building for my own python projects.
The setup and plan are based mostly on these pieces of writing and existing projects:

- [Hypermodern Python by Claudio Jolowicz](https://cjolowicz.github.io/posts/hypermodern-python-01-setup)
- [This answer by michau on StackOverflow](https://stackoverflow.com/a/71110028)
- [An opinionated guide to Python environments in 2021 by James Ravenscroft](https://brainsteam.co.uk/2021/04/01/opinionated-guide-to-virtualenvs/)
- [PyScaffold](pyscaffold.org/)
- [cookiecutter-cruft-poetry-tox-pre-commit-ci-cd](https://cookiecutter-cruft-poetry-tox-pre-commit-ci-cd.readthedocs.io/en/latest/#)


I am creating setup that suited my needs and preferences, while allowing me to learn the tools involved.
That is why, if you read the references above, you will notice that some significant decisions are different, while the fundamental idea remains.

In the (near?) future I will convert this template-sandbox into a proper cruft/cookicutter/cookieninja template.

In the meantime, when you **fork** the project, you can set it up using these steps:

1. `conda create --name <environment name> --file conda-linux-64.lock`
2. `poetry install --all-extras`
3. `pre-commit install`
4.  Get a URL with localtunnel: `./createtunnel.sh`
5. Setup an OAuth application for Woodpecker on Github.
6. Setup a personal token for Renovate
7. Create a TestPyPI account and token
8. Fill in the missing variables from `docker-compose.yml` in new file called `.env` in the project root.
9. Start the CI and Renovate with `docker compose up -d`
10. Log in into the Woodpecker container (e.g. if nothing was changed, by going to `localhost:8082`)
11. Enable the repository
12. Add the TestPyPI token as a secret named `test_pypi_token`
13. Check that the project can be built locally using `nox`

## Components

### Information Files

- [x] AUTHORS.md
- [x] CHANGELOG.md
- [ ] CONTRIBUTING.md
- [x] README.md

### Environment and CUDA dependencies

- [x] Conda
- [x] Mamba

### Dependency management

- [x] Poetry

### Hooks

- [x] pre-commit

### License management

- [x] REUSE
- [x] REUSE pre-commit hook

### Testing

- [x] pytest
- [x] Coverage.py
- [x] pytest-cov
- [x] nox
- [x] pytest-mock
- [x] Hypothesis
- [x] MutMut

### Lint

- [x] ruff (keep this in mind: [ruff #2459](https://github.com/charliermarsh/ruff/issues/2459))
- [x] ruff pre-commit hook
- [x] black
- [x] black pre-commit hook
- [x] safety
- [x] pylint
- [x] pre-commit-hooks
    - [x] end-of-file-fixer
    - [x] trailing-whitespace-fixer
    - [x] check-yaml
    - [x] debug-statements
    - [x] check-added-large-files
    - [x] check-ast

### Type checking

- [x] Mypy (Consider `dmypy` in the future)
- [x] Mypy pre-commit hook (Consider removing due to time consumed)
- [x] Typeguard

### Documentation

- [x] xdoctest
- [x] Sphinx
- [x] MyST ([the docstrings still need to use rST](https://myst-parser.readthedocs.io/en/v0.15.2_a/sphinx/use.html#use-sphinx-ext-autodoc-in-markdown-files))
- [x] autodoc
- [x] napoleon
- [x] sphinx-autodoc-typehints
- [x] towncrier

### CI/CD

- [x] Trufflehog (Consider removing as pre-commit hook due to time, consider changing to detect-secrets due to license issues)
- [x] Woodpecker CI/CD setup (local) + Localtunnel script
- [x] Build recipe
- [x] Renovate
- [x] TestPyPI
- [ ] PyPI (disabled by default)
- [ ] ReadTheDocs (disabled by default)

### Logging

- [ ] structlog-sentry-logger
