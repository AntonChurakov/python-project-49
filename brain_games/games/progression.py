from random import randint
length_of_progression = 10
number_random_range = 99
max_common_difference = 10
RULES_OF_GAME = 'What number is missing in the progression?'


def generate_question_and_answer():
    start_element_of_progression = randint(0, number_random_range)
    common_difference = randint(1, max_common_difference)
    progression = []

    for _ in range(length_of_progression):
        progression.append(str(start_element_of_progression))
        start_element_of_progression += common_difference

    index_of_hided_element = randint(0, length_of_progression - 1)
    correct_answer = progression[index_of_hided_element]
    progression[index_of_hided_element] = '..'
    question = f"{' '.join(progression)}"
    return question, correct_answer
