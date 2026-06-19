import sqlite3
db_name="sec_task.db"
def get_db_connection():
    conn=sqlite3.connect(db_name)
    conn.row_factory=sqlite3.Row
    return conn

def init_db():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("""create table if not exists users(
                   id integer primary key autoincrement,
                   email text unique not null,
                   hashed_password text not null
                   )""")
    cursor.execute("""
create table if not exists tasks(
                   id integer primary key autoincrement,
                   title text not null,
                   completed bool not null default 0,
                   owner_email text not null,
                   foreign key (owner_email) references users(email)
                   )
                    """)
    conn.commit()
    conn.close()