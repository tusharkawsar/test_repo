#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Objcet created by function().yield """
def func():
    yield range(1,5)
    yield 7
    for i in range(0,2):
        yield 'A'
        yield 'B'
result = func()
#for item in result:
#    print(item)
print(list(result))
result = func() # Need to write again since the previous one is exhausted already
print(next(result)) # Eventually leads to StopIteration error

# Generator comprehension
result = (2*i for i in range(0,3)) # Just use round braces instead of square braces
print(result)
print(list(result))

""" Utlity of Generator - 1. creating custom iterable object """
# Difficult to create [1,3,2,4,3,5]
""" 2. Lazy initialization """
# Use of next() prevents anything to be stored in memory
""" 3. Possibility to create infinite iterable onjects with little memory """
# Using while True loop