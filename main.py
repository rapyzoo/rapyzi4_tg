from asyncore import read
from calendar import c
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import Message
import random

bot = Bot(token='5369934578:AAGj85WkjHd-wJuFSx5yO-f_M0iiKWoODsQ')
dp = Dispatcher(bot)

file_wallets = open('dry.txt', 'r', encoding='utf-8')

lines = file_wallets.readlines()
lines = [line.rstrip('\n') for line in lines]

file_wallets.close()

ADMIN = '1247057378'
whitelist = ['1794493767']

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nНапиши /give")

@dp.message_handler(commands=['give'])
async def give_command(message: types.Message):
    if not message.chat.id in whitelist:
        await message.reply('Вы не находитесь в белом списке')
    else:
        await message.reply(random.choice(lines))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)