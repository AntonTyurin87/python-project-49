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
        correct_ans = number_1 + number_2
    elif arithmetic_sign == '-':
        correct_ans = number_1 - number_2
    elif arithmetic_sign == '*':
        correct_ans = number_1 * number_2

    print(f'Question: {number_1} {arithmetic_sign} {number_2}')
    your_ans = prompt.string('Your answer: ')

    if (your_ans[0] == '-' and your_ans[1::].isdigit()) or your_ans.isdigit():
        your_ans = int(your_ans)
    # elif your_ans.isdigit():
        # your_ans = int(your_ans)

    return your_ans, correct_ans
