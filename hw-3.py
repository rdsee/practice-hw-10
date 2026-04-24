import re

user_mail = input("Enter your email address: ")
result = re.fullmatch(r'[\w\.\-]{3,20}@gmail\.com', user_mail)
if result:
    print(f'Your mail: {user_mail}')
else:
    print(f'Your mail is not valid!')
