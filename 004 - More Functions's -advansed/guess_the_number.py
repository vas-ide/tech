import random

generate_the_number = random.randint(0, 1000)
def guess_the_number():
    try:
        number = int(input('Input the Number !'))
    except ValueError:
        number = int(input('Input the Number Correctly !'))
    if number == generate_the_number:
        print(f'You vin !!!')
        return True
    elif number < generate_the_number:
        print(f'You number is before the generate number')
    elif number > generate_the_number:
        print(f'You number is after the generate number')

while True:
    print(generate_the_number)
    if guess_the_number() == True:
        break










