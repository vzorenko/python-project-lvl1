#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from brain_games.cli import welcome_user, welcome
from brain_games.games.game_even import game


def main():
    """Doc string."""
    welcome()
    name = welcome_user()
    if game(3):
        print("Congratulations, {}!".format(name))
    else:
        print("Let's try again, {}!".format(name))


if __name__ == '__main__':
    main()
