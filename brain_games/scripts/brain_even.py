#!/usr/bin/env python3

from brain_games.brain_engine import welcome_user
from brain_games.brain_engine import name_of_gamer
from brain_games.brain_engine import question
from brain_games.brain_engine import answer
from brain_games.brain_engine import is_even
from brain_games.brain_engine import congrats


def main():
    welcome_user()
    name_of_gamer()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    quantity_of_correct_answers = 3

    while counter < quantity_of_correct_answers:
        question()
        answer()
        is_even()
        if answer() == is_even():
            print('Correct!')
            counter += 1
        else:
            print(f"'{answer()}' is wrong answer ;(. "
                  f"Correct answer was '{is_even()}'."
                  f"Let's try again, {name_of_gamer}!")
    if counter == 3:
        congrats()


if __name__ == '__main__':
    main()
