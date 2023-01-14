from random import randint
import math
RULES_OF_GAME = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    number_random_range = 99
    first_number = randint(1, number_random_range)
    second_number = randint(1, number_random_range)
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)
    return question, str(correct_answer)
