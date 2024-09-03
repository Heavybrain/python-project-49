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


def create_progression():
    start_num = random.randint(1, 100)
    step = random.randint(1, 100)
    miss_num = random.randint(0, 9)

    progression = []
    for i in range(10):
        progression.append(start_num + i * step)

    correct_answer = progression[miss_num]
    progression[miss_num] = '..'

    return progression, correct_answer

def prog_game():
    counter = 0
    while counter < 3:
        progression, correct_answer = create_progression()
        progression_str = ''
        for item in progression:
            progression_str += str(item) + ' '
        print(f"Question: {progression_str}")
        user_input = input("Your answer: ")
        if int(user_input) == correct_answer:
            counter += 1
            print('Correct!')
        else:
            print(f"{user_input} is wrong answer;(. Correct answer was {correct_answer}")
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

        



        