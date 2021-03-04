#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
import prompt
import random

import math


def game(max_steps=3):
    pprint('What number is missing in the progression?')
    cur_step = 0
    while True:
        random1 = random.randrange(1000)
        random2 = random.randrange(1000)
        cur_start = min(random1, random2)
        cur_end = max(random1, random2)
        cur_steps_count = random.randrange(5, 10)
        cur_step_add = random.randrange((cur_end - cur_start - 1) // cur_steps_count)
        cur_range = random.randrange(cur_start, cur_end, cur_step_add)
        cur_secret_index = random.randrange(cur_steps_count-1)
        cur_secret_value = cur_range[cur_secret_index]
        cur_range[cur_secret_index] = '..'

        print("Question: {}".format(cur_range))

        str_answer = prompt.string('Your answer: ')
        try:
            answer = int(str_answer)
        except ValueError:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(str_answer, cur_secret_value))
            return False

        if answer == cur_secret_value:
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, cur_secret_value))
            return False
