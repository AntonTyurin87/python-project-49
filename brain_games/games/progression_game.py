#!/usr/bin/env python3
import random
import prompt


def rules():
    print('''What number is missing in the progression?''')


# The functionality of the game "Progression-Game"
def progression_game():
    len_progression = random.randint(5, 11)
    secret_number = random.randint(0, len_progression - 1)
    step_progression = random.randint(1, 10)
    first_term_progression = random.randint(0, 51)

    progression = [str(first_term_progression)]

    for i in range(1, len_progression):
        progression += [str(int(progression[i - 1]) + step_progression)]

    correct_ans = int(progression[secret_number])

    progression[secret_number] = '..'

    print('Question: ' + ' '.join(progression))
    your_ans = prompt.string('Your answer: ')

    if your_ans.isdigit():
        your_ans = int(your_ans)

    return your_ans, correct_ans
