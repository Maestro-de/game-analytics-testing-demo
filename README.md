# Game Analytics Testing Demo

Пет-проект по автоматизации тестирования игровых метрик на **Python + SQLite + Pytest**.

Демонстрирует навыки: разработка автотестов с нуля, поддержка и обновление тестов, анализ результатов, работа с БД, Git, CI/CD.

### Что тестируется
Модуль `game_analytics.py` — система логирования игровых событий:
- `purchase` — покупки с подсчетом выручки
- `level_complete` — прохождения уровней  
- `death` — смерти игроков

Функции:
- `init_db()` — создание таблицы событий
- `log_event(user_id, event_type, event_data, amount)` — логирование
- `count_events(user_id, event_type)` — подсчет событий
- `total_revenue(user_id)` — подсчет общей выручки

### Стек
- Python 3.10+
- SQLite
- Pytest
- Git / GitHub / GitHub Actions (CI/CD)

### Как запустить локально
```bash
git clone https://github.com/Maestro-de/game-analytics-testing-demo.git
cd game-analytics-testing-demo
pip install -r requirements.txt
pytest -v
