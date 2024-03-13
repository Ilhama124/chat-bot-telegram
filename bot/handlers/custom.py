# custom.py
from aiogram import types, Router
from aiogram.filters import Command
from aiogram.filters import CommandStart
from aiogram.filters.command import CommandObject
import datetime

custom_router = Router()


@custom_router.message(CommandStart())
async def send_menu(message: types.Message):
    from utils.markup import (
        main_menu,
    )  # Правильное место для импорта если он вызывается внутри функции

    await message.answer("Выберите опцию из меню ниже:", reply_markup=main_menu())


@custom_router.message(Command("custom"))
async def handle_custom_command(message: types.Message):
    await message.answer("Это пользовательская команда.")


@custom_router.callback_query(lambda c: c.data == "start")
async def on_start_click(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Привет! Это стартовая команда.")
    await callback_query.answer()


@custom_router.callback_query(lambda c: c.data == "help")
async def on_help_click(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Это помощь команда.")
    await callback_query.answer()


@custom_router.callback_query(lambda c: c.data == "time")
async def on_time_click(callback_query: types.CallbackQuery):
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    await callback_query.message.answer(f"Текущее время: {current_time}")
    await callback_query.answer()


@custom_router.callback_query(lambda c: c.data == "echo")
async def on_echo_click(callback_query: types.CallbackQuery):
    await callback_query.message.answer("Это эхо команда.")
    await callback_query.answer()
