#!/usr/bin/python3
from calculator_1 import add, sub, mul,div
dir()
a = 10
b = 5
'''
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
'''
print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
