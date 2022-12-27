#!/usr/bin/env python3
import random
import prompt
import math


def rules():
    print('''Find the greatest common divisor of given numbers.''')


# The functionality of the game "Gcd-Game"
def gcd_game():
    global number_1, number_2, correct_ans
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)

    correct_ans = math.gcd(number_1, number_2)

    print(f'Question: {number_1} {number_2}')
    your_ans = prompt.string('Your answer: ')

    if your_ans.isdigit():
        your_ans = int(your_ans)

    return your_ans, correct_ans
