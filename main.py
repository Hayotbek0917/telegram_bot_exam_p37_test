import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
from models import User

dp = Dispatcher(storage=MemoryStorage())


class RegisterForm(StatesGroup):
    name = State()
    birth_year = State()
    phone = State()


class SearchForm(StatesGroup):
    query = State()


def contact_btn():
    return ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="Telefon yuborish", request_contact=True)]],
        resize_keyboard=True
    )


@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    user = User.get_by_telegram_id(message.from_user.id)
    if user:
        await message.answer("Xush kelbsz brooooo bizning botga, 👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋👋")
    else:
        await message.answer("Ismingizni kiriting brooooooooooooo ---->:")
        await state.set_state(RegisterForm.name)


@dp.message(RegisterForm.name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Tugilgan yilingizni kiriting broooooo ------> :")
    await state.set_state(RegisterForm.birth_year)


@dp.message(RegisterForm.birth_year)
async def get_year(message: Message, state: FSMContext):
    await state.update_data(birth_year=message.text)
    await message.answer("Telefonni yuboring:", reply_markup=contact_btn())
    await state.set_state(RegisterForm.phone)


@dp.message(RegisterForm.phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    data = await state.get_data()
    User.create(
        telegram_id=message.from_user.id,
        name=data["name"],
        birth_year=data["birth_year"],
        phone=message.contact.phone_number
    )
    await state.clear()
    await message.answer("Royxatdan o‘tdingiz broooooooo tabrikliman ✅✅✅✅✅✅✅✅✅✅")


@dp.message(Command("search"))
async def search_start(message: Message, state: FSMContext):
    await message.answer(
        "Ism yoki telefon kiritsangiz men ozim sizga chotki qlb topb beraman, bir xursand boln brooooooo ----> ")
    await state.set_state(SearchForm.query)


@dp.message(SearchForm.query)
async def search_handler(message: Message, state: FSMContext):
    query = message.text.lower()

    users = User.get_all()
    natija = []

    for user in users:
        if query in user.name.lower() or query in user.phone:     #qaysiligini blmay qoldim and yokida or shunga yozb qoydim   if query in user.name.lower() and query in user.phone: qaysiligini blmay qoldim and yokida or shunga yozb qoydim
            natija.append(user)

    if not natija:
        await message.answer("Topilmadi bro ❌❌❌❌❌❌❌❌❌❌❌❌❌")
    else:
        text = "Topilganlar:\n\n"
        for user in natija:
            text += f"Ism: {user.name}\n"
            text += f"Tug‘ilgan yil: {user.birth_year}\n"
            text += f"Telefon: {user.phone}\n\n"
        await message.answer(text)
    await state.clear()


async def main():
    bot = Bot(
        settings.TELEGRAM_BOT_TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())







