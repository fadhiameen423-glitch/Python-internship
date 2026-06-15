import sqlite3
db_name="students_db_system.db"

def create_table():
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER,
        name TEXT,
        marks INTEGER
    )
    """)
    conn.commit()
    conn.close()

def insert_student(id, name, marks):
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?)",
        (id, name, marks)
    )
    conn.commit()
    conn.close()
    print("Student added successfully.")


def get_all_students():
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(
        f"Id: {row[0]},"
        f"Name: {row[1]},"
        f"Mark: {row[2]}"
          )

def get_student_by_id(id):
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (id,)
    )
    row = cursor.fetchone()
    conn.close()
    if id not in row:
        print("id not found")
    print(
        f"Id: {row[0]},"
        f"Name: {row[1]},"
        f"Mark: {row[2]}"
          )

def update_marks(id, new_marks):
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE students SET marks = ? WHERE id = ?",
        (new_marks, id)
    )
    conn.commit()
    conn.close()
    print("Marks updated successfully.")

def delete_student(id):
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (id,)
    )
    conn.commit()
    conn.close()
    print("Student deleted successfully.")

def get_students_above(threshold):
    conn = sqlite3.connect("db_name")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM students WHERE marks > ?",
        (threshold,)
    )
    rows = cursor.fetchall()
    conn.close()
    for row in rows:
        print(
        f"Id: {row[0]},"
        f"Name: {row[1]},"
        f"Mark: {row[2]}"
          )

create_table()

while True:
    print("\n===== STUDENT DATABASE SYSTEM =====")
    print("1. Insert Student")
    print("2. View All Students")
    print("3. Get Student By ID")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Students Above Threshold")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        id = int(input("Enter ID: "))
        name = input("Enter Name: ")
        marks = int(input("Enter Marks: "))
        insert_student(id, name, marks)

    elif choice == "2":
        get_all_students()

    elif choice == "3":
        id = int(input("Enter ID: "))
        get_student_by_id(id)

    elif choice == "4":
        id = int(input("Enter ID: "))
        new_marks = int(input("Enter New Marks: "))
        update_marks(id, new_marks)

    elif choice == "5":
        id = int(input("Enter ID: "))
        delete_student(id)

    elif choice == "6":
        threshold = int(input("Enter Threshold Marks: "))
        get_students_above(threshold)

    elif choice == "7":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")