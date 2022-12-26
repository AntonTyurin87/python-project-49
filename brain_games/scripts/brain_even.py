#!/usr/bin/env python3
from brain_games.game_launcher import welcome_user, game_launch
from brain_games.games.even_game import rules, even_game


def main():
    name = welcome_user()
    rules()
    game_launch(even_game, name)
    

if __name__ == '__main__':
    main()