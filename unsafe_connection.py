import tkinter as tk
import sqlite3 as mysql
from tkinter import messagebox

# Function to check if the username exists in the database
def check_username(username):
    database = "test_databse.db"
    try:
        # Connect to the database
        conn = mysql.connect(database)
        cursor = conn.cursor()

        # Create a prepared statement with placeholders to check for the username
        query = "SELECT * FROM user WHERE username = ?"
        
        # Execute the prepared statement with the username as a parameter
        cursor.execute(query, (username,))

        # Fetch the result (safe from SQL injection)
        result = cursor.fetchone()

        conn.close()

        return result is not None  # If result is not None, the username exists
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
        return False

# Function to handle the authentication process
def authenticate():
    # Get the user input from the Entry widgets
    user_typed_username = username_entry.get()
    user_typed_password = password_entry.get()

    # Check if the username exists in the database
    if check_username(user_typed_username):
        try:
            # Connect to the database
            conn = mysql.connect("test_databse.db")
            cursor = conn.cursor()

            # Create a query to authenticate
            query = f"SELECT * FROM user WHERE username = '{user_typed_username}' AND password = '{user_typed_password}' OR '1'='1'"

            # Execute the above query
            cursor.execute(query)

            # Fetch the result (this is vulnerable to SQL injection)
            result = cursor.fetchone()

            if result:
                messagebox.showinfo("Authentication", "Authentication successful")
            else:
                messagebox.showerror("Authentication", "Authentication failed")

            conn.close()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showerror("Authentication", "Username does not exist")

# Create the main window
root = tk.Tk()
root.title("Authentication")

# Set the window dimensions to 200x200 pixels
root.geometry("200x200")

# Create and pack the Username label and Entry widget
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create and pack the Password label and Entry widget
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)  # Passwords are hidden with "*"
# password_entry = tk.Entry(root, show="*")  # Passwords are hidden with "*"
password_entry.pack()

# Create and pack the Authenticate button
authenticate_button = tk.Button(root, text="Authenticate", command=authenticate)
authenticate_button.pack()

# Start the Tkinter main loop
root.mainloop()
