import random
play = input('Press y to roll, Press n to exit')

response = 'y'

while response == 'y':
    no = random.randint(1,6)
    if no == 1:
        print('You rolled a 1')
    elif no == 2:
        print("You rolled a 2")
    elif no == 3:
        print("You rolled a 3")
    elif no == 4:
        print("You rolled a 4")
    elif no == 5:
        print("You rolled a 5")
    elif no == 6:
        print("You rolled a 6")