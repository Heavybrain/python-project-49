import random
import sys
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')
from ..cli import welcome_user

# Игра: "калькулятор"
# 1. Вывод случайного математического выражения на экран
# 2. Пользователь делает вычисления и вводит ответ
# 3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
# 4. Если ответ верный - следующее число
# 5. Игра до 3 правильных ответов подряд
# 6. Вывод поздравления

#!/usr/bin/env python3


name = welcome_user()
print('What is the result of the expression?')


def generate_expression():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    else:
        result = num1 * num2
    return f"{num1} {operator} {num2}", result


def calculator():
    counter = 0
    while counter < 3:
        expression, true = generate_expression()
        print(f"Question: {expression}")
        user_input = input("Your answer: ")
        if int(user_input) == int(true):
            counter += 1
            print('Correct!')
        else:
            print(f"{user_input} is wrong answer;(. Correct answer was {true}")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
