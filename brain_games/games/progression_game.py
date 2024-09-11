import random


question = 'What number is missing in the progression?'


def get_question_and_answer():
    start_num = random.randint(1, 100)
    step = random.randint(1, 20)
    miss_num = random.randint(0, 9)
    progression = list(range(start_num, 1000, step))[:10]
    hidden_number = progression[miss_num]
    progression[miss_num] = '..'
    new_task = ' '.join(map(str, progression))
    correct_answer = str(hidden_number)
    return new_task, correct_answer
