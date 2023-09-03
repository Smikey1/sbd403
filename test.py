import bcrypt
import time

# Simulated user data (replace with actual database interactions)
users = {
    "hira1": {
        "password_hash": bcrypt.hashpw(b"Hira@123", bcrypt.gensalt()),
        "failed_attempts": 0,
        "locked_until": 0
    }
}

MAX_FAILED_ATTEMPTS = 5
LOCKOUT_DURATION = 900  # 15 minutes in seconds

def authenticate(username, password):
    if username in users:
        user = users[username]
        if time.time() < user["locked_until"]:
            print("Account locked. Please try again later.")
            return False
        
        if bcrypt.checkpw(password.encode("utf-8"), user["password_hash"]):
            user["failed_attempts"] = 0  # Reset failed attempts
            print("Login successful!")
            return True
        else:
            user["failed_attempts"] += 1
            if user["failed_attempts"] >= MAX_FAILED_ATTEMPTS:
                user["locked_until"] = time.time() + LOCKOUT_DURATION
                print("Account locked due to too many failed attempts.")
            else:
                print("Invalid credentials. Please try again.")
    
    else:
        print("User not found.")
    
    return False

# Test the authentication function
username = input("Please Enter Your Username:").lower()
password = input("Please Enter Your Password:")
authenticate(username, password)
