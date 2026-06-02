import pytest
import game_analytics as ga

@pytest.fixture(autouse=True)
def clean_db():
    """Recreates a clean database before each test."""
    ga.init_db()
    import sqlite3
    conn = sqlite3.connect(ga.DB_NAME)
    conn.execute("DELETE FROM events")
    conn.commit()
    conn.close()
    yield
    conn = sqlite3.connect(ga.DB_NAME)
    conn.execute("DELETE FROM events")
    conn.commit()
    conn.close()

def test_log_and_count():
    """Checks that an event is logged and counted correctly."""
    ga.log_event("player1", "level_complete", "level_5")
    ga.log_event("player1", "level_complete", "level_5")
    ga.log_event("player1", "death", "boss")

    assert ga.count_events("player1", "level_complete") == 2
    assert ga.count_events("player1", "death") == 1
    assert ga.count_events("player1", "purchase") == 0

def test_revenue_calculation():
    """Checks that total revenue is calculated correctly."""
    ga.log_event("player1", "purchase", "sword", amount=4.99)
    ga.log_event("player1", "purchase", "shield", amount=9.99)
    ga.log_event("player2", "purchase", "potion", amount=2.50)

    assert ga.total_revenue("player1") == pytest.approx(14.98, 0.01)
    assert ga.total_revenue("player2") == 2.50
    assert ga.total_revenue("player3") == 0.0

def test_empty_database():
    """Checks behavior with an empty database."""
    assert ga.count_events("any_user", "any_event") == 0
    assert ga.total_revenue("any_user") == 0.0