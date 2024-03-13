# common.py
from aiogram import types, Router
from aiogram.filters import Command

common_router = Router()


@common_router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я твой бот. Введи /help, чтобы узнать список доступных команд."
    )


@common_router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Список команд: /start - начать работу с ботом, /help - отобразить помощь."
    )
