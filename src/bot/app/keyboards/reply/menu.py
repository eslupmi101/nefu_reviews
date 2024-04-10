from aiogram import types

MAIN_MENU_KB = types.ReplyKeyboardMarkup(
    keyboard=[
        [types.KeyboardButton(text='Оставить обращение')],
        [types.KeyboardButton(text='Все обращения')],
        [types.KeyboardButton(text='Мой профиль')],
    ]
)
