from aiogram import Router, types, Dispatcher
from aiogram.types import Message
from utils.markup import main_menu
from aiogram.filters import Command
from handlers.common import cmd_start, cmd_help, cmd_time
from handlers.custom import cmd_echo


router = Router()


@router.message(commands=["menu"])
async def show_menu(message: types.Message):
    await message.answer("Выберите команду из меню:", reply_markup=main_menu())

@router.callback_query(text="start")
async def on_start_clicked(call: types.CallbackQuery):
    await cmd_start(call.message)

@router.callback_query(text="help")
async def on_help_clicked(call: types.CallbackQuery):
    await cmd_help(call.message)

@router.callback_query(text="time")
async def on_time_clicked(call: types.CallbackQuery):
    await cmd_time(call.message)

@router.callback_query(text="echo")
async def on_echo_clicked(call: types.CallbackQuery):
    await cmd_echo(call.message)