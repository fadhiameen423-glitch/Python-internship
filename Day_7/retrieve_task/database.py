import sqlite3

def get_connection():
    conn=sqlite3.connect("app.db")
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("""
create table if not exists tasks(
                   id integer primary key autoincrement,
                   title text not null,
                   completed boolean default 0
                   )
                   """)
    conn.commit()
    conn.close()

def db_create_task(task_data):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("insert into tasks(title,completed) values(?,?)",(task_data["title"],task_data["completed"]))
    conn.commit()
    conn.close()
    return {"message":"Task created"}

def db_get_all_task():
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from tasks")
    row=cursor.fetchall()
    conn.close()
    if not row:
        return {"message":"No tasks"}
    return [dict(rows) for rows in row]

def db_get_one(id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("select * from tasks where id= ?",(id,))
    row=cursor.fetchone()
    conn.close()
    if row is None:
        return {"message":"Task not found"}
    return dict(row)