from random import randint
import random
import operator
rules_of_game = 'What is the result of the expression?'


def question():
    number_random_range = 25
    operators_list = ["+", "-", "*"]
    first_operand = randint(1, number_random_range)
    second_operand = randint(1, number_random_range)
    math_operator = random.choice(operators_list)
    print(f'Question: {first_operand} {math_operator} {second_operand}')
    if math_operator == '+':
        result = operator.add(first_operand, second_operand)
    elif math_operator == '-':
        result = operator.sub(first_operand, second_operand)
    else:
        result = operator.mul(first_operand, second_operand)
    return str(result)
