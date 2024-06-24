# A program that asks for a number of which to find factorial,
# then performs the calculation of the factorial
# and prints the result.

num = int(input('Type a number of which you want to find factorial: '))

# A variable to keep track of the number that user input,
# needed for the final print funciton of the program.
# Of course this, as well as the entire program, 
# could be written in a thousand different ways,
# but this is what I did.
saved_num = num

# The 'factorial' variable is needed to keep track of
# the result of the current calculation in the current iteration of the while loop.
# It's initialized to 1, because 0! == 1.
factorial = 1

# The while loop that actually calculates the factorial.
# A humble reminder that 'factorial *= num' here 
# is just shortened form of 'factorial = factorial * num'.
while num > 0:
    factorial *= num
    num -= 1

print ('Factorial of', saved_num, 'is', factorial)
