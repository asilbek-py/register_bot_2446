from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class RegistrationState(StatesGroup):
    chat_id = State()
    ism = State()
    familiya = State()
    yosh = State()
    telefon_raqam = State()
    login = State()
    parol = State()
    all_data = State()
    tasdiqlash = State()