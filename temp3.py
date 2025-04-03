import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("example.db")

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create 'users' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Create 'orders' table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        product TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
    )
''')

# Insert sample data into 'users'
cursor.executemany('''
    INSERT OR IGNORE INTO users (name, email) VALUES (?, ?)
''', [
    ("Alice Johnson", "alice@example.com"),
    ("Bob Smith", "bob@example.com"),
    ("Charlie Brown", "charlie@example.com")
])

# Insert sample data into 'orders'
cursor.executemany('''
    INSERT INTO orders (user_id, product, quantity, price) VALUES (?, ?, ?, ?)
''', [
    (1, "Laptop", 1, 1200.50),
    (2, "Phone", 2, 650.00),
    (1, "Mouse", 1, 25.99),
    (3, "Keyboard", 1, 45.00)
])

# Commit changes
conn.commit()

# Fetch and display users
print("Users:")
cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

# Fetch and display orders
print("\nOrders:")
cursor.execute("SELECT * FROM orders")
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()

print("\nDatabase populated with sample data.")
