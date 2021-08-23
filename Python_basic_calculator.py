'''
freeCodeCamp - Python and Django 
BUILDING A BASIC CALCULATOR
See YouTube: https://youtu.be/jBzwzrDvZ18?t=9458

'''

# try .. except .. statement



# simple calculator
# exit by typing q as operator
while 1==1:
    try:
        num1 = int(input('Enter first number: '))
        num2 = int(input('Enter second number: '))
    except ValueError:
        print('Please enter numbers.')
    else:
        op = input('Enter operator (+, -, *, /) or type q to quit: ')

        if op == '+': 
            print(num1, num2, op, '=>', num1+num2)
        elif op == '-':
            print(num1, num2, op, '=>', num1-num2)
        elif op == '*':
            print(num1, num2, op, '=>', num1*num2)
        elif op == '/':
            print(num1, num2, op, '=>', num1/num2)
        elif op == 'q':
            break
        else:
            print('Invalid operator.')
    finally:
        print('=============================')

