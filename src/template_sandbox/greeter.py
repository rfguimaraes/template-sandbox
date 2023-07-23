# SPDX-FileCopyrightText: 2023 The Template-Sandbox Authors
#
# SPDX-License-Identifier: Apache-2.0

"""Placeholder file with a 'hello world'."""

import structlog_sentry_logger as stlg

from . import __version__

LOGGER = stlg.get_logger()


def main() -> None:
    """Print the greeting message and version number."""
    print(f"Hello, World! ({__version__})")


def message_to_shout(message: str) -> str:
    """
    Greet a person by name.

    :param message: The message to convert to "shout"
    :type message: str
    :return: The shout-formatted message if the string is not empty,
        empty string otherwise
    :rtype: str
    """
    if not message:
        LOGGER.info("Empty or invalid message received")
        return ""
    new_message = message.upper()
    if new_message[-1] != "!":
        new_message = new_message + "!"
    return new_message
