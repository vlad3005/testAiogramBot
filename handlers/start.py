from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from keyboards.all_keyboards import main_kb

start_router = Router()

@start_router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start используя фильтр CommandStart()',
                         reply_markup=main_kb(message.from_user.id))
@start_router.message(Command('start_2'))
async def cmd_start(message: Message):
    await message.answer('Запуск сообщения по команде /start_2 используя фильтр Command()')
#
# @start_router.message(F.text == '/start_3')
# async def cmd_start(message: Message):
#     await message.answer('Запуск сообщения по команде /start_3 используя магический фильтр F.text!',
#                          reply_markup=create_rat())