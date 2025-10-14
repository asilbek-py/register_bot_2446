import asyncio
import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import API_TOKEN
from states import RegistrationState
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.filters.state import StateFilter
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Salom, {message.from_user.full_name}! 😊\nRo'yhatdan o'tish uchun /register buyrug'ini bering.")


@dp.message(Command('register'))
async def register_handler(message: Message, state: FSMContext):
    await message.answer("Registratsiyaga xush kelibsiz! Ismingizni kiriting:")
    await state.set_state(RegistrationState.ism)


@dp.message(StateFilter(RegistrationState.ism))
async def ism_handler(message: Message, state: FSMContext):
    await message.answer("Ismingiz qabul qilindi! Familiyangizni kiriting:")
    await state.update_data(ism=message.text)
    await state.set_state(RegistrationState.familiya)
    
@dp.message(StateFilter(RegistrationState.familiya))
async def familiya_handler(message: Message, state: FSMContext):
    await message.answer("Familiyagiz qabul qilindi! yoshingizni kiriting:")
    await state.update_data(familiya=message.text)
    await state.set_state(RegistrationState.yosh)


telefon_button = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📞 Telefon raqam jo'natish", request_contact=True)]
], resize_keyboard=True)

@dp.message(StateFilter(RegistrationState.yosh))
async def yosh_handler(message: Message, state: FSMContext):
    await message.answer("Yoshingiz qabul qilindi! telefon raqam jo'nating:", reply_markup=telefon_button)
    await state.update_data(yosh=message.text)
    await state.set_state(RegistrationState.telefon_raqam)


@dp.message(StateFilter(RegistrationState.telefon_raqam))
async def telefon_raqam_handler(message: Message, state: FSMContext):
    await message.answer("Telefon raqam qabul qilindi! telefon raqam jo'nating:", reply_markup=ReplyKeyboardRemove())
    await state.update_data(telefon_raqam=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(text=f'{data}')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
