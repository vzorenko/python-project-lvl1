#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from pprint import pprint
import prompt
import operator
import random


def game(max_steps=3):
    pprint('What is the result of the expression?')
    cur_step = 0
    operations = [operator.mul, operator.add, operator.sub]
    while True:
        cur_step += 1
        cur_number1 = random.randrange(1, 10)
        cur_number2 = random.randrange(1, 10)
        cur_operation = random.choice(operations)
        cur_result = cur_operation(cur_number1, cur_number2)
        cur_operation_symbol = ''
        if cur_operation is operator.mul:
            cur_operation_symbol = '*'
        if cur_operation is operator.add:
            cur_operation_symbol = '+'
        if cur_operation is operator.sub:
            cur_operation_symbol = '-'

        print("Question: {} {} {}".format(cur_number1, cur_operation_symbol, cur_number2))

        str_answer = prompt.string('Your answer: ')
        try:
            answer = int(str_answer)
        except ValueError:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(str_answer, cur_result))
            return False

        if answer == cur_result:
            print("Correct!")
            if max_steps <= cur_step:
                return True
            else:
                continue
        else:
            print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(answer, cur_result))
            return False
