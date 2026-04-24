import re

user_password = input("Enter your password: ")
result = re.fullmatch(r'(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{8,16}', user_password)
if result:
    print(f"Password: {user_password}")
    print(result)
else:
    print("Password is not valid!")
