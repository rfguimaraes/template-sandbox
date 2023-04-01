# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

from template_sandbox import greeter, __version__


def test_main_greeter_correct_greeting(capsys):
    greeter.main()
    captured = capsys.readouterr()
    assert captured.out == f"Hello, World! ({__version__})\n"
    assert captured.err == ""
