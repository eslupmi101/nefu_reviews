from aiogram import types

MAIN_MENU_KB = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Создать обращение'),
            types.KeyboardButton(text='Все обращения'),
            types.KeyboardButton(text='Мой профиль'),
        ]
    ],
    resize_keyboard=True
)
