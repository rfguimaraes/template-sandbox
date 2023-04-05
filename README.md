<!--
SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Template-Sandbox

This project is a simple template that I am building for my own python projects.
The setup and plan are based mostly on these pieces of writing:

- [Hypermodern Python by Claudio Jolowicz](https://cjolowicz.github.io/posts/hypermodern-python-01-setup)
- [This answer by michau on StackOverflow](https://stackoverflow.com/a/71110028)
- [An opinionated guide to Python environments in 2021 by James Ravenscroft](https://brainsteam.co.uk/2021/04/01/opinionated-guide-to-virtualenvs/)

I am creating setup that suited my needs and preferences, while allowing me to learn the tools involved.
That is why, if you read the references above, you will notice that some significant decisions are different, while the fundamental idea remains.

In the (near?) future I will convert this template-sandbox into a proper cookicutter/cookieninja template.

## Components

### Information Files

- [x] AUTHORS.md
- [x] CHANGELOG.md
- [ ] CONTRIBUTING.md
- [x] README.md

### Environemnt and CUDA dependencies

- [x] Conda
- [x] Mamba

### Dependency management

- [x] Poetry

### Hooks

- [x] pre-commit
- [x] pre-commit-hooks

### License management

- [x] REUSE
- [x] REUSE pre-commit hook

### Testing

- [x] pytest
- [x] Coverage.py
- [x] pytest-cov
- [x] nox
- [x] pytest-mock

### Lint

- [x] ruff (keep this in mind: [ruff #2459](https://github.com/charliermarsh/ruff/issues/2459))
- [x] ruff pre-commit hook
- [x] black
- [x] black pre-commit hook
- [x] safety

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

## CI/CD

- [x] Trufflehog (Consider removing as pre-commit hook due to time)
- [x] Woodpecker CI/CD setup (local) + Localtunnel script
- [x] Build recipe
- [ ] TestPyPI
- [ ] ReadTheDocs
