import sqlite3

c = sqlite3.connect('test.db')
cur = c.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY,
    name TEXT,
    company TEXT,
    size TEXT,
    ratting INTEGER,
    gametype TEXT
)''')
c.commit()
c.close()
