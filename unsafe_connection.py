import sqlite3 as mysql

username = input("Please Provide your username:")
password= input("please Provide your password:")

# Get user input (simulated as user-entered data)
user_typed_username = username
user_typed_password = password
database = "test_databse.db"

# Construct a SQL query
query = f"SELECT * FROM user WHERE username = '{user_typed_username}' AND password = '{user_typed_password}' OR '1'='1'"

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