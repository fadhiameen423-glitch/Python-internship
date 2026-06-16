import sqlite3

def get_connection():
    conn = sqlite3.connect("app.db")
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        completed BOOLEAN DEFAULT 0
    )
    """)
    conn.commit()
    conn.close()

def db_get_all_tasks():
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        "SELECT * FROM tasks"
    )
    rows=cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

def db_get_task(task_id):
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        "SELECT * FROM tasks WHERE id=?",
        (task_id,)
    )
    row=cursor.fetchone()
    conn.close()
    if row is None :
        return None
    return dict(row)

def db_create_task(task_data):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO tasks(title, completed)
        VALUES (?, ?)
        """,
        (
            task_data["title"],
            False
        )
    )
    task_id=cursor.lastrowid
    cursor.execute("select * from tasks where id= ?",(task_id,))
    row=cursor.fetchone()
    conn.commit()
    conn.close()
    return dict(row)

def db_update_task(task_id, task_data):
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET title=?, completed=?
        WHERE id=?
        """,
        (
            task_data["title"],
            task_data["completed"],
            task_id
        )
    )
    conn.commit()
    cursor.execute("select * from tasks where id= ?",(task_id,))
    row=cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)

def db_delete_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM tasks WHERE id=?",
        (task_id,)
    )
    deleted=cursor.rowcount
    conn.commit()
    conn.close()
    return deleted > 0    

def db_complete_task(task_id):
    conn = get_connection()
    cursor=conn.cursor()
    cursor.execute(
        """
        UPDATE tasks
        SET completed=1
        WHERE id=?
        """,
        (task_id,)
    )
    conn.commit()
    cursor.execute("select * from tasks where id= ?",(task_id,))
    row=cursor.fetchone()
    conn.close()
    if row is None:
        return None
    return dict(row)

def db_search_tasks(status):
    conn = get_connection()
    cursor=conn.cursor()
    if status == "completed":
        cursor.execute(
            "SELECT * FROM tasks WHERE completed=1"
        )
        rows=cursor.fetchall()

    elif status == "pending":
        cursor.execute(
            "SELECT * FROM tasks WHERE completed=0"
        )
        rows=cursor.fetchall()

    else:
        cursor.execute(
            "SELECT * FROM tasks"
        )
        rows=cursor.fetchall()

    conn.close()
    return [dict(row) for row in rows]