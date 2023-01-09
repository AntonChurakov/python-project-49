#!/usr/bin/env python3

from brain_games.brain_engine import launch
from brain_games.games import gcd


def main():
    launch(gcd)


if __name__ == '__main__':
    main()
