#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""Example project."""

from brain_games.cli import welcome_user

from pprint import pprint


def welcome():
    """Doc string."""
    pprint('Welcome to the Brain Games!')


def main():
    """Doc string."""
    welcome()
    welcome_user()


if __name__ == '__main__':
    main()
