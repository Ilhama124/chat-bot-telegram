from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# Функция для создания основного меню
def main_menu():
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton(text="Начать", callback_data="start"),
        InlineKeyboardButton(text="Помощь", callback_data="help"),
        InlineKeyboardButton(text="Текущее время", callback_data="time"),
        InlineKeyboardButton(text="Эхо", callback_data="echo"),
    )
    return markup
