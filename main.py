# main.py
import asyncio
import logging

from aiogram import Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters.command import Command
from aiogram import Dispatcher


import config

from bot.handlers.common import common_router
from bot.handlers.custom import custom_router
from bot.utils.markup import main_menu

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=config.BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    # Включаем роутеры в диспетчер
    dp.include_router(common_router)
    dp.include_router(custom_router)

    # Удаляем вебхук, если он есть, и начинаем опрос бота
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
