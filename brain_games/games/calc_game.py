from random import randint
from random import choice
from operator import add
from operator import mul
from operator import sub


RULES = 'What is the result of the expression?'


def get_operation(oper):
    if oper == '+':
        return add
    elif oper == '*':
        return mul
    elif oper == '-':
        return sub
    else:
        raise ValueError("Unexpected operator")


def get_question_and_answer():
    a = randint(1, 100)
    b = randint(1, 100)
    oper = choice('+-*')
    new_task = f'{a} {oper} {b}'
    correct_answer = str(get_operation(oper)(a, b))
    return new_task, correct_answer
