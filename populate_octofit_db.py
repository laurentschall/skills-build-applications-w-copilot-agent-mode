import sqlite3

# Connect to the octofit_db database
conn = sqlite3.connect('octofit_db.sqlite')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS activities (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL,
    activity TEXT NOT NULL,
    duration INTEGER NOT NULL,
    date TEXT NOT NULL,
    FOREIGN KEY (student_id) REFERENCES students (id)
)
''')

# Insert test data
students = [
    (1, 'Alice Johnson', 10),
    (2, 'Bob Smith', 11),
    (3, 'Charlie Brown', 12)
]

activities = [
    (1, 1, 'Running', 30, '2023-10-01'),
    (2, 1, 'Cycling', 45, '2023-10-02'),
    (3, 2, 'Swimming', 60, '2023-10-01'),
    (4, 3, 'Yoga', 40, '2023-10-03')
]

cursor.executemany('INSERT INTO students (id, name, grade) VALUES (?, ?, ?)', students)
cursor.executemany('INSERT INTO activities (id, student_id, activity, duration, date) VALUES (?, ?, ?, ?, ?)', activities)

# Commit changes and close connection
conn.commit()
conn.close()

print("Test data has been populated into the octofit_db database.")
