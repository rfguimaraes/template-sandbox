# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

"""Placeholder test for the main placeholder."""

import pytest
from hypothesis import example, given
from hypothesis.strategies import text
from pytest_mock import MockerFixture
from template_sandbox import __version__, greeter


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


@given(text())
@example("")
def test_shout_ensures_exclamation_mark(message: str) -> None:
    """
    Test the conversion of a message to shout-like string.

    Test that the message has an exclamation mark at the end unless it is empty.

    :param message: the message to be converted
    :type message: the message to be converted
    :returns: None
    """
    shout = greeter.message_to_shout(message)
    assert not shout or shout[-1] == "!"


def test_empty_message_empty_shout() -> None:
    """
    Test the shout conversion of an empty string is an empty string.

    :returns: None
    """
    shout = greeter.message_to_shout("")
    assert not shout


@given(text())
@example("!")
def test_exclamation_ended_does_not_get_another(message: str) -> None:
    """
    Test the conversion of a message ended by '!' to shout-like string.

    Test that the message has an exclamation mark at the end unless it is empty.

    :param message: the message to be converted
    :type message: the message to be converted
    :returns: None
    """
    message = message + "!"
    shout = greeter.message_to_shout(message)
    assert shout.count("!") == message.count("!")
    assert shout[-1] == "!"


@given(text(min_size=1))
def test_non_empty_input_non_empty_output(message: str) -> None:
    """
    Test that the conversion of a non-empty message is non-empty.

    :param message: the message to be converted
    :type message: the message to be converted
    :returns: None
    """
    shout = greeter.message_to_shout(message)
    assert len(shout) > 0


def test_empty_message_log_info(mocker: MockerFixture) -> None:
    """
    Test log call when message is empty.

    Test that the logger is called with message "Hi" at debug level.
    """
    mock_info = mocker.patch.object(greeter.LOGGER, "info")
    greeter.message_to_shout("")
    mock_info.assert_called_once_with("Empty or invalid message received")
