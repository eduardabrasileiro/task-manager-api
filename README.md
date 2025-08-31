# Task Manager API (Flask)

Mini API REST para gerenciar tarefas (CRUD) com Flask + SQLite.

## Rotas
- `GET /` — status
- `GET /tasks/` — lista tarefas
- `POST /tasks/` — cria tarefa `{ "title": "..." }`
- `GET /tasks/<id>` — detalhe
- `PUT /tasks/<id>/done` — marca como concluída
- `PUT /tasks/<id>/undone` — desmarca
- `DELETE /tasks/<id>` — remove

## Como rodar
```powershell
py -3 -m venv .venv
& ".\.venv\Scripts\activate.bat"
py -m pip install -r requirements.txt
py app.py
