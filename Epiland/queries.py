from Epiland.db import get_connection


def get_entertainments(park_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM entertainments
        WHERE park_id = ?
    """, (park_id,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_tariffs(park_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM tariffs_packages
        WHERE park_id = ?
    """, (park_id,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_entertainments_by_age(park_id, age):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM entertainments
        WHERE park_id = ?
        AND age_min <= ?
        AND age_max >= ?
    """, (park_id, age, age))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_random_entertainments_by_age(park_id, age, limit=3):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT TOP {limit} name
        FROM entertainments
        WHERE park_id = ?
        AND age_min <= ?
        AND age_max >= ?
        ORDER BY NEWID()
    """, (park_id, age, age))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_entertainment_details(park_id, name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT description,
               age_min,
               age_max,
               price_unit_weekday,
               price_unit_weekend,
               unit_details
        FROM entertainments
        WHERE park_id = ?
        AND name = ?
    """, (park_id, name))

    row = cursor.fetchone()

    conn.close()

    return row


def get_tariff_details(park_id, name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT description,
               duration,
               price_weekday,
               price_weekend
        FROM tariffs_packages
        WHERE park_id = ?
        AND name = ?
    """, (park_id, name))

    row = cursor.fetchone()

    conn.close()

    return row


def get_rooms(park_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM rooms
        WHERE park_id = ?
    """, (park_id,))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_room_details(room_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name,
               theme,
               capacity,
               age_min,
               age_max,
               description
        FROM rooms
        WHERE id = ?
    """, (room_id,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_available_times(room_id, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT time
        FROM time_slots
        WHERE room_id = ?
        AND date = ?
        AND is_available = 1
    """, (room_id, date))

    rows = cursor.fetchall()

    conn.close()

    return rows


def get_available_dates(room_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT date
        FROM time_slots
        WHERE room_id = ?
        AND is_available = 1
        ORDER BY date
    """, (room_id,))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_park_info(park_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name,
               city,
               description,
               contacts,
               address,
               working_hours,
               social_media
        FROM parks
        WHERE id = ?
    """, (park_id,))

    row = cursor.fetchone()

    conn.close()

    return row


def get_rooms_by_age(park_id, age):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, name
        FROM rooms
        WHERE park_id = ?
        AND age_min <= ?
        AND age_max >= ?
    """, (park_id, age, age))

    rows = cursor.fetchall()

    conn.close()

    return rows


def booking(chat_id, user_data):

    user = user_data[chat_id]

    conn = get_connection()
    cursor = conn.cursor()

    ents_string = ", ".join(
        user.get("selected_entertainments", [])
    )

    cursor.execute("""
        INSERT INTO bookings (
            chat_id,
            park_id,
            room_id,
            children_count,
            age,
            date,
            time,
            phone,
            entertainments
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        chat_id,
        user.get("park_id"),
        user.get("room_id"),
        user.get("children"),
        user.get("age"),
        user.get("date"),
        user.get("time"),
        user.get("phone"),
        ents_string
    ))

    conn.commit()

    conn.close()


def get_birthday_items_by_category(park_id, category):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT name
        FROM birthday_items
        WHERE park_id = ?
        AND category = ?
    """, (park_id, category))

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def get_birthday_item_details(name):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category,
               price,
               age_min,
               age_max,
               description
        FROM birthday_items
        WHERE name = ?
    """, (name,))

    row = cursor.fetchone()

    conn.close()

    return row