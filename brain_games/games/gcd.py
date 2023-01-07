from random import randint
import math
number_random_range = 99
rules_of_game = 'Find the greatest common divisor of given numbers.'


def question():
    first_number = randint(1, number_random_range)
    second_number = randint(1, number_random_range)
    question = f'{first_number} {second_number}'
    correct_answer = math.gcd(first_number, second_number)
    return question, str(correct_answer)
