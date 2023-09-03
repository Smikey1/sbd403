import sqlite3 as mysql

# Get user input (simulated as user-entered data)
input_username = "user123"
input_password = "' OR '1'='1"
database = "test_databse.db"

# Connect to the database
conn = mysql.connect(database)
cursor = conn.cursor()

# Create a prepared statement with placeholders
query = "SELECT * FROM users WHERE username = ? AND password = ?"

# Execute the prepared statement with user input as parameters
cursor.execute(query, (input_username, input_password))

# Fetch the result (safe from SQL injection)
result = cursor.fetchone()

if result:
    print("Authentication successful")
else:
    print("Authentication failed")

conn.close()