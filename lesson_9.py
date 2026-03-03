# import asyncio
#
# from aiogram import Bot, Dispatcher
# from aiogram.filters import Command, CommandStart
# from aiogram.types import Message, InputFile, FSInputFile
#
# TOKEN = '8359753576:AAHeVGWO71W5Pk2V77IfdbZY3Fs5_pKh8e0'
#
# dp = Dispatcher()
# # @p37_group_bot
# ADMIN_ID = 514411336
#
#
# @dp.message(CommandStart())
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     # text = f"{message.from_user.id}\nXabar: {message.text}"
#     # await bot.send_message(ADMIN_ID, text)
#     await bot.send_document(message.from_user.id, FSInputFile('main.py', 'darslik.py'))
#     await bot.send_document(message.from_user.id, "https://daryo.uz/image/960x540?url=https%3A%2F%2Fdata.daryo.uz%2Fmedia%2F2026%2F02%2F17%2F1771317135608463862_960X540%20UZ.jpg")
#     await bot.send_photo(message.from_user.id, "https://daryo.uz/image/960x540?url=https%3A%2F%2Fdata.daryo.uz%2Fmedia%2F2026%2F02%2F17%2F1771317135608463862_960X540%20UZ.jpg")
#     # await message.answer("Adminga yuborildi")
#
#
# @dp.message()
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     file_id = message.document.file_id
#     print(message.content_type)
#     file = await bot.get_file(file_id)
#     await bot.download(file, message.document.file_name)
#     await message.answer("Adminga yuborildi")
#
#
# async def main() -> None:
#     bot = Bot(token=TOKEN)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     asyncio.run(main())

#
# import asyncio
# import logging
# import sys
# from datetime import datetime
#
# from aiogram import Bot, Dispatcher
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import CommandStart
# from aiogram.fsm.context import FSMContext
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.fsm.storage.memory import MemoryStorage
# from aiogram.fsm.storage.redis import RedisStorage
# from aiogram.types import Message
#
# TOKEN = '8233140536:AAECu2w9qPH0QmyuLX0UtIkkZA6n6LC7piQ'
#
# redis_url = 'redis://localhost:6379/0'
# dp = Dispatcher(storage=RedisStorage.from_url(redis_url))
#
#
# class Form(StatesGroup):
#     first_name = State()
#     birth_date = State()
#     image = State()
#
#
# @dp.message(CommandStart())
# async def command_start(message: Message, state: FSMContext) -> None:
#     await state.set_state(Form.first_name)
#     await message.answer("Xush kelibsz broooo\n"
#                          "Ismingizni kiriting:")
#
#
# @dp.message(Form.first_name)
# async def command_start(message: Message, state: FSMContext) -> None:
#     await state.update_data(first_name=message.text)
#     await state.set_state(Form.birth_date)
#     await message.answer("Tug‘ilgan sanangizni kiriting (YYYY.MM.DD): ")
#
#
# @dp.message(Form.birth_date)
# async def command_start(message: Message, state: FSMContext) -> None:
#     year = message.text
#
#     if year.isdigit() and 2000 < int(year) <= datetime.now().year:
#         await state.update_data(birth_day=year)
#         data = await state.get_data()
#         await state.clear()
#         text = (f"<b>First_name:</b> {data['first_name']}\n"
#                 f"<b>Data_birth:</b> {data['data_birth']}\n")
#         await message.answer_photo(data['image'], caption=text)
#     else:
#         await message.reply('Kamida 18 yosh bolsin')
#
#
# @dp.message(Form.image)
# async def command_start(message: Message, state: FSMContext) -> None:
#     if message.photo is None:
#         await message.reply('Rasm tashlash kerak ------>  (rasm formatda kelsin)')
#         return
#     file_id = message.photo[-1].file_id
#     await state.update_data(image=file_id)


# @dp.message(Form.birth_day)
# async def command_start(message: Message, state: FSMContext) -> None:
#     year = message.text
#
#     if year.isdigit() and 2005 < int(year) <= datetime.now().year:
#         await state.update_data(birth_day=year)
#         data = await state.get_data()
#         await state.clear()
#         text = (f"<b>Brand:</b> {data['brand']}\n"
#                 f"<b>Model:</b> {data['model']}\n"
#                 f"<b>Release Year:</b> {data['release_year']}\n")
#         await message.answer_photo(data['image'], caption=text)
#     else:
#         await message.reply('Yil 2005 dan katta bolsin')


# @dp.message(CommandStart())
# async def command_start(message: Message, state: FSMContext) -> None:
#     await state.set_state(Form.brand)
#     await message.answer('Xush kelibsiz')
#     await message.answer('Brand ni kiriting (Chevrolet)')


#
#
# class SettingForm(StatesGroup):
#     name = State()
#
# # name
# # phone_number
#
# @dp.message(CommandStart())
# async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
#     text = "Xush kelibsiz!"
#     rkm = ReplyKeyboardBuilder()
#     rkm.add(
#         KeyboardButton(text='Name'),
#         KeyboardButton(text='Description'),
#         KeyboardButton(text='Photo')
#     )
#     await message.answer(text, reply_markup=rkm.as_markup(resize_keyboard=True))
#     # await state.set_state(Form.name)
#     # await message.answer("Seminarga xush kelibsiz\n ismingizni kiriting!")
#
#
# @dp.message(lambda msg: msg.text == 'Name')
# async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
#     await state.set_state(SettingForm.name)
#     await message.answer('Bot uchun nom kiriting')
#
#
# @dp.message(SettingForm.name)
# async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
#     await state.clear()
#     await bot.set_my_name(message.text)
#     await message.answer('Bot nomi ozgartirildi')
#
#
# # @dp.message(Form.name)
# # async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
# #     await state.update_data(name=message.text)
# #     await state.set_state(Form.age)
# #     await message.answer("yoshingizni kiriting")
# #
# #
# # @dp.message(Form.age)
# # async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
# #     await state.update_data(age=message.text)
# #     await state.set_state(Form.phone)
# #     await message.answer("nomer kiriting")
# #
# #
# # @dp.message(Form.phone)
# # async def command_start(message: Message, bot: Bot, state: FSMContext) -> None:
# #     await state.update_data(phone=message.text)
# #     data = await state.get_data()
# #
# #     text = ''
# #     for k, v in data.items():
# #         text += f'{k}: {v}\n'
# #
# #     # await state.clear()
# #     ikm = InlineKeyboardBuilder()
# #     ikm.add(
# #         InlineKeyboardButton(text='Yes', style='success', callback_data='yes'),
# #         InlineKeyboardButton(text='No', style='danger', callback_data='no')
# #     )
# #     await message.answer(f"Malumotlarni to'g'rimi?\n{text}", reply_markup=ikm.as_markup())
#
#
# # p37_group_bot
# @dp.callback_query()
# async def calling_function(callback: CallbackQuery, bot: Bot, state: FSMContext) -> None:
#     if callback.data == 'yes':
#         data = await state.get_data()
#         text = ''
#         for k, v in data.items():
#             text += f'{k}: {v}\n'
#         await bot.send_message(ADMIN_ID, text)
#         await callback.message.delete()
#
#     elif callback.data == 'no':
#         await callback.message.answer('malumotlarni qayta kiriting /start')
#         await callback.message.delete()
#
#
# @dp.message(Command('del'))
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     await bot.delete_messages(message.chat.id, list(range(message.message_id, 0, -1))[:99])
#     ikm = InlineKeyboardBuilder()
#     ikm.add(InlineKeyboardButton(text='btn1', callback_data='123'))
#     await message.answer('<b>Barcha</b> <i>xabarlar</> <u>ochirildi</u>', reply_markup=ikm.as_markup())
#
#
# @dp.message(Command('edit'))
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     ikm = InlineKeyboardBuilder()
#     ikm.add(InlineKeyboardButton(text='yangisi', callback_data='123'))
#
#     await bot.edit_message_reply_markup(chat_id=message.chat.id, message_id=message.message_id - 1,
#                                         reply_markup=ikm.as_markup())
#
#
# @dp.message()
# async def command_start_handler(message: Message, bot: Bot) -> None:
#     ikm = InlineKeyboardBuilder()
#
#     ikm.add(
#         InlineKeyboardButton(text='btn1', callback_data='b1'),
#         InlineKeyboardButton(text='btn2', callback_data='b2'),
#         InlineKeyboardButton(text='❌ inline buttons', callback_data='remove-btn'),
#         InlineKeyboardButton(text='❌ remove msg', callback_data='remove-msg'),
#     )
#     ikm.adjust(2, 1, 1)
#     await message.answer('menyu', reply_markup=ikm.as_markup())
#
#
# @dp.callback_query()
# async def command_start_handler(callback: CallbackQuery) -> None:
#     if callback.data == 'remove-btn':
#         await callback.message.delete_reply_markup(callback.inline_message_id)
#     elif callback.data == 'remove-msg':
#         await callback.message.delete()
#     else:
#         await callback.answer(f"{callback.data} bu kalit")

# async def startup(bot: Bot) -> None:
#     await bot.set_my_name('Yangi bot')
#     await bot.send_message(ADMIN_ID, 'bot started!')
#     await bot.set_my_commands([
#         BotCommand(command='del', description='Ochirish uchun'),
#         BotCommand(command='edit', description='ozgartirish uchun')
#     ], scope=BotCommandScopeAllPrivateChats())

# async def shutdown(bot: Bot) -> None:
#     await bot.send_message(ADMIN_ID, 'bot stopped!')
#
#
# async def main() -> None:
#     bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
#     # dp.startup.register(startup)
#     # dp.shutdown.register(shutdown)
#     await dp.start_polling(bot)
#
#
# if __name__ == "__main__":
#     logging.basicConfig(level=logging.INFO, stream=sys.stdout)
#     asyncio.run(main())
