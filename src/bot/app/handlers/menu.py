from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.user import UserModel
from app.core.config import settings
from app.keyboards.reply.menu import MAIN_MENU_KB
from app.keyboards.reply.review import REVIEW_KB
from .states.menu import MainMenuStates
from .states.review import ReviewStates


router = Router(name='Основное меню')


@router.message(MainMenuStates.main_level, F.text == 'Создать обращение')
async def to_create_review_handler(
    message: types.Message,
    state: FSMContext
):
    # Имитация имени из базы данных
    text = (
        'Введите текст обращения. \n'
        'Так же вы можете отправить до 5 фотографий.'
    )
    await message.answer(
        text,
        reply_markup=REVIEW_KB
    )
    await state.set_state(ReviewStates.create_review)


@router.message(MainMenuStates.main_level, F.text == 'Все обращения')
async def all_reviews(message: types.Message, state: FSMContext, session: AsyncSession):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[[
            InlineKeyboardButton(
                text='Обращения',
                url=f'{settings.REVIEWS_HUB_URL}/?telegram_id={message.from_user.id}'
            )
        ]]
    )
    await message.answer(
        'Просмотр всех обращений',
        reply_markup=keyboard
    )


@router.message(MainMenuStates.main_level, F.text == 'Мой профиль')
async def user_profile_handler(message: types.Message, state: FSMContext, user: UserModel):
    await message.answer(
        str(str(user.id) + ' ' + user.full_name),
        reply_markup=MAIN_MENU_KB
    )
