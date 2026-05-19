from Epiland.keyboard import *
from Epiland.queries import *
from Epiland.utils import *

import time


def init(bot, user_data):

    @bot.message_handler(func=lambda m: m.text == "📍 Інфо")
    def info_entry(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "info_menu")

        bot.send_message(
            chat_id,
            "🌟 Тут зібрано все найважливіше про парк 👇\n\n"
            "Що саме тебе цікавить?",
            reply_markup=info_menu()
        )




    @bot.message_handler(func=lambda m: m.text == "🏰 Про парк")
    def about_park(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data[chat_id]["park_id"]

        data = get_park_info(park_id)

        text = (
            f"🏰 *{data[0].upper()}*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"📍 *Місто:* {data[1]}\n\n"

            f"✨ *Що на тебе чекає:*\n"
            f"{data[2]}\n\n"

            f"🎢 Атракціони\n"
            f"🎉 Святкові кімнати\n"
            f"🧠 Тематичні зони\n"
            f"🎈 Купа емоцій для дітей та батьків\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 Обирай, що хочеш дізнатись далі"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=info_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "📍 Адреса")
    def address(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data[chat_id]["park_id"]

        data = get_park_info(park_id)

        text = (
            f"📍 *ДЕ МИ ЗНАХОДИМОСЬ*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"🏰 *{data[0]}*\n"
            f"📌 {data[4]}\n\n"

            f"🚗 Зручно добиратись як авто,\n"
            f"так і громадським транспортом\n\n"

            f"✨ Чекаємо тебе у гості!"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=info_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "☎️ Контакти")
    def contacts(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        text = (
            f"☎️ *🏛️ КОНТАКТИ ПАРКУ EPILAND*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"📞 (073) 274-2727 — Менеджер свят"
            f"📞 (050) 380-8019 — Банкетний менеджер"
            f"📞 (073) 271-2727 — Адміністратор"

            f"💬 Якщо у вас виникли питання щодо:\n"
            f"• святкування Днів народжень\n"
            f"• бронювання квитків та локацій\n"
            f"• чинних тарифів та акцій\n"
            f"• розважальних програм парку\n\n"

            f"✨ Наші менеджери із радістю допоможуть вам!"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=info_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "🕒 Графік роботи")
    def working_hours(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data[chat_id]["park_id"]

        data = get_park_info(park_id)

        text = (
            f"🕒 *ГРАФІК РОБОТИ*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"⏰ {data[5]}\n\n"

            f"🎢 Атракціони працюють щодня\n"
            f"🎉 Святкові кімнати — за бронюванням\n\n"

            f"✨ Радимо бронювати свята завчасно"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=info_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "🌐 Соцмережі")
    def socials(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data[chat_id]["park_id"]

        data = get_park_info(park_id)

        text = (
            f"🌐 *МИ В СОЦМЕРЕЖАХ*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"{data[6]}\n\n"

            f"📸 Фото свят\n"
            f"🎢 Нові атракціони\n"
            f"🎁 Акції та подарунки\n"
            f"🔥 Актуальні новини парку\n\n"

            f"✨ Підписуйся, щоб нічого не пропустити"
        )

        bot.send_message(
            chat_id,
            text,
            reply_markup=info_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "🎟 Перейти до бронювання")
    def go_booking(message):

        chat_id = message.chat.id

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        text = (
            "🎉 Супер!\n\n"
            "Давай організуємо щось справді незабутнє ✨\n\n"
            "👇 Обирай, що хочеш зробити далі:"
        )

        bot.send_message(
            chat_id,
            text,
            reply_markup=main_menu_kb()
        )