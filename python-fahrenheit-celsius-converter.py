# A program that asks whether the user wants to convert 
# degrees Fahrenheit to Celsius or the other way around.
# Then it performs the conversion and prints the result.

choice = int(input('If you want to convert degrees Fahrenheit to Celsius, input 0. Otherwise input 1.'))

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
