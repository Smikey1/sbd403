import sqlite3 as mysql

username = input("Please Provide your username:")
password= input("please Provide your password:")

# Get user input (simulated as user-entered data)
user_typed_username = username
user_typed_password = password
database = "test_databse.db"

# Connect to the database
conn = mysql.connect(database)
cursor = conn.cursor()

# Create a prepared statement with placeholders
query = "SELECT * FROM user WHERE username = ? AND password = ?"

# Execute the prepared statement with user input as parameters
cursor.execute(query, (user_typed_username, user_typed_password))

# Fetch the result (safe from SQL injection)
result = cursor.fetchone()

if result:
    print("Authentication successful")
else:
    print("Authentication failed")

conn.close()