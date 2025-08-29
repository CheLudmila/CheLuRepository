from db import get_connection, create_table

# створює таблицю users, якщо ще немає
create_table()

def insert_user(name, age):
    """Додає нового користувача в базу."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, name, age):
    """Оновлює дані користувача за його id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    """Видаляє користувача за id."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    """Повертає список усіх користувачів з бази."""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users