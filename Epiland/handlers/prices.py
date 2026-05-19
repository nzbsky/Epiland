from Epiland.keyboard import *
from Epiland.queries import *
from Epiland.utils import *
import time

def init (bot, user_data):

    @bot.message_handler(func=lambda m: m.text == "💳 Ціни та Тарифи")
    def answer_prices(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "check_prices")

        bot.send_message(
            chat_id,
            "💰 Хочеш подивитися ціни актуальних тарифів?",
            reply_markup=prices_menu()
        )

    @bot.message_handler(func=lambda m: m.text == "💳 Подивитися ціни тарифів" or m.text == "💳 Подивитися інші тарифи")
    def answer_prices(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data.get(chat_id, {}).get("park_id")
        set_step(user_data, chat_id, "check_prices")
        tariffs = get_tariffs(park_id)

        bot.send_message(
            chat_id,
            "Обирай тариф, а я розповім більше ✨",
            reply_markup=tariffs_menu(tariffs)
        )


    @bot.message_handler(func=lambda m: m.text.startswith("💫"))
    def show_tariff_details(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        park_id = user_data.get(chat_id, {}).get("park_id")

        name = message.text.replace("💫", "").strip()
        user_data[chat_id]["selected_tariff"] = name

        data = get_tariff_details(park_id, name)

        if not data:
            bot.send_message(chat_id, "❌ Немає даних")
            return

        set_step(user_data, chat_id, "tariff_details")

        text = (
                    f"🎢 *{name.upper()}*\n"
                    f"━━━━━━━━━━━━━━━━━━\n\n"

                    f"✨ *Що це:*\n"
                    f"{data[0]}\n\n"

                    f"⏱ *Формат:* {data[1]}\n\n"

                    f"💰 *Вартість:*\n"
                    f"▫️ Будні: *{data[2]} грн*\n"
                    f"▫️ Вихідні: *{data[3]} грн*\n\n"

                    f"━━━━━━━━━━━━━━━━━━\n"
                    f"👇 *Що далі?*"
                )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=after_choosing_tariff()
        )


