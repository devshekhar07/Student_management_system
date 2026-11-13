
import sqlite3

# Connect to database
conn = sqlite3.connect("student.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    marks REAL,
    attendance INTEGER
)
""")

# Main program
while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Show Marks Statistics")
    print("4. Show Attendance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = float(input("Enter marks: "))
        attendance = int(input("Enter attendance: "))

        cursor.execute(
            "INSERT INTO students (name, marks, attendance) VALUES (?, ?, ?)",
            (name, marks, attendance)
        )
        conn.commit()
        print("Student added successfully!")

    elif choice == "2":
        cursor.execute("SELECT * FROM students")
        for student in cursor.fetchall():
            print(student)

    elif choice == "3":
        cursor.execute("SELECT MIN(marks), MAX(marks), AVG(marks) FROM students")
        result = cursor.fetchone()

        if result[0] is None:
            print("No student records found.")
        else:
            print("Minimum Marks:", result[0])
            print("Maximum Marks:", result[1])
            print("Average Marks:", round(result[2], 2))

    elif choice == "4":
        cursor.execute("SELECT name, attendance FROM students")
        for student in cursor.fetchall():
            print(student[0], "-", student[1], "%")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")

conn.close()
