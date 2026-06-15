import sqlite3
students = [
    ("Shyam",50),
    ("Aber",70),
    ("Sathyan",90),
    ("Ayas",100),
    ("Gautham",95)
]
conn=sqlite3.connect("student_grtr_70.db")
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
cursor.execute("select * from students where mark > ?",(70,))
rows=cursor.fetchall()
for name,mark in rows:
    print(f"Name: {name}, Mark: {mark}")
conn.close()