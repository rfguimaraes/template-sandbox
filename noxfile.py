# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

import tempfile
import nox


locations = "src", "tests", "noxfile.py"
nox.options.sessions = "lint", "safety" "tests"


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


@nox.session(python="3.9")
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
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")
