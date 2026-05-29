import sqlite3

DB_NAME = "game.db"

def init_db():
    """Создаёт таблицу игровых событий, если её ещё нет."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            event_type TEXT,
            event_data TEXT,
            amount REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_event(user_id: str, event_type: str, event_data: str = "", amount: float = 0.0):
    """Записывает одно событие в базу."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO events (user_id, event_type, event_data, amount) VALUES (?, ?, ?, ?)",
        (user_id, event_type, event_data, amount)
    )
    conn.commit()
    conn.close()

def count_events(user_id: str, event_type: str) -> int:
    """Считает количество событий конкретного типа для пользователя."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT COUNT(*) FROM events WHERE user_id = ? AND event_type = ?",
        (user_id, event_type)
    )
    count = cursor.fetchone()[0]
    conn.close()
    return count

def total_revenue(user_id: str) -> float:
    """Считает суммарную выручку с покупок пользователя."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT SUM(amount) FROM events WHERE user_id = ? AND event_type = 'purchase'",
        (user_id,)
    )
    total = cursor.fetchone()[0]
    conn.close()
    return total if total is not None else 0.0