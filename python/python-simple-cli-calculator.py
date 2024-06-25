# Define basic operations of the calculator.
def addition (an1, an2):
    return an1 + an2

def subtraction (sn1, sn2):
    return sn1 - sn2

def multiplication (mn1, mn2):
    return mn1 * mn2

def division (dn1, dn2):
    return dn1 / dn2

# Ask the user for input.
operation = input('For addition, input "+" (without the quotation marks). For subtraction, input "-". For multiplication, input "*". For division, input "/"')
if operation not in ('+', '-', '*', '/'):
    print('Wrong input')
    exit()
num1 = float(input('The first number in your calculation: '))
num2 = float(input('The second number in your calculation: '))

# Perform the operation chosen by the user on the numbers that the user has provided.
if operation == '+':
    result = addition(num1, num2)
    print(num1, '+', num2, '=', result)
elif operation == '-':
    result = subtraction(num1, num2)
    print(num1, '-', num2, '=', result)
elif operation == '*':
    result = multiplication(num1, num2)
    print(num1, '*', num2, '=', result)
elif operation == '/':
    result = division(num1, num2)
    print(num1, '/', num2, '=', result)
else:
    print('Wrong input.')