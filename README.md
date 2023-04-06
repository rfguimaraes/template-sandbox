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
- [ ] Hypothesis
- [ ] MutMut

### Lint

- [x] ruff (keep this in mind: [ruff #2459](https://github.com/charliermarsh/ruff/issues/2459))
- [x] ruff pre-commit hook
- [x] black
- [x] black pre-commit hook
- [x] safety
- [ ] pylint (check speed to decide if it is worth as a pre-commit hook)
- [ ] hadolint
- [ ] ShellCheck
- [ ] shfmt
- [x] pre-commit-hooks
    - [x] end-of-file-fixer
    - [x] trailing-whitespace-fixer
    - [x] check-yaml
    - [ ] debug-statements
    - [ ] check-added-large-files
    - [ ] check-ast

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
- [ ] interrogate

### CI/CD

- [x] Trufflehog (Consider removing as pre-commit hook due to time, consider changing to detect-secrets due to license issues)
- [x] Woodpecker CI/CD setup (local) + Localtunnel script
- [x] Build recipe
- [ ] Renovate
- [ ] TestPyPI
- [ ] ReadTheDocs

### Logging

- [ ] structlog-sentry-logger
