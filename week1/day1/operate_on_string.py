#!/usr/bin/env python3
"""
operate_on_string.py

Illustrates common string operations.
"""

targetstr = "One,two,THREE,fouR"

print(f'Your original string: {targetstr}')
print('Uppercase:', f'{targetstr.upper()}')
print('Lowercase:', f'{targetstr.lower()}')
print('Space replace comma:', f"{targetstr.replace(',', ' ')}")
