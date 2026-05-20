import time
from Epiland.keyboard import *
from Epiland.utils import *

def init(bot, user_data):

    @bot.message_handler(commands=['start', 'reset'])
    def start(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        bot.send_message(
            chat_id,
            "🎢 Вітаю, мій мандрівнику!\nОбери світ, у який хочеш потрапити 👇",
            reply_markup=parks_kb()
        )




    @bot.message_handler(func=lambda m: m.text in ["🏰 ПАНДОРА", "🌿 ЧАРІВНИЙ ЛІС", "🌌 СВІТ КОМІКСІВ"] or m.text == "🚀 Головне меню")
    def choose_park(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        if message.text == "🚀 Головне меню":
            bot.send_message(chat_id, "✨ Чудовий вибір!\nЩо тебе цікавить?", reply_markup=main_menu_kb())
            return

        park_map = {
            "🏰 ПАНДОРА": 1,
            "🌿 ЧАРІВНИЙ ЛІС": 2,
            "🌌 СВІТ КОМІКСІВ": 3
        }

        user_data[chat_id]["park_id"] = park_map[message.text]
        user_data[chat_id]["step"] = "main_menu"

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        bot.send_message(
            chat_id,
            "✨ Чудовий вибір!\nЩо тебе цікавить?",
            reply_markup=main_menu_kb()
        )

