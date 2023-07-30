<!--
SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Contributing

Welcome to Template-Sandbox's contributor's guide.

> Note: This is a currently a work-in-progress document!

The goal of this guide is to help any potential contributor to understand the fundamentals of the project and how to [contribute in different ways].

This document focuses on getting any potential contributor familiarized
with the development processes, but [other kinds of contributions] are also
appreciated.

This project adopts [Contributor Covenant's Code of Conduct].

We use [REUSE] to manage licenses with the following general rules:
- Source code of the main project is license under [Apache-2.0].
- Documentation is licensed under [CC-BY-4.0].
- Configuration and less important files are licensed under [CC0-1.0].

Releases are numbered using [Semantic Versioning] and the [changelog is kept using towncrier].

## For First-Timers in Open Source Contribution

If you are new to open source contributions, we highly recommend that you familiarise yourself with [git] and have a look at resources such as [contribution-guide.org] and this [guide created by FreeCodeCamp] [^contrib1].

## Issue Reports

Before reporting an issue, check if it is not already in the [issue tracker] (check also the closed ones).
If there is not, please open a new issue.

Issues should contain enough information to assess the scope of the problem and allow reproducibility.
Hence, please include all the relevant information such as operating system, Python version, and a minimal example with the steps that trigger the problem.

## Documentation Improvements

We eagerly accept help to improve the project's documentation.

The documentation is written in CommonMark with MyST extensions using [Sphinx] as compiler.

When working on documentation changes in your local machine, you can
compile them using [nox]:

```
nox -e docs
```

and use Python's built-in web server for a preview in your web browser
(`http://localhost:8000`):

```
python3 -m http.server --directory 'docs/_build/html'
```

## Code Contributions

We use a combination of [github's fork and pull request workflow] and [Digital Ocean's rebase workflow].

### Submit an issue

Before you work on any non-trivial code contribution it's best to first create
a report in the [issue tracker] to start a discussion on the subject.
This often provides additional considerations and avoids unnecessary work.

### Fork the project

### Setup the environment

1. Create the isolated python environment with [conda] or [mamba]:
```
mamba create --name <environment name> --file conda-linux-64.lock
```
2. Install all dependencies (including development ones):
```
poetry install --all-extras
```
3. Prepare the pre-commit hooks:
```
pre-commit install
```

### Working in your contribution

- Make sure to add relevant tests and that existing tests are passing (updating them if required).
- Document your code with docstrings.
- Use the `nox` session `lint` to check and format your code.
- The pre-commit hooks should take care of the formatting, but you can also run [black] and [ruff] manually with `nox -e reformat`.
- Create small commits with [descriptive commit messages].

### Submit your contribution

1. Once you finished your contribution, create a [news fragment with towncrier]

2. If everything works fine, push your local branch to Github with:

   ```
   git push -u origin my-feature
   ```
3. Make sure that at least the `nox` default sessions run without errors with:
```
nox -e
```

4. Create a pull request and mark it as draft if it contains non-trivial contributions and decisions that need to be discussed, marking it as ready for review.

## Maintainer tasks

### Releases

The following steps can be used to release a new version for
Template-Sandbox on [PyPI]:

1. Make sure all nox sessions are successful (especially tests) with TODO `nox -t rc`.
2. Compile the changelog with `towncrier build` and make the necessary amends.
3. Tag the current commit on the main branch with a release tag, e.g., `v1.2.3`.
4. Push the new tag to the upstream [repository], e.g., `git push upstream v1.2.3`.
5. The CI/CD should automatically publish the project to [TestPyPI] or [PyPI], and the documentation to [Read The Docs], if enabled.

[^contrib1]: Even though, these resources focus on open source projects and
    communities, the general ideas behind collaborating with other developers
    to collectively create software are general and can be applied to all sorts
    of environments, including private companies and proprietary code bases.

[Apache-2.0]: https://opensource.org/license/apache-2-0/
[black]: https://black.readthedocs.io/
[CC-BY-4.0]: https://creativecommons.org/licenses/by/4.0/
[CC0-1.0]: https://creativecommons.org/publicdomain/zero/1.0/
[changelog is kept using towncrier]: https://towncrier.readthedocs.io/en/stable/markdown.html
[commonmark]: https://commonmark.org/
[conda]: https://docs.conda.io/en/latest/miniconda.html
[contribute in different ways]: https://opensource.guide/how-to-contribute
[contribution-guide.org]: https://www.contribution-guide.org
[Contributor Covenant's Code of Conduct]: https://www.contributor-covenant.org/
[creating a pr]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
[descriptive commit messages]: https://chris.beams.io/posts/git-commit
[Digital Ocean's rebase workflow]: https://www.digitalocean.com/community/tutorials/how-to-rebase-and-update-a-pull-request
[docstrings]: https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html
[first-contributions tutorial]: https://github.com/firstcontributions/first-contributions
[git]: https://git-scm.com
[github's fork and pull request workflow]: https://guides.github.com/activities/forking/
[guide created by freecodecamp]: https://github.com/FreeCodeCamp/how-to-contribute-to-open-source
[issue tracker]: https://github.com/<USERNAME>/template-sandbox/issues
[mamba]: https://mamba.readthedocs.io/en/latest/
[myst]: https://myst-parser.readthedocs.io/en/latest/syntax/syntax.html
[nox]: https://nox.thea.codes/en/stable/
[news fragment with towncrier]: https://towncrier.readthedocs.io/en/stable/markdown.html
[pre-commit]: https://pre-commit.com/
[pypi]: https://pypi.org/
[repository]: https://github.com/<USERNAME>/template-sandbox
[Read the Docs]: https://readthedocs.org/
[REUSE]: https://reuse.software/
[ruff]: https://beta.ruff.rs/
[Semantic Versioning]: https://semver.org/
[sphinx]: https://www.sphinx-doc.org/en/master/
[TestPyPI]: https://test.pypi.org/
