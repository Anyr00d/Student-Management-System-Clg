import sqlite3

# Connect to SQLite database
connection = sqlite3.connect("ffcs.db")  
cursor = connection.cursor()

# Create a table for students
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        rollNumber INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        transport INTEGER NOT NULL,
        cgpa REAL NOT NULL,
        attendance INTEGER NOT NULL
    )
''')

fake_records = [
    (1, 'Alice', 1, 9.5, 90),
    (2, 'Bob', 1, 9.2, 87),
    (3, 'Charlie', 0, 8.9, 82),
    (4, 'David', 1, 8.9, 95),
    (5, 'Emily', 1, 9.2, 87),
    (6, 'Frank', 1, 9.4, 90),
    (7, 'Grace', 1, 8.9, 85),
    (8, 'Harry', 1, 8.9, 82),
    (9, 'Isabella', 1, 9.2, 95),
    (10, 'Jack', 0, 8.9, 80),
    (11, 'Lily', 1, 8.9, 87),
    (12, 'Michael', 1, 9.2, 85),
    (13, 'Olivia', 0, 8.9, 90),
    (14, 'Peter', 1, 8.9, 92),
    (15, 'Rachel', 0, 8.9, 85),
    (16, 'Sarah', 1, 9.2, 87),
    (17, 'Thomas', 0, 8.9, 80),
    (18, 'Victoria', 1, 8.9, 95),
    (19, 'William', 0, 8.9, 82),
    (20, 'Zoe', 1, 9.2, 87)
]

cursor.executemany('''
    INSERT INTO students (rollNumber, name, transport, cgpa, attendance)
    VALUES (?, ?, ?, ?, ?)
''', fake_records)

# Commit the changes and close the connection
connection.commit()
connection.close()