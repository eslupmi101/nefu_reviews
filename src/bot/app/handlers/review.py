from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.user import UserModel
from app.keyboards.reply.menu import MAIN_MENU_KB
from app.services.users import add_review
from .states.menu import MainMenuStates
from .states.review import ReviewStates

router = Router(name='обращения')


@router.message(ReviewStates.create_review)
async def start_command_handler(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
    user: UserModel
):
    review = message.text

    if not review:
        await message.reply('Введите текст обращения')
        return

    await add_review(
        session,
        user,
        review
    )
    await state.set_state(MainMenuStates.main_level)
    await message.answer(
        'Спасибо, за обращение!',
        reply_markup=MAIN_MENU_KB
    )
