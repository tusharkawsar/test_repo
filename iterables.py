#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Iterables can be used in a foor loop -> 
list, tuple, set, dictionary, string """

import itertools
droids_list = ['R2-D2', 'TC-16', 'C-3PO']; print(droids_list)
droids_tuple = ('X2-D2', 'TC-16', 'C-3PO'); print(droids_tuple)
droids_set = {'R2-D2', 'TC-16', 'C-3PO'}; print(droids_set)
for (a,b,c) in itertools.zip_longest(droids_list, droids_tuple, droids_set):
    print(a,b,c, "sad") # prints each list in one row if used without itertools
#    break

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
print("Map:")

for x, y in itertools.zip_longest( a, b):
    print (x, y)
    
string ="star wars"
for char in string :
    print(char)
    
episodes = {'Episode I': 'TPM',
            'Episode II': 'AotC',
            'Episode III': 'RotS',
            'Episode IV': 'ANH',
            }
for x,episode in episodes.items():
    print(x,episode)
    
    
""" LESS VISUAL OBJECTS """
interval = range(1,4)
print(interval) # does not print from 1 to 4
for i in interval:
    print(i)

# We only use enumerate when we care about index of an item being explicitely available to us
# Therefore, it is useless to apply enumerate() on Dict and Set
villains = ['Darth Maul', 'Palpatin', 'Darth Vader']
enum_villains = enumerate(villains)
print(enum_villains) # does not print all villain names
for idx,name in enum_villains:
    print(str(idx)+ '-' + name)
#for item in enum_villains: # cannot iterate over items more than one time in ITERATOR
#    print(item) # not ITERABLE
list(enumerate(villains))
set(enumerate(villains))
# String enumerator is useful to return both character and position

""" How to know if we del with an Iterable / Generate Iterator from Iterator"""
interval_iter = iter(interval)
interval_iter # will print an iterator object if the original obejct was iterable
while True:
    try:
        print(next(interval_iter))
    except StopIteration: # if this is not caught, there will be an exception 
        break
    
""" Many iterables are iterators - iter() and next() can be applied """
# Example - enumarete() and finditer() in regexpr.py
# The iterables that can be looped over multiple times have no next() function

""" DATAFRAME """
import pandas as pd
pars = {'weight': [168, 183, 198], 'height': [77,79,135]} # A dict only has names for columns
characters = pd.DataFrame(pars, index=['Luke', 'Han', 'Darth']) # Basically adds names to each row
print(characters)
for item in characters: # Prints only the column names, not data!
    print(item)
result = characters.iterrows()
for index,series in result:
    print(index, series)
result2 = characters.iteritems() # Separate columns and their names
for columnname, Series in result2: # Each column has all rows for that columns and row names/headers
    print('column=',columnname,'\n series=', Series)
