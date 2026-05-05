import logging
import asyncio
import os
from aiogram.filters import Command
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')

bot = Bot(token=TOKEN)

dp = Dispatcher()

# Handles start command

@dp.message(Command('start'))
async def start(message: types.Message):
    await message.answer('Привіт!')

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
