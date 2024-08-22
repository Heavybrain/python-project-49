# Игра: "проверка на четность"
#  1. Вывод случайного целого числа на экран
#  2. Пользователь отвечает yes/no
#  3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
#  4. Если ответ верный - следующее число
#  5. Игра до 3 правильных ответов подряд
#  6. Вывод поздравления

#!/usr/bin/env python3

import random
import sys
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')
from ..cli import welcome_user

name = welcome_user()
print('Answer "yes" if the number is even, otherwise answer "no"')


def game():
    counter = 0
    while counter < 3:
        random_number = random.randint(1,100)
        print(f"Question: {random_number}")
        user_input = input("Your answer: ").lower()
        if  random_number % 2 == 0 and user_input =='yes':
            counter += 1
            print('Correct!')
        elif random_number % 2 != 0 and user_input == 'no':
            counter += 1
            print('Correct!')
        elif random_number % 2 == 0 and user_input == "no":
            print("'no' is wrong answer;(. Correct answer was 'yes'")
            print(f"Let's try again,{name}!")
            return
        elif random_number % 2 != 0 and user_input == "yes":
            print("'yes' is wrong answer;(. Correct answer was 'no'")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations,{name}!')
