from random import randint
import math

RULES_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_question_and_answer():
    number_from_question = randint(1, 99)
    question = f'{number_from_question}'
    if is_prime(number_from_question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def is_prime(number_from_question):
    if number_from_question < 2:
        return False
    number_sqrt = int(math.sqrt(number_from_question))
    divisors = range(2, (number_sqrt + 1))
    for element in divisors:
        if number_from_question % element == 0:
            return False
    return True
