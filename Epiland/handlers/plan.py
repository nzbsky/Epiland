from Epiland.keyboard import *
from Epiland.utils import *
import time


def init(bot, user_data):

    @bot.message_handler(func=lambda m: m.text == "🧠 План")
    def plan_menu(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "plan_menu")

        text = (
            f"🧠 *Допоможу скласти ідеальний план відпочинку!*\n\n"

            f"Можемо:\n"
            f"🎢 підібрати розваги\n"
            f"👶 знайти варіанти за віком\n"
            f"⏰ розрахувати приблизний час\n"
            f"🎉 скласти план для свята\n"
            f"👨‍👩‍👧 допомогти для сімейного відпочинку\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Для кого плануємо відпочинок?*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=plan_menu_kb()
        )

    @bot.message_handler(func=lambda m: m.text == "👶 Для дітей")
    def kids_plan(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "plan_kids_age")

        text = (
            f"👶 *Супер!*\n\n"

            f"Зараз підберемо найкращі розваги\n"
            f"саме для цього віку ✨\n\n"

            f"👇 Обери вік дітей:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=age_choice_book()
        )


    

    @bot.message_handler(func=lambda m: m.text == "👨‍👩‍👧 Для сім'ї")
    def family_plan(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "plan_family")

        text = (
            f"👨‍👩‍👧 *Для сімейного відпочинку рекомендуємо:*\n\n"

            f"🎮 VR та симулятори\n"
            f"🎯 інтерактивні ігри\n"
            f"🏆 командні активності\n"
            f"📸 фотозони та тематичні локації\n\n"

            f"✨ Найчастіше сім'ї проводять у парку\n"
            f"від 2 до 5 годин 😎\n\n"

            f"👇 Хочеш подивитися розваги?"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=entertainments_menu()
        )



    @bot.message_handler(func=lambda m: m.text == "🎉 Для свята")
    def celebration_plan(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        text = (
            f"🎉 *Для ідеального свята рекомендуємо:*\n\n"

            f"🏠 тематичну кімнату\n"
            f"🎢 2-4 розваги\n"
            f"🎂 святкову програму\n"
            f"📸 фотозону\n\n"

            f"✨ У середньому святкування триває\n"
            f"2-3 години 🎈\n\n"

            f"👇 Переходимо до організації?"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=booking_start_kb()
        )