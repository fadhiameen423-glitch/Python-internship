import sqlite3
students = [
    ("Shyam",50),
    ("Aber",70),
    ("Sathyan",90),
    ("Ayas",100),
    ("Gautham",95)
]
conn=sqlite3.connect("student_dlt.db")
cursor=conn.cursor()
cursor.execute("""
               create table if not exists students(
               name text,
               mark integer
               )
               """)

for student in students:
    cursor.execute("insert into students values(?,?)",student)

conn.commit()
cursor.execute("delete from students where name = ?",("Shyam",))
conn.commit()
cursor.execute("select * from students")
rows=cursor.fetchall()
for name,mark in rows:
    print(f"Name: {name}, Mark: {mark}")
conn.close()