from random import randint
length_of_progression = 10
number_random_range = 99
max_common_difference = 10
rules_of_game = 'What number is missing in the progression?'


def question():
    start_element_of_progression = randint(0, number_random_range)
    common_difference = randint(1, max_common_difference)
    list_of_progression = []

    for _ in range(length_of_progression):
        list_of_progression.append(str(start_element_of_progression))
        start_element_of_progression += common_difference

    index_of_hided_element = randint(0, length_of_progression - 1)
    correct_answer = list_of_progression[index_of_hided_element]
    list_of_progression[index_of_hided_element] = '..'
    list_as_string = ' '.join(list_of_progression)
    question = f'{list_as_string}'
    return question, correct_answer
