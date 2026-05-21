# Login System with brute force protection
import time

users = {
    "tavishi": "Secure@123",
    "admin": "Admin@456"
}

def login(username, password):
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        if username in users and users[username] == password:
            print("Access granted. Welcome", username)
            return
        else:
            attempts += 1
            remaining = max_attempts - attempts
            print(f"Wrong credentials. {remaining} attempts remaining.")
            time.sleep(2)

    print("Account locked. Too many failed attempts.")

username = input("Enter username: ")
password = input("Enter password: ")
login(username, password)