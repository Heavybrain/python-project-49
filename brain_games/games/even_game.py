import random
import sys
from ..cli import welcome_user
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')

# Игра: "проверка на четность"
#  1. Вывод случайного целого числа на экран
#  2. Пользователь отвечает yes/no
#  3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
#  4. Если ответ верный - следующее число
#  5. Игра до 3 правильных ответов подряд
#  6. Вывод поздравления

# !/usr/bin/env python3


name = welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no".')


def is_answer_correct(rand, us_in):
    if rand % 2 == 0 and us_in == 'yes':
        return 'Correct!'
    elif rand % 2 != 0 and us_in == 'no':
        return 'Correct!'
    elif rand % 2 == 0 and us_in == 'no':
        return f"'{us_in}' is wrong answer;(. Correct answer was 'yes"
    else:
        return f"'{us_in}' is wrong answer;(. Correct answer was 'no'"
    


def game():
    counter = 0
    while counter < 3:
        rand = random.randint(1, 100)
        print(f"Question: {rand}")
        us_in = input("Your answer: ").lower()
        result = is_answer_correct(rand, us_in)
        if result == 'Correct!':
            counter += 1
            print(result)
        else:
            print(result)
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
