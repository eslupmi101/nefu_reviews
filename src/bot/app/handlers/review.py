from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.models.user import UserModel
from app.core.config import MEDIA_DIR
from app.keyboards.reply.menu import MAIN_MENU_KB
from app.services.users import add_review
from .states.menu import MainMenuStates
from .states.review import ReviewStates

router = Router(name='обращения')


@router.message(ReviewStates.create_review, F.text | F.photo)
async def create_review_handler(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
    user: UserModel
):
    text = message.text
    photos_names = []

    if message.photo:
        photos = message.photo[:5]
        for photo in photos:
            filename = f'{str(photo.file_unique_id)}.jpg'
            photos_names.append(filename)

            destination = f'{MEDIA_DIR}/{filename}'

            await message.bot.download(
                file=photo.file_id,
                destination=destination
            )

    await message.answer(
        'Ваше обращение успешно отправлено! Спасибо 😊',
        reply_markup=MAIN_MENU_KB
    )
    await state.set_state(MainMenuStates.main_level)

    await add_review(
        session,
        user,
        text,
        photos_names
    )
