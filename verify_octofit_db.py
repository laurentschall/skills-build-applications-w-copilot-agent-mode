import sqlite3

# Connect to the octofit_db database
conn = sqlite3.connect('octofit_db.sqlite')
cursor = conn.cursor()

# Verify students table
print("Students:")
for row in cursor.execute('SELECT * FROM students'):
    print(row)

# Verify activities table
print("\nActivities:")
for row in cursor.execute('SELECT * FROM activities'):
    print(row)

# Close connection
conn.close()
