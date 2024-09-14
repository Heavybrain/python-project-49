from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(a):
    if a <= 1:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True


def get_question_and_answer():
    number = randint(0, 100)
    if is_prime(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
