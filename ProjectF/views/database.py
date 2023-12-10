import sqlite3

DB_NAME = 'university.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Create University table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS University (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location TEXT NOT NULL
        )
    ''')

    # Create Branch table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Branch (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            university_id INTEGER NOT NULL,
            FOREIGN KEY (university_id) REFERENCES University(id)
        )
    ''')

    conn.commit()
    conn.close()

def execute_query(query, params=()):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, params)
    result = cursor.fetchall()
    conn.commit()
    conn.close()
    return result
