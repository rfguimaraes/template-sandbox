# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

"""Placeholder test for the main placeholder."""

import pytest
from template_sandbox import greeter, __version__


def test_main_greeter_correct_greeting(capsys: pytest.CaptureFixture[str]) -> None:
    """
    Test main greeter function.

    Test that the greeting is 'Hello, World!', followed by the module version
    between parentheses.
    """
    greeter.main()
    captured = capsys.readouterr()
    assert captured.out == f"Hello, World! ({__version__})\n"
    assert not captured.err
