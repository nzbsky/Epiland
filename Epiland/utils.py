from datetime import datetime
from Epiland.keyboard import *
from Epiland.queries import *
import time


def default_user():
    return {
        "step": None,          # поточний етап
        "history": [],         # історія для кнопки "назад"

        "park_id": None,       # обраний парк

        "last_activity": time.time(),
        "selected_entertainments": [],  # вибрана розвага
        "birthday_items": [],
        "preferences": [],
        "age": None,           # вік для підбору

        "booking": {           # всі дані бронювання в одному місці
            "children_count": None,
            "age_group": None,
            "room_id": None,
            "room_name": None,
            "date": None,
            "time": None
        }
    }



def ensure_user(user_data, chat_id):
    if chat_id not in user_data:
        user_data[chat_id] = default_user()
    user_data[chat_id]["last_activity"] = time.time()



def set_step(user_data, chat_id, step):
    ensure_user(user_data, chat_id)

    user = user_data[chat_id]

    if user.get("step") is not None:
        user["history"].append(user["step"])  # запам'ятовуємо попередній крок

    user["step"] = step



def go_back(user_data, chat_id):
    ensure_user(user_data, chat_id)

    user = user_data[chat_id]

    if user["history"]:
        user["step"] = user["history"].pop()  # повертаємось на попередній step
        return user["step"]

    return None  # якщо історії нема



def reset_user(user_data, chat_id):
    user_data[chat_id] = default_user()  # повністю очищаємо state



def is_working_hours():
    hour = datetime.now().hour
    return 9 <= hour < 21 



def get_booking(user_data, chat_id):
    ensure_user(user_data, chat_id)
    return user_data[chat_id]["booking"]


def render_step(bot, user_data, chat_id, step):

    user = user_data[chat_id]


    if step == "main_menu":

        bot.send_message(
            chat_id,
            "✨ Що тебе цікавить?",
            reply_markup=main_menu_kb()
        )

    elif step == "entertainments_menu":

        bot.send_message(
            chat_id,
            "🎢 Як хочеш обрати розваги?",
            reply_markup=entertainments_menu()
        )

    elif step == "choose_age":

        bot.send_message(
            chat_id,
            "👇 Обери вік:",
            reply_markup=age_choice_book()
        )

    elif step == "choose_entertainment":

        park_id = user["park_id"]

        items = get_entertainments(park_id)

        bot.send_message(
            chat_id,
            "👇 Обирай розвагу:",
            reply_markup=choose_entertainment(items)
        )

    elif step == "booking_children":

        bot.send_message(
            chat_id,
            "👥 Скільки буде дітей?",
            reply_markup=number_of_children()
        )


    