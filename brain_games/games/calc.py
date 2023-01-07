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

    question = f'{first_operand} {math_operator} {second_operand}'
    if math_operator == '+':
        correct_answer = operator.add(first_operand, second_operand)
    elif math_operator == '-':
        correct_answer = operator.sub(first_operand, second_operand)
    else:
        correct_answer = operator.mul(first_operand, second_operand)
    return question, str(correct_answer)
