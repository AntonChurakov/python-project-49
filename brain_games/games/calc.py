from random import randint
import random
RULES_OF_GAME = 'What is the result of the expression?'


def generate_question_and_answer():
    number_random_range = 25
    operators = ["+", "-", "*"]
    first_operand = randint(1, number_random_range)
    second_operand = randint(1, number_random_range)
    math_operator = random.choice(operators)

    question = f'{first_operand} {math_operator} {second_operand}'
    if math_operator == '+':
        correct_answer = first_operand + second_operand
    elif math_operator == '-':
        correct_answer = first_operand - second_operand
    elif math_operator == '*':
        correct_answer = first_operand * second_operand
    return question, str(correct_answer)
