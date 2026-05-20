from Epiland.keyboard import *
from Epiland.utils import *
import time


def init(bot, user_data):

    @bot.message_handler(func=lambda m: m.text == "🎉 День народження")
    def birthday_menu(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "birthday_menu")

        text = (
            f"🎉 *День народження в парку — це щось неймовірне!*\n\n"

            f"У нас можна:\n"
            f"🎢 обрати круті розваги\n"
            f"🏠 забронювати тематичну кімнату\n"
            f"🎂 організувати повне свято\n"
            f"📸 зробити незабутні фото\n"
            f"🎁 отримати допомогу менеджера\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Що хочеш зробити?*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=birthday_menu_kb()
        )


    @bot.message_handler(func=lambda m: m.text == "🎉 Організувати свято")
    def quick_party_start(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "booking_children")

        text = (
            f"🎂 *Погнали створювати ідеальне свято!*\n\n"

            f"Я допоможу все підібрати ✨\n\n"

            f"👥 Скільки приблизно буде дітей?"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
        )


    @bot.message_handler(func=lambda m: m.text == "🎢 Подивитися розваги для свята")
    def birthday_entertainments(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        text = (
            f"🎢 *Для святкування у нас є дуже багато всього!*\n\n"

            f"🔥 VR та симулятори\n"
            f"🎯 командні ігри\n"
            f"🕹 інтерактивні зони\n"
            f"🏆 челенджі та атракціони\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 Переходимо до розваг"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=entertainments_menu()
        )

        set_step(user_data, chat_id, "entertainments_menu")



    @bot.message_handler(func=lambda m: m.text == "🏠 Подивитися кімнати")
    def birthday_rooms(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "birthday_rooms")

        text = (
            f"🏠 *У нас є тематичні кімнати для різного віку!*\n\n"

            f"✨ Є кімнати для маленьких дітей\n"
            f"🎮 кімнати для геймерів\n"
            f"🌌 атмосферні VIP-зони\n"
            f"🎉 великі кімнати для компаній\n\n"

            f"👇 Обери приблизний вік дітей:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=age_choice_book()
        )


    @bot.message_handler(func=lambda m: m.text == "📞 Допомога менеджера")
    def birthday_manager(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "manager_help")

        text = (
            f"📞 *Менеджер допоможе організувати свято!*\n\n"

            f"Можеш:\n"
            f"• уточнити ціни\n"
            f"• дізнатися про вільні дати\n"
            f"• отримати допомогу з вибором\n"
            f"• попросити повністю підібрати свято ✨\n\n"

            f"👇 Напиши номер телефону або питання:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown"
        )



    @bot.message_handler(func=lambda m:
        m.text in [
            "🎭 Шоу-програми",
            "🧪 Майстер-класи",
            "🗺 Квести"
        ]
    )
    def birthday_category(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        category_map = {
            "🎭 Шоу-програми": "Шоу-програми",
            "🧪 Майстер-класи": "Майстер-класи",
            "🗺 Квести": "Квести"
        }

        category = category_map[message.text]

        park_id = user_data[chat_id]["park_id"]

        items = get_birthday_items_by_category(
            park_id,
            category
        )

        set_step(user_data, chat_id, "birthday_items")

        bot.send_message(
            chat_id,
            "🎉 Обирай програму 👇",
            reply_markup=birthday_items_kb(items)
        )


    @bot.message_handler(func=lambda m: m.text.startswith("➡️"))
    def birthday_item_details(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        name = message.text.replace("➡️", "").strip()

        data = get_birthday_item_details(name)
        user_data['selected_birthday_item'] = message.text()
        if not data:
            return

        text = (
            f"🎉 *{name}*\n\n"

            f"📂 Категорія: {data[0]}\n"
            f"👶 Вік: {data[2]}-{data[3]}\n"
            f"💰 Ціна: {data[1]} грн\n\n"

            f"{data[4]}"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=add_birthday_item_kb()
        )


    @bot.message_handler(func=lambda m:
        m.text == "✅ Додати до свята"
    )
    def add_birthday_item(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        selected = user.get("selected_birthday_item")

        if not selected:
            return

        if "birthday_items" not in user:
            user["birthday_items"] = []

        if selected not in user["birthday_items"]:
            user["birthday_items"].append(selected)

        bot.send_message(
            chat_id,
            "🎉 Додано до свята! Давай продовжувати 🎉",
            reply_markup=birthday_menu_kb()
        )