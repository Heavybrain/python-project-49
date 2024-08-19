# Игра: "проверка на четность"
#  1. Вывод случайного целого числа на экран
#  2. Пользователь отвечает yes/no
#  3. Если неверный ответ - игра завершается и выводится сообщение о проигрышше
#  4. Если ответ верный - следующее число
#  5. Игра до 3 правильных ответов подряд
#  6. Вывод поздравления

import random
from cli import welcome_user

print('Answer "yes" if the number is even, otherwise answer "no"')
def game():
    counter = 0
    while counter < 3:
        random_number = random.randint(1,)
        print(f"Question: {random_number}")
        user_input = input("Your answer: ")
        if  random_number % 2 == 0 and user_input == 'yes':
            counter += 1
            print('Correct!')
        elif random_number % 2 != 0 and user_input == 'no':
            counter += 1
            print('Correct!')
        elif random_number % 2 == 0 and user_input == "no":
            print(f"'no' is wrong answer;(. Correct answer was 'yes'\n Let's try again," {name}"!" )
        elif random_number % 2 != 0 and user_input == "yes":
            print(f"'yes' is wrong answer;(. Correct answer was 'no'\n Let's try again," {name}"!")
    print(f'Congratulations, ' {name} '!')

