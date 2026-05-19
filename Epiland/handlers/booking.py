from Epiland.keyboard import *
from Epiland.queries import *
from Epiland.utils import *
import time



def init(bot, user_data):

    @bot.message_handler(
        func=lambda m:
        m.text == "🎟 Забронювати"
        or
        m.text == "🟢 Забронювати"
    )
    def start_booking(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        if "preferences" not in user:
            user["preferences"] = []

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        if message.text == "🎟 Забронювати":

            if (
                user.get("selected_entertainment")
                and
                user["selected_entertainment"]
                not in user["preferences"]
            ):

                user["preferences"].append(
                    user["selected_entertainment"]
                )

            set_step(
                user_data,
                chat_id,
                "booking_after_entertainment"
            )

            entertainments_text = ""

            if user["preferences"]:

                for ent in user["preferences"]:
                    entertainments_text += f"🎢 {ent}\n"

            else:
                entertainments_text = (
                    "🎢 Поки що без доданих розваг\n"
                )

            text = (
                f"🎉 *Супер вибір!*\n\n"

                f"✨ До твого святкування вже додано:\n\n"

                f"{entertainments_text}\n"

                f"━━━━━━━━━━━━━━━━━━\n"
                f"👇 Що робимо далі?"
            )

            bot.send_message(
                chat_id,
                text,
                parse_mode="Markdown",
                reply_markup=after_choosing_entertainment()
            )

        elif message.text == "🟢 Забронювати":

            set_step(user_data, chat_id, "booking_start")

            text = (
                f"🎉 *Допоможу все організувати!*\n\n"

                f"Можемо:\n"
                f"• підібрати розваги 🎢\n"
                f"• організувати день народження 🎂\n"
                f"• знайти ідеальну кімнату 🏠\n"
                f"• або проконсультувати тебе 📞\n\n"

                f"━━━━━━━━━━━━━━━━━━\n"
                f"👇 З чого почнемо?"
            )

            bot.send_message(
                chat_id,
                text,
                parse_mode="Markdown",
                reply_markup=booking_start_kb()
            )



    @bot.message_handler(
        func=lambda m:
        m.text == "🎉 Організувати свято"
        or
        m.text == "🎉 Забронювати свято"
        or
        m.text == "🎉 Організувати свято зараз"
    )
    def start_party(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        if "preferences" not in user:
            user["preferences"] = []

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "should_add_preferences")

        entertainments_text = ""

        if user["preferences"]:

            for ent in user["preferences"]:
                entertainments_text += f"🎢 {ent}\n"

            text = (
                f"🎂 *Погнали створювати ідеальне свято!*\n\n"

                f"✨ Хочеш додати до нього ось ці свої улюблені розваги?\n\n"
                f"{entertainments_text}\n"

            )
            bot.send_message(
                chat_id,
                text,
                parse_mode="Markdown",
                reply_markup=should_add_favourite()
            )

        else:

            text = (
                f"🎂 *Погнали створювати ідеальне свято!*\n\n"

                f"Я допоможу все підібрати ✨\n\n"

                f"👥 Скільки приблизно буде дітей?"
            )

            bot.send_message(
                chat_id,
                text,
                parse_mode="Markdown",
                reply_markup=number_of_children()
            )



    @bot.message_handler(
        func=lambda m:
        m.text == "⭐ Додати до свята улюблені розваги"
    )
    def add_preferences_to_party(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        if not user.get("preferences"):
            user["preferences"] = []

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        user["selected_entertainments"] = (
            user["preferences"].copy()
        )

        set_step(user_data, chat_id, "booking_children")

        entertainments_text = ""

        for ent in user["selected_entertainments"]:
            entertainments_text += f"🎢 {ent}\n"

        text = (
            f"🎉 *Супер! Додаємо улюблені розваги до свята*\n\n"

            f"✨ Уже додано:\n\n"

            f"{entertainments_text}\n"

            f"━━━━━━━━━━━━━━━━━━\n"

            f"👥 Будемо дивитися ще, чи бронюємо? 😏"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=after_adding_favourite()
        )




    @bot.message_handler(
        func=lambda m:
        m.text == "🎉 Організувати свято з цим"
        or
        m.text == "🎉 Організувати свято з цим тарифом"
        or
        m.text == "🎉 Забронювати"
    )
    def start_party_from_ent(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        user = user_data[chat_id]

        if "preferences" not in user:
            user["preferences"] = []

        if (
            user.get("selected_entertainment")
            and
            user["selected_entertainment"]
            not in user["preferences"]
        ):

            user["preferences"].append(
                user["selected_entertainment"]
            )

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "booking_children")

        entertainments_text = ""

        for ent in user["preferences"]:
            entertainments_text += f"🎢 {ent}\n"

        text = (
            f"🎉 *Ооо, це буде круте свято!*\n\n"

            f"✨ До бронювання вже додано:\n\n"

            f"{entertainments_text}\n"

            f"Тепер організуємо саме свято! Скільки приблизно буде дітей на святкуванні? 👇"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=number_of_children()
        )



    @bot.message_handler(
        func=lambda m:
        m.text == "📞 Консультація менеджера"
    )
    def manager_help(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        set_step(user_data, chat_id, "manager_help")

        text = (
            f"📞 *Менеджер допоможе тобі з вибором!*\n\n"

            f"Можеш:\n"
            f"• поставити будь-які питання\n"
            f"• уточнити ціни\n"
            f"• дізнатися про вільні дати\n"
            f"• або отримати персональну консультацію ✨\n\n"

            f"👇 Напиши номер телефону або питання:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown"
        )



    @bot.message_handler(func=lambda m: m.text.startswith("😺"))
    def children(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        count_map = {
            "😺 1-5": 3,
            "😺 5-10": 7,
            "😺 10-15": 12,
            "😺 15-20": 17,
            "😺 20+": 25
        }

        count = count_map[message.text]

        user_data[chat_id]["children"] = count

        set_step(user_data, chat_id, "booking_age")

        text = (
            f"🔥 *Супер!*\n\n"

            f"Я вже врахував святкування приблизно "
            f"на *{count} дітей* 🎈\n\n"

            f"👇 Який приблизно вік дітей?"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=age_choice_book_after_amount()
        )



    @bot.message_handler(func=lambda m: m.text.startswith("🌟"))
    def age(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        if user_data[chat_id].get("step") != "booking_age":
            return

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        age_map = {
            "🌟 3-5": 4,
            "🌟 6-8": 7,
            "🌟 9-12": 10,
            "🌟 13-16": 14
        }

        age = age_map[message.text]

        user_data[chat_id]["age"] = age
        user_data[chat_id]["age_number"] = age
        user_data[chat_id]["age_printed"] = (
            message.text.replace("🌟", "").strip()
        )

        set_step(user_data, chat_id, "booking_room")

        rooms = get_rooms_by_age(
            user_data[chat_id]["park_id"],
            user_data[chat_id]["age_number"]
        )

        text = (
            f"🏠 *Час обрати кімнату!*\n\n"

            f"✨ Ось кімнати, які найкраще "
            f"підходять для цього віку:\n\n"

            f"👇 Обирай кімнату:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=rooms_kb(rooms)
        )



    @bot.message_handler(func=lambda m: m.text.startswith("🏠"))
    def room(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        user = user_data[chat_id]
        age = user["age"] 
        park_id = user["park_id"]

        name = message.text.replace("🏠", "").strip()

        rooms = get_rooms_by_age(
            park_id,
            age
        )

        room_id = next(
            (r[0] for r in rooms if r[1] == name),
            None
        )

        if not room_id:

            bot.send_message(
                chat_id,
                "❌ Кімнату не знайдено"
            )

            return

        room = get_room_details(room_id)

        user["room_id"] = room_id
        user["room_name"] = room[0]

        set_step(user_data, chat_id, "booking_date")

        dates = get_available_dates(room_id)

        text = (
            f"🏠 *{room[0].upper()}*\n"
            f"━━━━━━━━━━━━━━━━━━\n\n"

            f"🎨 *Тема:* {room[1]}\n"
            f"👥 *До:* {room[2]} дітей\n"
            f"👶 *Вік:* {room[3]}–{room[4]} років\n\n"

            f"✨ {room[5]}\n\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"📅 Обирай дату:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=dates_kb(dates)
        )



    @bot.message_handler(func=lambda m: m.text.startswith("📅"))
    def date(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        date = message.text.replace("📅", "").strip()

        user_data[chat_id]["date"] = date

        times = get_available_times(
            user_data[chat_id]["room_id"],
            date
        )

        set_step(user_data, chat_id, "booking_time")

        text = (
            f"📅 *{date}*\n\n"
            f"🕐 Ось доступний час:"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=times_kb(times)
        )



    @bot.message_handler(func=lambda m: m.text.startswith("🕐"))
    def time_select(message):

        chat_id = message.chat.id
        ensure_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        time_val = message.text.replace("🕐", "").strip()

        user_data[chat_id]["time"] = time_val

        set_step(user_data, chat_id, "booking_contacts")

        user = user_data[chat_id]

        preferences = user.get("preferences", [])
        birthday_items = user.get("birthday_items", [])

        ents_list = ""
        birthday_text = ""

        if preferences:
            ents_list = "\n".join(
                [f"🎢 {ent}" for ent in preferences]
            )
        else:
            ents_list = "🎢 Без додаткових розваг"

        if birthday_items:
            birthday_text = "\n".join(
                [f"🎉 {item}" for item in birthday_items]
            )
        else:
            birthday_text = "🎉 Без шоу-програм"

        recommendation_text = ""


        if not preferences:

            recommendation_text += (
                "\n✨ *Рекомендуємо додати розваги "
                "для більш яскравого свята!*\n"
            )

        if not birthday_items:

            recommendation_text += (
                "\n🎭 *Також можна додати:*\n"
                "• шоу-програму\n"
                "• квест\n"
                "• майстер-клас\n"
            )

        text = (
            f"🎉 *Майже готово!*\n\n"

            f"📅 *Дата:* {user.get('date')}\n"
            f"🕐 *Час:* {user.get('time')}\n\n"

            f"✨ *Обрані розваги:*\n"
            f"{ents_list}\n\n"

            f"🎭 *Програми:*\n"
            f"{birthday_text}\n"

            f"{recommendation_text}\n"

            f"━━━━━━━━━━━━━━━━━━\n"
            f"📞 Для підтвердження заявки "
            f"надішли номер телефону 👇"
        )

        bot.send_message(
            chat_id,
            text,
            parse_mode="Markdown",
            reply_markup=contact_kb()
        )




    @bot.message_handler(content_types=['contact'])
    def handle_contact(message):
        chat_id = message.chat.id
        if message.contact is not None:
            user_data[chat_id]["phone"] = message.contact.phone_number
            user = user_data[chat_id]
            
            ents_list = "\n".join([f"🎢 {ent}" for ent in user.get("preferences", [])]) or "🎢 Без додаткових розваг"
            birthday_items = "\n".join([f"🎉 {item}" for item in user.get("birthday_items", [])]) or "🎢 Без додаткових розваг"

            

            text = (
                f"🧐 *Перевірте ваші дані:*\n\n"
                f"━━━━━━━━━━━━━━━━━━\n\n"

                f"👥 *Дітей:* {user.get('children')}\n"
                f"👶 *Вік:* {user.get('age_printed')}\n"
                f"🏠 *Кімната:* {user.get('room_name')}\n"
                f"📅 *Дата:* {user.get('date')}\n"
                f"🕐 *Час:* {user.get('time')}\n\n"
                f"✨ *Розваги:*\n{ents_list}\n"
                f"✨ *Обрані програми:*\n{birthday_items}\n"

                f"━━━━━━━━━━━━━━━━━━\n"
                f"📞 *Телефон:* {user.get('phone')}\n" 
            )

            bot.send_message(chat_id, text, parse_mode="Markdown", reply_markup=confirm_kb())



    @bot.message_handler(func=lambda m: m.text == "✅ Підтвердити")
    def confirm(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        user = user_data[chat_id]
        
        try:
            booking(chat_id, user_data)
        except Exception as e:
            print(f"Помилка бази даних: {e}")

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)
        
        status = (
            "📞 Менеджер скоро зв’яжеться для уточнення деталей ✨" 
            if is_working_hours() else 
            "🌙 Заявка додана! Менеджер відповість зранку ✨"
        )
        
        bot.send_message(
            chat_id, 
            f"🎉 *Заявка успішно створена!*\n{status}", 
            parse_mode="Markdown", 
            reply_markup=main_menu_kb()
        )
        
        user["preferences"] = []





    @bot.message_handler(func=lambda m: m.text == "❌ Скасувати")
    def confirm(message):
        chat_id = message.chat.id
        ensure_user(user_data, chat_id)
        user = user_data[chat_id]
        
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        text = (
            "❌ Заявку скасовано, але нічого, давай повернемося на головне меню і подивимось ще раз ✨" 
        )
        
        bot.send_message(
            chat_id, 
            text, 
            parse_mode="Markdown", 
            reply_markup=main_menu_kb()
        )
        
        user["preferences"] = []




    @bot.message_handler(func=lambda m: m.text == "Назад")
    def back_handler(message):

        chat_id = message.chat.id

        previous_step = go_back(user_data, chat_id)

        if not previous_step:
            bot.send_message(
                chat_id,
                "Ти вже в головному меню",
                reply_markup=main_menu_kb()
            )
            return

        render_step(bot, user_data, chat_id, previous_step)


    @bot.message_handler(func=lambda m: m.text == "Скинути")
    def reset(message):

        chat_id = message.chat.id

        reset_user(user_data, chat_id)

        bot.send_chat_action(chat_id, 'typing')
        time.sleep(1)

        bot.send_message(
            chat_id,
            "🔄 Дані очищено!\n\n"
            "🎢 Обери парк заново 👇",
            reply_markup=parks_kb()
        )

