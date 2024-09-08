import random
import sys
from ..cli import welcome_user
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


def game_prime():
    counter = 0
    list_numbers = [2, 3, 4, 5, 6, 7, 8, 9]
    while counter < 3:
        random_number = random.randint(1, 100)
        print(f"Question: {random_number}")
        us_in = input("Your answer: ").lower()
        is_div = any(random_number % num == 0 for num in list_numbers)
        if (is_div and us_in == 'no') or (not is_div and us_in == 'yes'):
            counter += 1
            print('Correct!')
        else:
            c_ans = 'no' if is_div else 'yes'
            print(f"'{us_in}' is wrong answer;(. Correct answer was '{c_ans}'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
