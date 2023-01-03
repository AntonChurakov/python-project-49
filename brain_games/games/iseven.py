from random import randint

number_random_range = 99
rules_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def question():
    number_from_question = randint(1, number_random_range)
    print(f'Question: {number_from_question}')
    correct_answer = number_from_question % 2 == 0 and 'yes' or 'no'
    return correct_answer
