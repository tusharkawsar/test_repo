#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Iterables can be used in a foor loop -> 
list, tuple, set, dictionary, string """

droids_list = ['R2-D2', 'TC-16', 'C-3PO']; print(droids_list)
droids_tuple = ('X2-D2', 'TC-16', 'C-3PO'); print(droids_tuple)
droids_set = {'R2-D2', 'TC-16', 'C-3PO'}; print(droids_set)
for (a,b,c) in itertools.zip_longest(droids_list, droids_tuple, droids_set):
    print(a,b,c, "sad")
#    break

a = ['a1', 'a2', 'a3']
b = ['b1', 'b2']
print("Map:")
import itertools
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
""" range """
interval = range(1,10)
print(interval)
for i in interval:
    print(i)