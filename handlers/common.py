from aiogram import types


# Функция обработки команды /start
async def cmd_start(message: types.Message):
    await message.reply(
        "Hi! I'm your bot. Enter /help to find out the list of available commands."
    )


# Функция обработки команды /help
async def cmd_help(message: types.Message):
    await message.reply(
        "The list of commands: /start - start working with the bot, /help - display help."
    )
