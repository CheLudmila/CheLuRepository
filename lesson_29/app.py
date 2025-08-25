from db import get_connection, create_table

create_table()

def insert_user(name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (name, age))
    conn.commit()
    cur.close()
    conn.close()

def update_user(user_id, name, age):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET name=%s, age=%s WHERE id=%s", (name, age, user_id))
    conn.commit()
    cur.close()
    conn.close()

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id=%s", (user_id,))
    conn.commit()
    cur.close()
    conn.close()

def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name, age FROM users")
    users = cur.fetchall()
    cur.close()
    conn.close()
    return users