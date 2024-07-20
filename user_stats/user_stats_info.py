import sqlite3
conn = sqlite3.connect('user_stats.db')
cursor = conn.cursor()

# Создание таблицы для статистики, если она еще не существует
cursor.execute('''
CREATE TABLE IF NOT EXISTS statistics
(user_id INTEGER PRIMARY KEY,
 games_played INTEGER DEFAULT 0,
 games_won INTEGER DEFAULT 0)
''')
conn.commit()

# Функция для обновления статистики
def update_statistics(user_id, won=False):
    cursor.execute('''
    INSERT OR REPLACE INTO statistics (user_id, games_played, games_won)
    VALUES (?,
            COALESCE((SELECT games_played FROM statistics WHERE user_id = ?) + 1, 1),
            COALESCE((SELECT games_won FROM statistics WHERE user_id = ?), 0) + ?)
    ''', (user_id, user_id, user_id, 1 if won else 0))
    conn.commit()