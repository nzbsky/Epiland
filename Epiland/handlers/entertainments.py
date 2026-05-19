from Epiland.keyboard import *
from Epiland.queries import *
from Epiland.utils import *
import time


def init(bot, user_data):

    @bot.message_handler(
        func=lambda m:
        m.text == "🎢 Розваги"
        or m.text == "🎢 Подивитися ціни окремих розваг"
        or m.text == "🎢 Подивитися інші"
        or m.text == "🎢 Окремі розваги для свята"
    )
    def enter(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "entertainments_menu")

        text = (
            f"🎢 *Час для пригод!*\n\n"

            f"У нас є:\n"
            f"🔥 екстремальні атракціони\n"
            f"🕹 VR та інтерактивні зони\n"
            f"👶 дитячі активності\n"
            f"🎯 командні ігри\n"
            f"🎉 розваги для святкувань\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Як хочеш обрати розваги?*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=entertainments_menu()
        )

    @bot.message_handler(func=lambda m: m.text == "🎢 Розваги для свята" or m.text == "🔎 Подивитися інші" or m.text == "🎢 Обрати розваги" or m.text == "➕ Додати ще розваги")
    def enter(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        bot.send_message(
            chat_id,
            "Супер, обирай, що хочеш подивитися, я з радістю покажу всі актуальні деталі 😊",
            parse_mode="Markdown",
            reply_markup=entertainments_for_birthday_kb()
        )




    @bot.message_handler(
        func=lambda m:
        m.text == "🔎 Подивитися інші розваги"
        or m.text == "🔎 Дивимось ще"
        or m.text == "🎢 Просто подивитися інші"
        or m.text == "🎉 Обрати щось інше"
    )
    def show_other(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data.get(chat_id, {}).get("park_id")

        items = get_entertainments(park_id)

        set_step(user_data, chat_id, "choose_entertainment")

        text = (
            f"🚀 *Супер вибір!*\n\n"

            f"Для ідеального свята можна поєднувати\n"
            f"одразу декілька розваг 🎢✨\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 Обирай будь-яку розвагу —\n"
            f"я покажу всі деталі"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=choose_entertainment(items)
        )




    @bot.message_handler(func=lambda m: m.text == "➕ Додати програму")
    def show_all(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "add_birthday_item")

        text = (
            f"🚀 *У нас дууууже багато всього цікавого!*\n\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Обирай будь-яку вид програми*\n"
            f"та дивись ціни, формат і вік ✨"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=entertainments_for_birthday_kb()
        )




    @bot.message_handler(func=lambda m: m.text == "📋 Показати всі розваги")
    def show_all(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user_data.get(chat_id, {}).get("park_id")

        items = get_entertainments(park_id)

        set_step(user_data, chat_id, "choose_entertainment")

        text = (
            f"🚀 *У нас дууууже багато всього цікавого!*\n\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Обирай будь-яку розвагу*\n"
            f"та дивись ціни, формат і вік ✨"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=choose_entertainment(items)
        )


    @bot.message_handler(func=lambda m: m.text == "🎯 Підібрати для мене")
    def choose_age_handler(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "choose_age")

        text = (
            f"🎯 *Зараз підберемо ідеальний варіант*\n\n"

            f"Щоб не переглядати все підряд,\n"
            f"давай знайдемо розваги,\n"
            f"які точно підійдуть за віком 👶✨\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Обери вік:*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=age_choice_book()
        )


    @bot.message_handler(func=lambda m: m.text in ["🫶 3-5", "🫶 6-8", "🫶 9-12","🫶 13-16"])
    def age_selected(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        age_map = {
            "🫶 3-5": 4,
            "🫶 6-8": 7,
            "🫶 9-12": 10,
            "🫶 13-16": 14
        }

        age = age_map[message.text]

        user_data[chat_id]["age"] = age
        user_data[chat_id]["age_printed"] = message.text

        park_id = user_data.get(chat_id, {}).get("park_id")

        items = get_entertainments_by_age(park_id, age)

        set_step(user_data, chat_id, "choose_entertainment")

        text = (
            f"🔥 *Оооо, знайшов дещо круте!*\n\n"

            f"Ці розваги найкраще підходять\n"
            f"саме для цього віку 🎯\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 *Обирай, що хочеш подивитися:*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=choose_entertainment(items)
        )


    @bot.message_handler(func=lambda m: m.text.startswith("✔️"))
    def select_ent(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        park_id = user.get("park_id")

        name = message.text.replace("✔️", "").strip()

        user["selected_entertainment"] = name

        if "preferences" not in user:
            user["preferences"] = []

        if "selected_entertainments" not in user:
            user["selected_entertainments"] = []

        data = get_entertainment_details(park_id, name)

        if not data:
            bot.send_message(chat_id, "❌ Інформацію не знайдено")
            return

        set_step(user_data, chat_id, "entertainment_details")

        status_text = ""

        if name in user["preferences"]:
            status_text += "⭐ Додано в улюблені\n"

        if name in user["selected_entertainments"]:
            status_text += "🎉 Додано до святкування\n"

        text = (
            f"🎢 *{name.upper()}*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"✨ *Що це таке?*\n"
            f"{data[0]}\n\n"

            f"👶 *Рекомендований вік:*\n"
            f"від *{data[1]}* до *{data[2]}* років\n\n"

            f"🎮 *Формат гри:*\n"
            f"{data[5]}\n\n"

            f"💰 *Вартість:*\n"
            f"▫️ Будні — *{data[3]} грн*\n"
            f"▫️ Вихідні — *{data[4]} грн*\n\n"

            f"🎉 *Що можна зробити:*\n"
            f"✅ просто приїхати та грати\n"
            f"✅ додати до святкування\n"
            f"✅ зберегти в улюблені\n"
            f"✅ поєднати з іншими розвагами\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"

            f"{status_text}\n"

            f"👇 *Що робимо далі?*"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=after_choosing_entertainment()
        )


    @bot.message_handler(func=lambda m: m.text == "⭐ Додати в улюблені")
    def add_to_preferences(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        name = user.get("selected_entertainment")

        if not name:
            bot.send_message(chat_id, "❌ Спочатку обери розвагу")
            return

        if "preferences" not in user:
            user["preferences"] = []

        if name not in user["preferences"]:
            user["preferences"].append(name)

        set_step(user_data, chat_id, "add_to_preferences")

        text = (
            f"⭐ *Розвагу додано в улюблені!*\n\n"

            f"🎢 *{name}*\n\n"

            f"Тепер ти зможеш швидко\n"
            f"додати її до святкування ✨"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=book_ent()
        )


    @bot.message_handler(func=lambda m: m.text == "🎉 Додати до святкування")
    def add_to_booking(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        name = user.get("selected_entertainment")

        if not name:
            bot.send_message(chat_id, "❌ Спочатку обери розвагу")
            return

        if "selected_entertainments" not in user:
            user["selected_entertainments"] = []

        if name not in user["selected_entertainments"]:
            user["selected_entertainments"].append(name)

        set_step(user_data, chat_id, "add_to_booking")

        entertainments_text = ""

        for ent in user["selected_entertainments"]:
            entertainments_text += f"🎢 {ent}\n"

        text = (
            f"🎉 *Розвагу додано до святкування!*\n\n"

            f"✨ Зараз у святкуванні:\n\n"
            f"{entertainments_text}\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"👇 Що робимо далі?"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=book_ent()
        )


    @bot.message_handler(func=lambda m: m.text == "⭐ Мої улюблені")
    def show_preferences(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        preferences = user.get("preferences", [])

        if not preferences:

            bot.send_message(
                chat_id,
                "⭐ У тебе поки немає улюблених розваг"
            )

            return

        text = "⭐ *Твої улюблені розваги:*\n\n"

        for ent in preferences:
            text += f"🎢 {ent}\n"

        text += (
            "\n━━━━━━━━━━━━━━━━━━\n"
            "👇 Можеш додати їх до святкування"
        )

        set_step(user_data, chat_id, "show_preferences")

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=preferences_kb(preferences)
        )




    @bot.message_handler(func=lambda m: m.text == "🎭 Шоу-програми")
    def show_programs(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        park_id = user_data[chat_id]["park_id"]

        items = get_birthday_items_by_category(
            park_id,
            "Шоу-програми"
        )

        set_step(user_data, chat_id, "show_programs")

        bot.send_message(
            chat_id,
            "🎭 Обирай шоу-програму ✨",
            reply_markup=birthday_items_kb(items)
        )


    @bot.message_handler(func=lambda m: m.text == "🧪 Майстер-класи")
    def master_classes(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        park_id = user_data[chat_id]["park_id"]

        items = get_birthday_items_by_category(
            park_id,
            "Майстер-класи"
        )

        set_step(user_data, chat_id, "master_classes")

        bot.send_message(
            chat_id,
            "🧪 Обирай майстер-клас ✨",
            reply_markup=birthday_items_kb(items)
        )


    @bot.message_handler(func=lambda m: m.text == "🗺 Квести")
    def quests(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        park_id = user_data[chat_id]["park_id"]

        items = get_birthday_items_by_category(
            park_id,
            "Квести"
        )

        set_step(user_data, chat_id, "quests")

        bot.send_message(
            chat_id,
            "🗺 Обирай квест ✨",
            reply_markup=birthday_items_kb(items)
        )




    @bot.message_handler(func=lambda m: m.text.startswith("➡️"))
    def birthday_item_details(message):

        chat_id = message.chat.id

        ensure_user(user_data, chat_id)

        name = message.text.replace("➡️", "").strip()

        data = get_birthday_item_details(name)

        if not data:

            bot.send_message(
                chat_id,
                "❌ Інформацію не знайдено"
            )

            return

        user_data[chat_id]["selected_birthday_item"] = name

        text = (
            f"🎉 *{name}*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"✨ {data[4]}\n\n"

            f"👶 *Вік:* {data[2]} - {data[3]} років\n\n"

            f"💰 *Вартість:* {data[1]} грн\n"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=add_birthday_item_kb()
        )