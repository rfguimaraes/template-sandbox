# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

"""Definition of nox sessions (tasks)."""

import tempfile

import nox  # pylint: disable=import-error
from poetry.factory import Factory  # pylint: disable=import-error

PACKAGE_NAME = "template_sandbox"


def _install_on_nox_from_poetry_lock(
    session: nox.Session,
    poetry_args: tuple,
    *args: str,
    **kwargs: str,
) -> None:
    with tempfile.NamedTemporaryFile() as constraints:
        session.run(
            "poetry",
            "export",
            *poetry_args,
            "--format=constraints.txt",
            "--without-hashes",
            f"--output={constraints.name}",
            external=True,
        )
        session.install(f"--constraint={constraints.name}", *args, **kwargs)


locations = "src", "tests", "noxfile.py", "docs/conf.py"
nox.options.sessions = "lint", "safety", "tests", "mypy"


@nox.session(python=["3.9", "3.10", "3.11"], tags=["rc"])
def tests(session: nox.Session) -> None:
    """Run tests."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pytest", *args)
    runner_tokens = ["pytest", "-x", "--assert=plain", *args]
    runner_args = [f"'{s}'" if " " in s else s for s in runner_tokens]
    runner_config = " ".join(runner_args)
    session.run("mutmut", "run", "--runner", runner_config)


@nox.session(python=["3.9", "3.10", "3.11"])
def mutmut(session: nox.Session) -> None:
    """Run mutation tests."""
    args = session.posargs
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("mutmut", "run", *args)


@nox.session(python=["3.9", "3.10", "3.11"], tags=["rc"])
def typeguard(session: nox.Session) -> None:
    """Run tests with additional typecheck."""
    args = session.posargs or ["-m", "not e2e"]
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    dependencies.extend(config.package.dependency_group("type").dependencies)
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "test,type"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pytest", f"--typeguard-packages={PACKAGE_NAME}", *args)


@nox.session(python=["3.9", "3.10", "3.11"], tags=["rc"])
def xdoctest(session: nox.Session) -> None:
    """Test examples in documentation with xdoctest."""
    args = session.posargs or ["all"]
    _install_on_nox_from_poetry_lock(session, ("--with", "docs"), "xdoctest")
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("python", "-m", "xdoctest", PACKAGE_NAME, *args)


@nox.session(python=["3.9", "3.10", "3.11"], tags=["rc"])
def lint(session: nox.Session) -> None:
    """Lint check with ruff and pylint."""
    args = session.posargs or locations
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("lint").dependencies
    dependencies.extend(config.package.dependency_group("test").dependencies)
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "lint,test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pylint", *args)
    session.run("ruff", "check", *args)


@nox.session(python=["3.11"], tags=["rc"])
def reformat(session: nox.Session) -> None:
    """Fix with ruff and format with black."""
    args = session.posargs or locations
    _install_on_nox_from_poetry_lock(session, ("--only", "lint"), "black", "ruff")
    session.run("ruff", "--fix", *args)
    session.run("black", *args)


@nox.session(python=["3.11"], tags=["rc"])
def safety(session: nox.Session) -> None:
    """Safety check with public repository."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with=dev,lint,test",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        _install_on_nox_from_poetry_lock(session, ("--only", "lint"), "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3.9", "3.10", "3.11"], tags=["rc"])
def mypy(session: nox.Session) -> None:
    """Type check with mypy."""
    args = session.posargs or locations
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    dependencies.extend(config.package.dependency_group("type").dependencies)
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "type,test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("mypy", *args)


@nox.session(python=["3.11"], tags=["rc"])
def docs(session: nox.Session) -> None:
    """Build the documentation using Sphinx."""
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("docs").dependencies
    names = [x.name for x in dependencies]
    _install_on_nox_from_poetry_lock(session, ("--with", "docs"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("towncrier", "--yes", "--draft")
    session.run("sphinx-build", "docs", "docs/_build")
