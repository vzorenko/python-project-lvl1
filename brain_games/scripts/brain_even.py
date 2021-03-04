#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
from random import randrange
from brain_games.cli import welcome_user, welcome
import prompt


def game(name, max_steps=3):
    pprint('Answer "yes" if the number is even, otherwise answer "no".')
    cur_step = 0
    while True:
        cur_step += 1
        cur_number = randrange(1, 100)
        is_cur_even = True if cur_number % 2 == 0 else False
        print("Question:", cur_number)
        answer = prompt.string('Your answer: ')
        if ((answer == 'yes') & is_cur_even) | ((answer != 'yes') & (not is_cur_even)):
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}".format(answer, name))
            return False


def main():
    """Doc string."""
    welcome()
    name = welcome_user()
    if game(name, 3):
        print("Congratulations, {}!".format(name))


if __name__ == '__main__':
    main()
