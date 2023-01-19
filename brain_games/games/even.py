from random import randint

RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    random_number = randint(1, 99)
    question = f'{random_number}'
    correct_answer = random_number % 2 == 0 and 'yes' or 'no'
    return question, correct_answer
