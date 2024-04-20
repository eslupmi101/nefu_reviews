from aiogram import F, Router, types
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession
# from loguru import Logger

from app.database.models.user import UserModel
from app.keyboards.reply.menu import MAIN_MENU_KB
from app.keyboards.reply.review import REVIEW_KB
from app.services.users import add_review
from .states.menu import MainMenuStates
from .states.review import ReviewStates

router = Router(name='обращения')


@router.message(ReviewStates.create_review, F.text | F.photo | F.text != 'Отправить обращение')
async def creating_review_handler(
    message: types.Message,
    state: FSMContext
):
    data = await state.get_data()

    review_text = str()
    if data.get('review_text', None):
        review_text += '\n' + message.text
    else:
        review_text = message.text

    await state.update_data(
        {
            'review_text': review_text,
        }
    )
    """
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
    """
    await message.answer(
        'Текст добавлен в обращение',
        reply_markup=REVIEW_KB
    )


@router.message(ReviewStates.create_review, F.text == 'Отправить обращение')
async def save_review_handler(
    message: types.Message,
    state: FSMContext,
    session: AsyncSession,
    user: UserModel
):
    data = await state.get_data()
    if not data.get('review_text', None):
        await message.answer(
            'Введите текст обращения',
            reply_markup=REVIEW_KB
        )
        return
    try:
        await add_review(
            session,
            user,
            data['review_text'],
        )

        await message.answer(
            'Ваше обращение успешно отправлено! Спасибо 😊',
            reply_markup=MAIN_MENU_KB
        )
    except Exception as e:
        print(str(e))
        # Logger.error('Error saving review %s', e)
        await message.answer(
            'Произошла ошибка отправки обращения',
            reply_markup=MAIN_MENU_KB
        )
    # Delete review_text from state
    await state.update_data(
        {
            'review_text': None,
        }
    )
    await state.set_state(MainMenuStates.main_level)
