#!/usr/bin/env python3
"""
Testmodule

Small module with some print functions
A module = collection of functions, that you can import into
another program and use

Everything under if __name__=='__main__': is run only
if you run the module as a standalone program
"""
print('Hello there. Thanks for importing me!')

def sayhello(name, msg = 'Hello'):
    print(name, msg)

def saygoodbye(name, msg = 'Goodbye'):
    print(name, msg)


if __name__ = '__main__':
    sayhello('Yin')
    saygoodbye('Yin')