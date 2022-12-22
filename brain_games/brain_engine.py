#!/usr/bin/env python3

import prompt
from random import randrange


def welcome_user():
    print('Welcome to the Brain Games!')
    global name_of_gamer
    name_of_gamer = prompt.string('May I have your name? ')
    print(f'Hello, {name_of_gamer}!')


number_random_range = 99


def question():
    number_from_question = randrange(number_random_range)
    print(f'Question: {number_from_question}')
    return number_from_question


def answer():
    answer_of_gamer = prompt.string('Your answer: ')
    return answer_of_gamer


def is_even():
    return question() % 2 == 0 and 'yes' or 'no'


def result_of_answer():
    if answer() == is_even():
        print('Correct!')
    else:
        print(f"'{answer()}' is wrong answer ;(. "
              f"Correct answer was '{is_even()}'.")
        print(f"Let's try again, {name_of_gamer}!")


def congrats():
    print(f'Congratulations, {name_of_gamer}!')
