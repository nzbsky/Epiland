from Epiland.gemini import ask_gemini

from Epiland.keyboard import *

from Epiland.utils import *

import time

SYSTEM_BUTTONS = [

    "⬅️ Назад",
    "🔄 Скинути",
    "🚀 Головне меню",

    "🏰 ПАНДОРА",
    "🌿 ЧАРІВНИЙ ЛІС",
    "🌌 СВІТ КОМІКСІВ",

    "🎢 Розваги",
    "🎉 День народження",
    "💰 Ціни",
    "🧠 План",
    "📍 Інфо",
    "📞 Забронювати",

    "📋 Показати всі розваги",
    "🎯 Підібрати для мене",
    "⭐ Мої улюблені",
    "🎢 Подивитися ціни окремих розваг",
    "🔎 Подивитися інші розваги",
    "🎢 Просто подивитися інші",
    "🎉 Обрати щось інше",

    "⭐ Додати в улюблені",
    "⭐ Додати до свята улюблені розваги",

    "🎟 Забронювати",
    "🎉 Організувати свято",
    "🎉 Забронювати свято",
    "🎉 Організувати свято зараз",
    "🎉 Організувати свято з цим",
    "🎉 Організувати свято з цим тарифом",
    "🎉 Додати до святкування",
    "🎉 Забронювати",
    "📞 Консультація менеджера",

    "🎢 Обрати розваги",

    "➕ Додати ще розваги",
    "✅ Продовжити бронювання",

    "🔎 Дивимось ще",

    "💰 Подивитися ціни тарифів",
    "💰 Подивитися інші тарифи",

    "🏰 Про парк",
    "📍 Адреса",
    "☎️ Контакти",
    "🕒 Графік роботи",
    "🌐 Соцмережі",
    "🎟 Перейти до бронювання",

    "🎢 Подивитися розваги для свята",
    "🏠 Подивитися кімнати",
    "📞 Допомога менеджера",

    "👶 Для дітей",
    "👨‍👩‍👧 Для сім'ї",
    "🎉 Для свята",

    "✅ Підтвердити",
    "❌ Скасувати",

    "📱 Надіслати номер телефону",

]

BLOCKED_STEPS = [

    "booking_children",
    "booking_age",
    "booking_room",
    "booking_date",
    "booking_time",
    "booking_contacts",
    "booking_confirm"

]


def init(bot, user_data):


    @bot.message_handler(
        func=lambda m: True,
        content_types=['text']
    )
    def ai_handler(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        text = message.text.strip()

        current_step = user.get("step")


        if text in SYSTEM_BUTTONS:
            return

        if current_step in BLOCKED_STEPS:
            return



        bot.send_chat_action(chat_id, 'typing')

        response = ask_gemini(
            text=text,
            current_step=current_step,
            user_state=user
        )

        intent = response.get("intent", "UNKNOWN")


        if intent == "BOOK_PARTY":

            set_step(
                user_data,
                chat_id,
                "booking_children"
            )

            bot.send_message(
                chat_id,
                (
                    "🎉 Давай організуємо "
                    "супер свято!\n\n"
                    "👥 Скільки буде дітей?"
                ),
                reply_markup=number_of_children()
            )

            return



        elif intent == "SHOW_ENTERTAINMENTS":

            set_step(
                user_data,
                chat_id,
                "entertainments_menu"
            )

            bot.send_message(
                chat_id,
                "🎢 Добре, давай разом виберемо розваги! Обери наступний пункт меню 👇",
                reply_markup=entertainments_menu()
            )

            return


        elif intent == "SHOW_PRICES":

            set_step(
                user_data,
                chat_id,
                "prices_menu"
            )

            bot.send_message(
                chat_id,
                "💰 Давай подивимось ціни. Що хочеш подивитися?",
                reply_markup=prices_menu()
            )

            return



        elif intent == "SHOW_INFO":

            set_step(
                user_data,
                chat_id,
                "info_menu"
            )

            bot.send_message(
                chat_id,
                "📍 Що саме тебе цікавить?",
                reply_markup=info_menu()
            )

            return


        elif intent == "SHOW_PLAN":

            set_step(
                user_data,
                chat_id,
                "plan_menu"
            )

            bot.send_message(
                chat_id,
                "🧠 Допоможу спланувати відпочинок!",
                reply_markup=plan_menu_kb()
            )

            return



        elif intent == "MANAGER_HELP":

            set_step(
                user_data,
                chat_id,
                "manager_help"
            )

            bot.send_message(
                chat_id,
                (
                    "📞 Наші менеджери завжди готові допомогти. Напиши мвоє питання, а я передам його ✨"
                )
            )

            return


        bot.send_message(
            chat_id,
            response.get(
                "reply",
                (
                    "😔 Не зовсім зрозумів тебе.\n"
                    "Спробуй кнопки нижче 👇"
                )
            ),
            reply_markup=main_menu_kb()
        )