from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class RegistrationState(StatesGroup):
    ism = State()
    familiya = State()
    yosh = State()
    telefon_raqam = State()
    login = State()
    parol = State()
    tasdiqlash = State()