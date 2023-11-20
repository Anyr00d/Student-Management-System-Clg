import sqlite3

class Student:
    def __init__(self, roll_number, name, transport, cgpa, attendance):
        self.roll_number = roll_number
        self.name = name
        self.transport = transport
        self.cgpa = cgpa
        self.attendance = attendance

# Connect to SQLite database
connection = sqlite3.connect("ffcs.db") 
cursor = connection.cursor()

# Fetch 20 records from the database
cursor.execute("SELECT * FROM students LIMIT 20")  # Replace "students" with your actual table name
rows = cursor.fetchall()

# Create an array of Student objects from the fetched records
students = [Student(roll_number=row[0], name=row[1], transport=row[2], cgpa=row[3], attendance=row[4]) for row in rows]

# Close the database connection
connection.close()


def remove2(a):
    connection = sqlite3.connect("ffcs.db")  # Replace "your_database_name.db" with your actual database name
    cursor = connection.cursor()
    student_name_to_remove = a  # Replace with the actual name you want to remove

    cursor.execute('''
        DELETE FROM students
        WHERE name = ?
    ''', (student_name_to_remove,))
    connection.commit()
    connection.close()
    
# for j in students:
#     remove2(j.name)

# Define the four queues
high_priority_queue = []
medium_priority_queue = []
low_priority_queue = []
lowest_priority_queue = []

# Assign students to the appropriate queues
for student in students:
    if student.cgpa > 9.0:
        high_priority_queue.append(student)
    elif student.cgpa < 9.0 and student.attendance >= 85 and student.transport:
        medium_priority_queue.append(student)
    elif student.cgpa < 9.0 and not student.transport:
        low_priority_queue.append(student)
    else:
        lowest_priority_queue.append(student)

# Simulate the scheduling algorithm
if high_priority_queue or medium_priority_queue or low_priority_queue or lowest_priority_queue:
    # Process high priority queue first
    print("Students in first slot:")
    for i in high_priority_queue:
        print(i.name)

   # Process medium priority queue next
    print("Students in second slot:")
    for i in medium_priority_queue:
        print(i.name)


    # Process low priority queue next
    print("Students in third slot:")
    for i in low_priority_queue:
        print(i.name)


    # Process lowest priority queue last
    print("Students in last slot:")
    for i in lowest_priority_queue:
        print(i.name)