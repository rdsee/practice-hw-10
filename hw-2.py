import re

user_number = input("Enter a number: ")
result = re.fullmatch(r'\+?\d{10,12}', user_number)
if result:
    print(f'Your number: {user_number}')
else:
    print('Your number is not valid')

