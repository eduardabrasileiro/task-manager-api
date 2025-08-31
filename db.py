import sqlite3
from flask import g, current_app

def get_db():
    if "db" not in g:
        path = current_app.config.get("DATABASE_PATH", "tasks.db")
        g.db = sqlite3.connect(path)
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done INTEGER NOT NULL DEFAULT 0,
                created_at TEXT NOT NULL DEFAULT (datetime('now'))
            )
        """)
        db.commit()
    app.teardown_appcontext(close_db)