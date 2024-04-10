from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from sqlalchemy.ext.asyncio import AsyncSession

from app.keyboards.reply.menu import MAIN_MENU_KB
from app.services.users import add_user, user_exists
from .states.menu import MainMenuStates
from .states.registration import RegistrationStates

router = Router(name='регистрация')


@router.message(CommandStart())
async def start_command_handler(message: types.Message, state: FSMContext, session: AsyncSession):
    user = message.from_user
    if not await user_exists(session, user.id):
        await message.answer(f'Привет! {user.username}')
        await message.answer('Напишите свое ФИО')
        await state.set_state(RegistrationStates.wait_full_name)
        return

    await state.set_state(MainMenuStates.main_level)


@router.message(RegistrationStates.wait_full_name)
async def wait_full_name_handler(message: types.Message, state: FSMContext, session: AsyncSession):
    # Получение возраста из текстового сообщения
    full_name = str(message.text)

    if not full_name:
        await message.reply('Введите ФИО')
        return

    user = message.from_user

    await add_user(
        session,
        user,
        full_name
    )

    # Переключение состояния
    await state.set_state(MainMenuStates.main_level)
    await message.answer(
        f'Спасибо, за регистрацию {full_name}. Теперь вы можете оставить свое обращение.',
        reply_markup=MAIN_MENU_KB
    )
