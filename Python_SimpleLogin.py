'''
freeCodeCamp - Python and Django 
SHELL
See YouTube: https://youtu.be/jBzwzrDvZ18?t=12318
'''

print('Create account now.')
username = input('Enter username: ')
password = input('Enter password: ')

print('Your account has been created successfully.')

print('\nLogin now')

username2 = input('Enter username: ')
password2 = input('Enter password: ')

if username2 == username and password2 == password: 
    print('You have been logged in.')
else: 
    print('Invalid credentials.')