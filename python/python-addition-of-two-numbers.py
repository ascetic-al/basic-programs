def addition_of_two_numbers(number1, number2):
    return number1 + number2

user_number1 = float(input('What is the first number in your "addition of two numbers"? '))
user_number2 = float(input('What is the second number in your "addition of two numbers"? '))

sum = addition_of_two_numbers(user_number1, user_number2)

print(user_number1, '+', user_number2, '=', sum)
