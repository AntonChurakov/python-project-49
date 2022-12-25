#!/usr/bin/env python3

from brain_games.brain_engine import welcome_user
from brain_games.brain_engine import name_of_gamer
from brain_games.brain_engine import question
from brain_games.brain_engine import answer


def main():
    welcome_user()
    gamer_name = name_of_gamer()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    quantity_of_correct_answers = 3
    counter = 0

    for _ in range(quantity_of_correct_answers):
        question_for_gamer = question()
        correct_answer = question_for_gamer % 2 == 0 and 'yes' or 'no'
        gamer_answer = answer()
        if gamer_answer == correct_answer:
            print('Correct!')
            counter += 1
        else:
            print(f"'{gamer_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {gamer_name}!")
            return
    if counter == 3:
        print(f'Congratulations, {gamer_name}!')


if __name__ == '__main__':
    main()
