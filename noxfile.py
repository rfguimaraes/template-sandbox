# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

"""Definition of nox sessions (tasks)."""

import tempfile
import nox
from poetry.factory import Factory


package = "template_sandbox"


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


locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "safety", "tests", "type"


@nox.session(python=["3.9"])
def tests(session: nox.Session) -> None:
    """Run tests."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    names = [x.name for x in dependencies if str(x.name) != "nox"]
    _install_on_nox_from_poetry_lock(session, ("--with", "test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.9"])
def typeguard(session: nox.Session) -> None:
    """Run tests with additional typecheck."""
    args = session.posargs or ["-m", "not e2e"]
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    dependencies.extend(config.package.dependency_group("type").dependencies)
    names = [x.name for x in dependencies if str(x.name) != "nox"]
    _install_on_nox_from_poetry_lock(session, ("--with", "test,type"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pytest", f"--typeguard-packages={package}", *args)


@nox.session(python=["3.9"])
def lint(session: nox.Session) -> None:
    """Lint check with ruff."""
    args = session.posargs or locations
    _install_on_nox_from_poetry_lock(session, ("--only", "lint"), "ruff")
    session.run("ruff", "check", *args)


@nox.session(python=["3.9"])
def black(session: nox.Session) -> None:
    """Format with black."""
    args = session.posargs or locations
    _install_on_nox_from_poetry_lock(session, ("--only", "lint"), "black")
    session.run("black", *args)


@nox.session(python=["3.9"])
def safety(session: nox.Session) -> None:
    """Safety check with public repository."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--with=dev,lint,tests",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        _install_on_nox_from_poetry_lock(session, ("--only", "lint"), "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3.9"])
def mypy(session: nox.Session) -> None:
    """Type check with mypy."""
    args = session.posargs or locations
    # Workaround the need of poetry inside the nox session.
    # It is easier to skip this file from mypy check.
    _install_on_nox_from_poetry_lock(session, ("--with", "type"), "mypy")
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("mypy", *args)
