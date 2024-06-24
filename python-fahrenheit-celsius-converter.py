# A program that asks whether the user wants to convert 
# degrees Fahrenheit to Celsius or the other way around.
# Then it performs the conversion and prints the result.

# What I did here could be done in way more elegant ways, but I like the simplicity of it.
# Also a reminder that 0 is a value like any other! (Or is it?)
choice = int(input('If you want to convert degrees Fahrenheit to Celsius, input 0. Otherwise input 1.'))

# Simple if-elif-else is the main part of this program. 
# The program first checks if 'choice' is 0,
# in which case the part below the first conditional, 'if', 
# is the one that the program executes.
# If it isn't 0, it checks again whether it's 1, maybe?
# If it is 1, the program executes the part below the elif conditional.
# If it isn't any of those two, the else part is the one that the program executes.
if choice == 0:
    degrees_fahrenheit = float(input('How many degrees Fahrenheit to convert to Celsius: '))
    converted_fahrenheit = (degrees_fahrenheit - 32) / 1.8
    print (degrees_fahrenheit, 'degrees Fahrenheit equals', converted_fahrenheit, 'degrees Celsius.')
elif choice == 1:
    degrees_celsius = float(input('How many degrees Celsius to convert to Fahrenheit: '))
    converted_celsius = (degrees_celsius * 1.8) + 32
    print (degrees_celsius, 'degrees Celsius equals', converted_celsius, 'degrees Fahrenheit.')
else:
    print ('Wrong input.')
