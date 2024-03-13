from aiogram import types
import datetime
from aiogram import types


# Этот файл предназначен для обработчиков пользовательских команд
# Пример функции обработки пользовательской команды /custom
async def handle_custom_command(message: types.Message):
    await message.reply("This is a custom command.")


# Этот обработчик будет повторять сообщение пользователя
async def echo_message(message: types.Message):
    await message.answer(message.text)


# Этот обработчик будет отправлять текущее время пользователю
async def send_current_time(message: types.Message):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await message.answer(f"Текущее время: {current_time}")
