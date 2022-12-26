from brain_games.game_launcher import welcome_user, game_launch
from brain_games.games.calc_game import rules, calc_game


def main():
    name = welcome_user()
    rules()
    game_launch(calc_game, name)


if __name__ == '__main__':
    main()
