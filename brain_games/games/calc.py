from random import randint
import random
number_random_range = 50
operators_list = ["+", "-", "*"]
rules_of_game = 'What is the result of the expression?'


def question():
    first_operand = randint(1, number_random_range)
    second_operand = randint(1, number_random_range)
    math_operator = random.choice(operators_list)
    print(f'Question: {first_operand} {math_operator} {second_operand}')
    result_of_expression = (first_operand)(math_operator)(second_operand)
    return result_of_expression
