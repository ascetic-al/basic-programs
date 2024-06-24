# A program that asks the user for two numbers, one after the other,
# then checks whether the numbers are equal,
# in which case it prints the string "Those numbers are equal". 
# If they aren't equal, it finds the larger number of those two and prints it.

num1 = int(input('First number: '))
num2 = int(input('Second number: '))

if num1 == num2:
    print('Those numbers are equal')
elif num1 > num2:
    print(num1)
else:
    print(num2)
