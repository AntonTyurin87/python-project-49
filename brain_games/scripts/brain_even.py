#!/usr/bin/env python3
from brain_games.acquaintance import welcome_user
from brain_games.games.even_game import rules
from brain_games.games.even_game import even_game


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    rules()
    even_game()


if __name__ == '__main__':
    main()
