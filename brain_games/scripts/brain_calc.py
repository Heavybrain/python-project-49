from brain_games.logic import play_game
from brain_games.games.calc_game import get_question_and_answer
from brain_games.games.calc_game import QUESTION


def main():
    play_game(QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
