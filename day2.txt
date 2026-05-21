# Password Strength Analyzer
# Checks if a password meets security requirements

import re

def analyze_password(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password must be at least 8 characters")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Add at least one number")

    if re.search(r'[!@#$%^&*]', password):
        strength += 1
    else:
        feedback.append("Add a special character (!@#$%^&*)")

    if strength == 4:
        print("Strong password")
    elif strength == 3:
        print("Medium password")
    else:
        print("Weak password")

    for tip in feedback:
        print(f"  - {tip}")

password = input("Enter a password to analyze: ")
analyze_password(password)