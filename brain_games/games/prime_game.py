#!/usr/bin/env python3
import random
import prompt


def rules():
    print('''Answer "yes" if given number is prime. Otherwise answer "no".''')


# The functionality of the game "Prime-Game"
def prime_game():
    number = random.randint(1, 100)
    deliver = 2

    while number % deliver != 0:
        deliver += 1

    if number == deliver:
        correct_ans = 'yes'
    else:
        correct_ans = 'no'

    print(f'Question: {number}')
    your_ans = prompt.string('Your answer: ')

    return your_ans, correct_ans
