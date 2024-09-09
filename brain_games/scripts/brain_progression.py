#!/usr/bin/env python3
from brain_games.games.logic import play_game
from brain_games.games.progression_game.py import get_question_and_answer
from brain_games.games.progression_game.py import QUESTION


def main():
    play_game(QUESTION, get_question_and_answer)


if __name__ == '__main__':
    main()
