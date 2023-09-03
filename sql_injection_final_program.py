import sqlite3 as mysql


username = input("Please Provide your username:")
password= input("please Provide your password:")
code = int(input("Do you want sql injection (0 -> YES and 1 -> NO): "))

# Get user input (simulated as user-entered data)
user_typed_username = username
user_typed_password = password
database = "test_databse.db"

# Connect to the database
conn = mysql.connect(database)
cursor = conn.cursor()

# Construct a SQL query based upon code
if (code == 0):
    query = f"SELECT * FROM user WHERE username = '{user_typed_username}' AND password = '{user_typed_password}' OR '1'='1'"
    cursor.execute(query)
else:
    # Create a prepared statement with placeholders
    query = "SELECT * FROM user WHERE username = ? AND password = ?"
    # Execute the prepared statement with user input as parameters
    cursor.execute(query, (user_typed_username, user_typed_password))

# Fetch the result (this is vulnerable to SQL injection)
result = cursor.fetchone()

if result:
    print("Authentication successful")
else:
    print("Authentication failed")

conn.close()