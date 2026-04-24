import re
user_credentials = input('Please enter your full name: ')
result = re.fullmatch(r'[А-ЯЇІЄ][а-яїіє]{1,19}\s[А-ЯЇІЄ][а-яїіє]{1,19}\s[А-ЯЇІЄ][а-яїіє]{1,19}', user_credentials)
if result:
    print('Your full name is ' + user_credentials)
    print(result)
else:
    print('Your full name is not valid' )

