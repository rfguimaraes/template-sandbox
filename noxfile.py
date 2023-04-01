# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

import nox


locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "tests"


@nox.session(python=["3.9"])
def tests(session):
    args = session.posargs or ["--cov"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.9"])
def lint(session):
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("ruff", "check", *args)


@nox.session(python=["3.9"])
def black(session):
    args = session.posargs or locations
    session.run("poetry", "install", external=True)
    session.run("black", *args)
