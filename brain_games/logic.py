import prompt


ROUNDS_AMOUNT = 3


def play_game(question, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    print(question)

    for _ in range(ROUNDS_AMOUNT):
        new_task, correct_answer = get_question_and_answer()
        print(f'Question: {new_task}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
    else:
        print('Congratulations, ' + name + '!')
