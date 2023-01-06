from random import randint

number_random_range = 99
rules_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question():
    number_from_question = randint(1, number_random_range)
    print(f'Question: {number_from_question}')

    if number_from_question < 2:
        return 'no'

    divider = 2

    while divider <= number_from_question / 2:
        if number_from_question % divider == 0:
            return 'no'

        divider += 1

    return 'yes'
