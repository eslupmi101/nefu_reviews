from aiogram.fsm.state import State, StatesGroup


class RegistrationStates(StatesGroup):
    wait_full_name = State()
