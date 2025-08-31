from typing import Optional, List, Dict
from db import get_db

def fetch_all() -> List[Dict]:
    db = get_db()
    rows = db.execute("SELECT id, title, done, created_at FROM tasks ORDER BY id").fetchall()
    return [dict(r) for r in rows]

def fetch_one(task_id: int) -> Optional[Dict]:
    db = get_db()
    row = db.execute("SELECT id, title, done, created_at FROM tasks WHERE id = ?", (task_id,)).fetchone()
    return dict(row) if row else None

def create(title: str) -> Dict:
    db = get_db()
    cur = db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    db.commit()
    return fetch_one(cur.lastrowid)

def set_done(task_id: int, done: bool) -> Optional[Dict]:
    db = get_db()
    db.execute("UPDATE tasks SET done = ? WHERE id = ?", (1 if done else 0, task_id))
    db.commit()
    return fetch_one(task_id)

def delete(task_id: int) -> bool:
    db = get_db()
    cur = db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return cur.rowcount > 0