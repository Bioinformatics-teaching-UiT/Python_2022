#!/usr/bin/env python3
"""
simple_cmdline_program.py

This script is a standalone program, and includes what
you need to write your own command-line programs.

It runs the greeter function from the command line.

Run it as: python simple_cmdline_program.py <name>

1. shebang
2. argument parser module
3. if __name__ == '__main__' statement
"""

import argparse # main package to deal with argument parsing

def greeter(name):
    """
    Takes in a name, prints it back out
    :param name: str
    """
    print('Hello', name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Greet the user.")
    parser.add_argument('name',
                        help = 'Name of the user, given as a string',
                        type = str)
    args = parser.parse_args()
    greeter(args.name)