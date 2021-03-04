#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""


from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import wellcome
from pprint import pprint
from random import randrange
import prompt


def welcome_user():
    """Doc string."""
    name = prompt.string('May I have your name? ')
    pprint('Hello, {}!'.format(name))
    return name

def patiry_game():
	name = welcome_user()
	pprint('Answer "yes" if the number is even, otherwise answer "no".')
	max_steps = 3
	cur_step = 0
	while True:
		cur_step += 1
		cur_number = randrange(1, 100)
		is_cur_even = True if cur_number % 2 == 0 else False
		print("Question:", cur_number)
		answer = prompt.string('Your answer: ')
		if ((answer == 'yes') & is_cur_even) |  ((answer != 'yes') & (not is_cur_even)):
			print("Correct!")
			if max_steps <= cur_step:
				print("Congratulations, {}!".format(name))
				break
			else:
				continue
		else:
			print("'{}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {}".format(answer, name))
			break


def main():
    """Doc string."""
    patiry_game()


if __name__ == '__main__':
    main()
