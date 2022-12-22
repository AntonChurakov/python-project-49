#!/usr/bin/env python3

from brain_games.brain_engine import welcome_user
from brain_games.brain_engine import question
from brain_games.brain_engine import answer
from brain_games.brain_engine import is_even
from brain_games.brain_engine import result_of_answer
from brain_games.brain_engine import congrats


def main():
    welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question()
    answer()
    is_even()
    result_of_answer()
    congrats()


if __name__ == '__main__':
    main()
