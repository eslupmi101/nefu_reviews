from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.users import get_all_review_texts
from app.database.models.user import UserModel
from app.keyboards.reply.menu import MAIN_MENU_KB
from .states.menu import MainMenuStates
from .states.review import ReviewStates


router = Router(name='Основное меню')


@router.message(MainMenuStates.main_level, F.text == 'Оставить обращение')
async def to_create_review_handler(message: types.Message, state: FSMContext):
    # Имитация имени из базы данных
    await message.answer('Введите текст обращения')
    await state.set_state(ReviewStates.create_review)


@router.message(MainMenuStates.main_level, F.text == 'Все обращения')
async def all_reviews(message: types.Message, state: FSMContext, session: AsyncSession):
    review_texts = await get_all_review_texts(session)
    await message.answer(
        '\n'.join(review_texts),
        reply_markup=MAIN_MENU_KB
    )


@router.message(MainMenuStates.main_level, F.text == 'Мой профиль')
async def user_profile_handler(message: types.Message, state: FSMContext, user: UserModel):
    await message.answer(
        str(str(user.id) + ' ' + user.full_name),
        reply_markup=MAIN_MENU_KB
    )
