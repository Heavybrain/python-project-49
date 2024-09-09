import sys
import random
from ..cli import welcome_user
from .logic import play_game
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')

# Игра: "Простое ли число?"
#  1. Вывод случайного целого числа на экран
#  2. Пользователь отвечает yes/no
#  3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
#  4. Если ответ верный - следующее число
#  5. Игра до 3 правильных ответов подряд
#  6. Вывод поздравления

# !/usr/bin/env python3


name = welcome_user()
print('Answer "yes" if given number is prime. Otherwise answer "no".')


def is_p(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_correct_answer(rand, us_in):
    if is_p(rand) and us_in == 'yes' or not is_p(rand) and us_in == 'no':
        return 'Correct!'
    elif is_p(rand) and us_in == 'no':
        return f"'{us_in}' is wrong answer;(. Correct answer was 'yes'"
    else:
        return f"'{us_in}' is wrong answer;(. Correct answer was 'no'"


def game_prime():
    play_game(get_correct_answer)



"""     counter = 0
    while counter < 3:
        rand = random.randint(1, 100)
        print(f"Question: {rand}")
        us_in = input("Your answer: ").lower()
        result = get_correct_answer(rand, us_in)
        if result == 'Correct!':
            counter += 1
            print(result)
        else:
            print(result)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!') """
