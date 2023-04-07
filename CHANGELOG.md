<!--
SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors

SPDX-License-Identifier: CC-BY-4.0
-->

# Changelog

All notable changes to Template-Sandbox will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

This project uses [*towncrier*](https://towncrier.readthedocs.io/) and the changes for the upcoming release can be found in <https://github.com/twisted/my-project/tree/main/changelog.d/>.

<!-- towncrier release notes start -->

## [0.1.0a3](https://github.com/rfguimaraes/template-sandbox/tree/v0.1.0a3) - 2023-04-07



### Added

- Feat: add debug-statements, check-added-large-files, and check-ast pre-commit hooks [#1](https://github.com/template-sandbox/issues/1)
- Added pylint to lint session (nox) and pre-commit hook [#7](https://github.com/template-sandbox/issues/7)
- Feat: programmatically determine package version from pyproject.toml
- Use towncrier to manage the changelog


### Fixed

- Fixed project links in the changelog template [#8](https://github.com/template-sandbox/issues/8)
