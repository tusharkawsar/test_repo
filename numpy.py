#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
num_array = np.array([i for i in range (1,6)])
# print(num_array) # when you print it, there is NO COMMA
# print([i for i in range(1,6)]) # this one HAS COMMA
num_array[3:] = [40,50] 

""" NumPy arrays are optimized for high efficiency computation
1) All data of same type - print(num_array.dtype) - an ATTRIBUTE. 
ValueError if you want to place different data type.
"""
char_array = np.array([i for i in range(1,126)], dtype = np.dtype(str))
# Datatype is U1/U2/U3/... for str, meaning Unicode string of length 1/2/3
# dtype can also be int/float/bool
# print(char_array.dtype)

np_height = np.array([1, 2, 3, 4, 5])
np_weight = np.array([10, 20, 30, 40, 80])
BMI = np_weight / np_height**2
# BMI = np_weight / np_height**2
# print(BMI) # The spacing is consistent for all items, so I may see gaps
# print(type(BMI), BMI.dtype) # <class 'numpy.ndarray'> float64

# 2D Numpy Array
measurement = np.array([np_height, np_weight])
# print(measurement, type(measurement))


for val in measurement:
    print(val) # prints two arrays
    pass
for val in np.nditer(measurement):
    print(val) # prints all individual items
    pass