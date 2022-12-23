#!/usr/bin/env python3
import random
import prompt
import brain_games.acquaintance


# Announcement of game rules
def rules():
    print('''Answer "yes" if the number is even, otherwise answer "no".''')


# The functionality of the game "Even-Game"
def even_game():
    counter = 0

    while counter < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        your_answer = prompt.string('Your answer: ')
        if number % 2 == 0:
            correct_answer = 'yes'
        elif number % 2 != 0:
            correct_answer = 'no'
        if your_answer == correct_answer:
            counter = counter + 1
            print('Correct!')
        else:
            print(f"'{your_answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {brain_games.acquaintance.name}!")
            break
    if counter == 3:
        print(f'Congratulations, {brain_games.acquaintance.name}!')
