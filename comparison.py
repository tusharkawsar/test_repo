#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 10:25:09 2020

@author: tushar
"""
import numpy as np

True == 1 # Evaluates to True, similarly False is 0
'pyscript' == 'PyScript' # False

list1 = []
list2 = []
list3 = list1
list1 == list2 # True - values are same
list1 is list2 # False - object ids are not same
list1 == list3 and list1 is list3 # Both True

'abc' > 'bac' # False, since ord('a') < ord('b') [first characters]
'a' > 'b' # False for the reason above
'abc' < 'abcd' # True
'abc' > 'abcd' # False
'abc' == 'abcd' # False: when unequal size, return len(string1) < len(string2)

my_house = np.array([1,2,3,4])
your_house = np.array([4,3,2,1])
my_house > your_house # [F F T T]
np.logical_and(my_house>3, your_house<3) # F F F T
