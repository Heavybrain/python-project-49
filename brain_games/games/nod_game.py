import random
import sys
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')
from ..cli import welcome_user

# Игра: "Наибольший общий делитель"
# 1. Пользователю показываются два случайных числа на экран
# 2. Пользователь вычисляет наибольший общий делитель и вводит ответ
# 3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
# 4. Если ответ верный - следующие числа
# 5. Игра до 3 правильных ответов подряд
# 6. Вывод поздравления

#!/usr/bin/env python3


name = welcome_user()
print('Find the greatest common divisor of given numbers.')


def nod(a,b):
    while b != 0:
        a, b = b, a % b
    return a


def nod_counter():
  
    counter = 0
    while counter < 3:
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        print(f"Question: {num1} {num2}")
        user_input = input("Your answer: ")
        if int(user_input) == int(nod(num1, num2)):
            counter += 1
            print('Correct!')
        else:
            print(f"{user_input} is wrong answer;(. Correct answer was {nod(num1, num2)}")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


