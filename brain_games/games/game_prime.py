#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
import prompt
import random


def is_prime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def game(max_steps=3):
    pprint('Answer "yes" if given number is prime. Otherwise answer "no".')
    cur_step = 0
    while True:
        cur_step += 1
        cur_number = random.randrange(1, 3572)
        cur_result = is_prime(cur_number)
        cur_result_txt = 'yes' if cur_result else 'no'

        print("Question:", cur_number)
        answer = prompt.string('Your answer: ')

        if ((answer == 'yes') & cur_result) | ((answer == 'no') & (not cur_result)):
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, cur_result_txt))
            return False
