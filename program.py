import random

print('----------------------------')
print('------GUESS THE NUMBER------')
print('----------------------------')
print()

the_number = random.randint(0, 100)
guess = -1

name = input('What is your name? ')

while guess != the_number:
    guess_text = input('Guess a number between 0 and 100: ')
    guess = int(guess_text)

    if guess < the_number:
        print('Sorry {}, {} is too low.'.format(name, guess))
    elif guess > the_number:
        print('Sorry {}, {} is too high.'.format(name, guess))
    else:
        print('You win, {}! {} Is the right number.'.format(name, guess))

print('Done.')