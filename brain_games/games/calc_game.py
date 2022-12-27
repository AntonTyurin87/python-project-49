#!/usr/bin/env python3
import random
import prompt


def rules():
    print('''What is the result of the expression?''')


def arifmetic(arithmetic_sign):
    if arithmetic_sign == '+':
        correct_ans = number_1 + number_2
    elif arithmetic_sign == '-':
        correct_ans = number_1 - number_2
    elif arithmetic_sign == '*':
        correct_ans = number_1 * number_2

    return correct_ans


# The functionality of the game "Calc-Game"
def calc_game():
    global number_1, number_2, arithmetic_sign
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    arithmetic_sign = random.choice(['+', '-', '*'])

    print(f'Question: {number_1} {arithmetic_sign} {number_2}')
    your_ans = prompt.string('Your answer: ')

    if (your_ans[0] == '-' and your_ans[1::].isdigit()) or your_ans.isdigit():
        your_ans = int(your_ans)

    return your_ans, arifmetic(arithmetic_sign)
