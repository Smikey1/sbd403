import sqlite3 as mysql

# Get user input (simulated as user-entered data)
input_username = "user123"
input_password = "' OR '1'='1"
database = "test_databse.db"

# Construct a SQL query (unsafe)
query = f"SELECT * FROM users WHERE username = '{input_username}' AND password = '{input_password}'"

# Connect to the database and execute the query
conn = mysql.connect(database)
cursor = conn.cursor()
cursor.execute(query)

# Fetch the result (this is vulnerable to SQL injection)
result = cursor.fetchone()

if result:
    print("Authentication successful")
else:
    print("Authentication failed")

conn.close()
