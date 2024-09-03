import random
import sys
sys.path.append('/home/heavybrain/projects/python-project-49/brain_games')
from ..cli import welcome_user

# Игра: "Арифметическая прогрессия"
# 1. Пользователю показывается арифметичкая прогрессия
# 2. Один элемент заменяется двумя точками
# 3. Пользователь должен определить это число
# 4. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
# 5. Если ответ верный - следующая прогрессия
# 5. Игра до 3 правильных ответов подряд
# 6. Вывод поздравления

#!/usr/bin/env python3


name = welcome_user()
print('What number is missing in the progression?')


def prog_game():
    counter = 0
    while counter < 3:
        num1 = random.randint(1,100)
        num2 = random.randint(1,100)
        miss_num = random.randint(0,9)
        progression = []
        prog_number = 0
        while prog_number < 10:
            progression.append(num1+num2)
            prog_number += 1
        return
        progression[miss_num] == '..'
        print(f"Question: {progression}")
        user_input = input("Your answer: ")
        if int(user_input) == int(progression[miss_num]):
            counter += 1
            print('Correct!')
        else:
            print(f"{user_input} is wrong answer;(. Correct answer was {progression[miss_num]}")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

        



        