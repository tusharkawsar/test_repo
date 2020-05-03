#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:57:25 2020

@author: tushar
"""
import random

# If a FLOAT is inserted -> ValueError
# n = int(input("Please enter an integer: ")) 
# print(n)

# while True:
#     try:
#         n = input("Please enter an integer: ")
#         n = int(n)
#     except ValueError:
#         print("Not valid! Please try again.")


# dummy_list = [0, 0]
# for i in range(0, 3):
#     try:
#         n = int(input())
#         dummy_list[i] = n
#         print(n, 'inserted at position', i)
#     except IndexError as ie:
#         print('You are trying to insert to list positions that are out of bounds at position', i)
#         print('So, you generated an error called:', ie)
#     except ValueError as ve:
#         print('Value error, please insert integer, not float')


# def func_error():
#     four = int('four')
    
# try:
#     func_error()
# except ValueError:
#     print("Got an error from a function call")


# raise SyntaxError("Sorry, my fault!")
class MyException(Exception):
    pass
# raise MyException("An exception doesn't always prove the rule!")
    
try:
    x = float(input("Your number: "))
    inverse = 1.0 / x
except ValueError:
    print("You should have given either an int or a float")
except ZeroDivisionError:
    print("Infinity")
finally:
    print("There may or may not have been an exception.")














