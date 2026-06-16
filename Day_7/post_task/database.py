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


