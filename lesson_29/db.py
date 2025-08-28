import psycopg2

def get_connection():
    return psycopg2.connect(
        host="postgres_db",  # ім'я контейнера Postgres
        database="testdb",
        user="testuser",
        password="testpass"
    )

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            age INT
        )
    """)
    conn.commit()
    cur.close()
    conn.close()