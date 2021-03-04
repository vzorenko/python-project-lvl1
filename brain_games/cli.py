# -*- coding:utf-8 -*-

"""Example project."""

import prompt
from pprint import pprint


def welcome_user():
    """Doc string."""
    name = prompt.string('May I have your name? ')
    pprint('Hello, {}!'.format(name))
    return name
