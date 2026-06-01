# File integrity checker
# Detects if files have been tampered with
# Used in intrusion detection systems

import hashlib
import os

def hash_file(filename):
    sha256 = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

def check_integrity(files):
    print("=" * 50)
    print("FILE INTEGRITY CHECKER")
    print("=" * 50)
    
    for file in files:
        hash_value = hash_file(file)
        if hash_value:
            print(f"\nFile: {file}")
            print(f"SHA256: {hash_value}")
        else:
            print(f"\nFile: {file} - NOT FOUND")

files_to_check = ["day2.py", "day3.py", "day4.py", "day5.py", "day6.py", "day7.py"]
check_integrity(files_to_check)