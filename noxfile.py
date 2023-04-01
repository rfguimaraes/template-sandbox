# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

import tempfile
import nox
from poetry.factory import Factory


def install_on_nox_from_poetry_lock(session, poetry_args, *args, **kwargs):
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
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    config = Factory().create_poetry()
    dependencies = config.package.dependency_group("test").dependencies
    names = list(map(lambda x: x.name, dependencies))
    names.remove("nox")
    install_on_nox_from_poetry_lock(session, ("--with", "test"), *names)
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.9"])
def lint(session):
    args = session.posargs or locations
    install_on_nox_from_poetry_lock(session, ("--only", "lint"), "ruff")
    session.run("ruff", "check", *args)


@nox.session(python=["3.9"])
def black(session):
    args = session.posargs or locations
    install_on_nox_from_poetry_lock(session, ("--only", "lint"), "black")
    session.run("black", *args)


@nox.session(python=["3.9"])
def safety(session):
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
        install_on_nox_from_poetry_lock(session, ("--only", "lint"), "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=["3.9"])
def mypy(session):
    args = session.posargs or locations
    # Workaround the need of poetry inside the nox session.
    # It is easier to skip this file from mypy check.
    args = tuple([x for x in args if x != "noxfile.py"])
    install_on_nox_from_poetry_lock(session, ("--with", "type"), "mypy")
    session.run("poetry", "install", "--only", "main", external=True)
    session.run("mypy", *args)
