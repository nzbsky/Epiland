from telebot import TeleBot

from dotenv import load_dotenv

import os

from handlers import start
from handlers import booking
from handlers import entertainments
from handlers import prices
from handlers import info
from handlers import birthday
from handlers import plan
from handlers import ai_handler


load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = TeleBot(TELEGRAM_TOKEN)

user_data = {}

start.init(bot, user_data)
booking.init(bot, user_data)
entertainments.init(bot, user_data)
prices.init(bot, user_data)
info.init(bot, user_data)
birthday.init(bot, user_data)
plan.init(bot, user_data)


ai_handler.init(bot, user_data)


bot.infinity_polling()
print ("Bot is running...")