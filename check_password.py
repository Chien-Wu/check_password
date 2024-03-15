#Following are the criteria for checking the password:
#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12

import re

while True:
    pw = input("Create a password: ")
    if pw.lower() == "q":
        break
    
    if len(pw) < 6 or len(pw) > 12:
        print("Password length should be between 6 and 12 characters.")
        continue

    if not re.search("[a-z]", pw):
        print("Use at least one lowercase letter.")
        continue

    if not re.search("[0-9]", pw):
        print("Use at least one digit.")
        continue

    if not re.search("[A-Z]", pw):
        print("Use at least one uppercase letter.")
        continue

    if not re.search("[$#@]", pw):
        print("Use at least one of $#@.")
        continue

    print("Password is legal.")
    break
    

