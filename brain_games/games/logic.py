ROUNDS_AMOUNT = 3


def play_game(question, get_question_and_answer):
    print('Welcome to the Brain Games!')
    name = input('May I have your name? ')
    print('Hello, ' + name + '!')
    print(question)
    count = 0
    while count < ROUNDS_AMOUNT:
        new_task, correct_answer = get_question_and_answer()
        print(f'Question: {new_task}')
        answer = input('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            count += 1
        elif answer != correct_answer:
            print(f'\'{answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.'
                  f'\nLet\'s try again, {name}!')
            break
    if count == ROUNDS_AMOUNT:
        print('Congratulations, ' + name + '!')