#!/usr/bin/env python3
from brain_games.logic import play_game
from brain_games.games.prime_game import get_question_and_answer
from brain_games.games.prime_game import question


def main():
    play_game(question, get_question_and_answer)


if __name__ == '__main__':
    main()
