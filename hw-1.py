import re

user_number = input("Enter your phone number without country code: ")
result = re.fullmatch(r'\d{9}', user_number)
if result:
    print(f'Your number: {user_number}')
else:
    print('Your number is not valid')

