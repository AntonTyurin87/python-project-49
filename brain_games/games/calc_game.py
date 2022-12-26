import random
import prompt


def rules():
    print('''What is the result of the expression?''')


# The functionality of the game "Even-Game"
def calc_game():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    arithmetic_sign = random.choice(['+', '-', '*'])

    if arithmetic_sign == '+':
        correct_answer = number_1 + number_2
    elif arithmetic_sign == '-':
        correct_answer = number_1 - number_2
    elif arithmetic_sign == '*':
        correct_answer = number_1 * number_2

    print(f'Question: {number_1} {arithmetic_sign} {number_2}')
    your_answer = prompt.string('Your answer: ')

    if your_answer[0] == '-' and your_answer[1::].isdigit():
        your_answer = int(your_answer)
    elif your_answer.isdigit():
        your_answer = int(your_answer)

    return your_answer, correct_answer
