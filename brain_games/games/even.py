from random import randint

number_random_range = 99
RULES_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_and_answer():
    number_from_question = randint(1, number_random_range)
    question = f'{number_from_question}'
    correct_answer = number_from_question % 2 == 0 and 'yes' or 'no'
    return question, correct_answer
