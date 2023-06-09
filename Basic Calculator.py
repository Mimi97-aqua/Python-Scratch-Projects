name = input('What is your name? ')
welcome_message = f'Hi {name}! What calculation would you like to perform today? \n' \
                  f'A: Addition \n' \
                  f'M: Multiplication \n' \
                  f'D: Division \n' \
                  f'S: Subtraction \n' \
                  f'R: Remainder division \n'
                  f'E: Exponentiation'
print(welcome_message)
calculation= input('Enter letter: ').lower()
number_1 = float(input('First number: '))
number_2 = float(input('Second number: '))
if calculation == 'a':
    print(number_1 + number_2)
elif calculation == 'm':
    print(number_1 * number_2)
elif calculation == 'd':
    print(number_1 / number_2)
elif calculation == 's':
    print(number_1 - number_2)
elif calculation == 'r':
    print(number_1 % number_2)
elif calculation == 'e':
    print(number_1 ** number_2)
else:
    print('Incorrect input')
