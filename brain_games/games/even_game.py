#!/usr/bin/env python3
import random
import prompt


def rules():
    print('''Answer "yes" if the number is even, otherwise answer "no".''')


# The functionality of the game "Even-Game"
def even_game():
    number = random.randint(1, 100)
    print(f'Question: {number}')
    your_ans = prompt.string('Your answer: ')

    if number % 2 == 0:
        correct_ans = 'yes'
    elif number % 2 != 0:
        correct_ans = 'no'

    return your_ans, correct_ans
