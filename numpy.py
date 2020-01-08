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
char_array = np.array([i for i in range(1,6)], dtype = np.dtype(str))
print(char_array.dtype)