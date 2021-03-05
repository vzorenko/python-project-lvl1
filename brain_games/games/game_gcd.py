#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
import prompt
import random

import math


def game(max_steps=3):
    pprint('Find the greatest common divisor of given numbers.')
    cur_step = 0
    while True:
        cur_step += 1
        cur_number1 = random.randrange(1, 50)
        cur_number2 = random.randrange(1, 50)
        cur_result = math.gcd(cur_number1, cur_number2)

        print("Question: {} {}".format(cur_number1, cur_number2))

        str_answer = prompt.string('Your answer: ')
        try:
            answer = int(str_answer)
        except ValueError:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(str_answer, cur_result))
            return False

        if answer == cur_result:
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'.".format(answer, cur_result))
            return False
