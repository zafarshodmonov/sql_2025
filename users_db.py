import sqlite3

# Connect to SQLite database (creates 'users.db' if it doesn't exist)
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create 'users' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    age INTEGER CHECK (age >= 0),
    city TEXT
);
""")

# Insert sample data
users_data = [
    ("aliyev_uz", 25, "Tashkent"),
    ("shodiev_b", 30, "Samarkand"),
    ("murodov_n", 22, "Bukhara"),
    ("kamolova_s", 28, "Fergana"),
    ("rustamov_d", 35, "Khiva")
]

cursor.executemany("INSERT OR IGNORE INTO users (username, age, city) VALUES (?, ?, ?);", users_data)

# Commit changes and close connection
conn.commit()

# Retrieve and print all records
cursor.execute("SELECT * FROM users;")
rows = cursor.fetchall()

print("Users in the database:")
for row in rows:
    print(row)

# Close the database connection
conn.close()
