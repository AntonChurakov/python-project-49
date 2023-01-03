#!/usr/bin/env python3

from brain_games.brain_engine import launch_game
from brain_games.games import iseven


def main():
    launch_game(iseven)


if __name__ == '__main__':
    main()
