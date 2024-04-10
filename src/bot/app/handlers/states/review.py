from aiogram.fsm.state import State, StatesGroup


class ReviewStates(StatesGroup):
    create_review = State()
