from aiogram import types

REVIEW_KB = types.ReplyKeyboardMarkup(
    keyboard=[
        [
            types.KeyboardButton(text='Отправить обращение'),
        ]
    ],
    resize_keyboard=True
)
