from telebot import types


def contact_kb():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    button = types.KeyboardButton(text="📱 Надіслати номер телефону", request_contact=True)
    markup.add(button)
    
    return markup

def parks_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🏰 ПАНДОРА")
    kb.row("🌿 ЧАРІВНИЙ ЛІС")
    kb.row("🌌 СВІТ КОМІКСІВ")
    return kb

def info_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("🏰 Про парк")
    kb.row("📍 Адреса", "☎️ Контакти")
    kb.row("🕒 Графік роботи", "🌐 Соцмережі")
    kb.row("🎟 Перейти до бронювання")
    kb.row("🚀 Головне меню")

    return kb

def main_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 День народження", "🟢 Забронювати")
    kb.row("🎢 Розваги", "🧠 План")
    kb.row("💳 Ціни та Тарифи", "📍 Інфо")
    kb.row("Назад", "Скинути")
    return kb


def entertainments_menu():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("📋 Показати всі розваги")
    kb.row("🎯 Підібрати для мене")
    kb.row("⭐ Мої улюблені")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb


def age_choice_book():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🫶 3-5", "🫶 6-8")
    kb.row("🫶 9-12", "🫶 13-16")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb


def age_choice_book_after_amount():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🌟 3-5", "🌟 6-8")
    kb.row("🌟 9-12", "🌟 13-16")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb

def book_ent():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 Забронювати свято")
    kb.row("🔎 Подивитися інші розваги")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb


def choose_entertainment(items):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for item in items:
        kb.row(f"✔️ {item}")
    kb.row("Назад","Скинути")
    return kb

def should_add_favourite():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 Обрати щось інше")
    kb.row("⭐ Додати до свята улюблені розваги")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb


def after_choosing_entertainment():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 Організувати свято з цим")
    kb.row("⭐ Додати в улюблені")
    kb.row("🎢 Просто подивитися інші")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb

def rooms_kb(rooms):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for r in rooms:
        kb.row(f"🏠 {r[1]}")
    kb.row("Назад","Скинути")
    return kb


def times_kb(times):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for t in times:
        kb.row(f"🕐 {t[0]}")
    kb.row("Назад","Скинути")
    return kb


def number_of_children():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("😺 1-5", "😺 5-10")
    kb.row("😺 10-15", "😺 15-20")
    kb.row("😺 20+", "⬅️ Назад")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb


def dates_kb(dates):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for d in dates:
        kb.row(f"📅 {d}")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb


def confirm_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("✅ Підтвердити")
    kb.row("Назад","Скинути")
    kb.row("🚀 Головне меню")
    return kb


def prices_menu():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("💳 Подивитися ціни тарифів")
    kb.row("🎢 Подивитися ціни окремих розваг")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb

def tariffs_menu(tariffs):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    for t in tariffs:
        kb.row(f"💫 {t}")
    kb.row("Назад","Скинути")
    return kb

def after_choosing_tariff():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 Організувати свято з цим тарифом")
    kb.row("💳 Подивитися інші тарифи")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb

def booking_start_kb():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("🎉 Організувати свято")
    kb.row("🎢 Обрати розваги")
    kb.row("⭐ Мої улюблені")
    kb.row("📞 Консультація менеджера")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb

def preferences_kb(preferences):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for ent in preferences:
        kb.row(f"🎢 {ent}")

    kb.row("➕ Додати ще розваги")
    kb.row("✅ Продовжити бронювання")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb


def birthday_items_kb(preferences):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for ent in preferences:
        kb.row(f"🎢 {ent}")

    kb.row("➕ Додати програму")
    kb.row("✅ Продовжити бронювання")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb


def after_adding_favourite():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row("🎉 Забронювати")
    kb.row("🔎 Дивимось ще")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")
    return kb



def birthday_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("🎢 Розваги для свята")
    kb.row("🎉 Організувати свято")
    kb.row("📞 Допомога менеджера")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb


def entertainments_for_birthday_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("🎭 Шоу-програми")
    kb.row("🧪 Майстер-класи")
    kb.row("🗺 Квести")
    kb.row("🎢 Окремі розваги для свята")
    kb.row("📞 Допомога менеджера")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb



def plan_menu_kb():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("👶 Для дітей")
    kb.row("👨‍👩‍👧 Для сім'ї")
    kb.row("🎉 Для свята")
    kb.row("🚀 Головне меню")
    kb.row("Назад","Скинути")

    return kb



def birthday_items_kb(items):

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for item in items:
        kb.row(f"➡️ {item}")

    kb.row("🚀 Головне меню")
    kb.row("Назад", "Скинути")

    return kb


def add_birthday_item_kb():

    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    kb.row("✅ Додати до свята")
    kb.row("🔎 Подивитися інші")
    kb.row("🚀 Головне меню")

    kb.row("Назад", "Скинути")

    return kb