#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
import prompt
import random


def game(max_steps=3):
    pprint('What number is missing in the progression?')
    cur_step = 0
    while True:
        cur_step += 1
        cur_start = random.randrange(150)
        cur_steps_count = random.randrange(7, 15)
        cur_step_add = random.randrange(1, 10)
        cur_range = \
            list(range(cur_start,
                       cur_start + (cur_step_add * (cur_steps_count + 3)),
                       cur_step_add))
        cur_secret_index = \
            random.randrange(max(0, cur_steps_count - 1))

        cur_secret_value = cur_range[cur_secret_index]
        cur_range[cur_secret_index] = '..'

        print("Question:", ' '.join(str(e) for e in cur_range))

        str_answer = prompt.string('Your answer: ')
        try:
            answer = int(str_answer)
        except ValueError:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'."
                  .format(str_answer, cur_secret_value))
            return False

        if answer == cur_secret_value:
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. "
                  "Correct answer was '{}'."
                  .format(answer, cur_secret_value))
            return False
