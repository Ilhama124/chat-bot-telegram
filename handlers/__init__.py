from .common import cmd_start, cmd_help
from .custom import handle_custom_command
from .common import cmd_start, cmd_help
from .custom import handle_custom_command, echo_message, send_current_time


def register_handlers_common(dp):
    dp.register_message_handler(cmd_start, commands=["start", "help"])
    dp.register_message_handler(cmd_help, commands=["help"])


def register_handlers_custom(dp):
    dp.register_message_handler(handle_custom_command, commands=["custom"])


def register_handlers_common(dp):
    dp.register_message_handler(cmd_start, commands=["start", "help"])
    dp.register_message_handler(cmd_help, commands=["help"])


def register_handlers_custom(dp):
    dp.register_message_handler(handle_custom_command, commands=["custom"])
    dp.register_message_handler(
        echo_message, lambda message: message.text and not message.text.startswith("/")
    )
    dp.register_message_handler(send_current_time, commands=["time"])
