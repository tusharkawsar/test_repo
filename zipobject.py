#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Zip is an iterable object that can combine several iterable objects. 
Zip contains tuples from original objects, combining items of same indices together.
"""

# 3 iterables in 3 lines
title = 'TMNT'  # If iterables are not the same size, extra elements do not get into a tuple
villains = ['Shredder', 'Krang', 'Bebop', 'Rocksteady']
turtles = {'Raphael':'Sai', 'Michelangelo':'Nunchaku', 
           'Leonardo':'Katana', 'Donatello':'Bo'}
result = zip(title, villains, turtles)
#print(result)
#for item in result:
#    print(item) # Sequence same as that of zipping
#tuples = list(result)
#print(tuples) # If you've already gone through items of result, this list will be empty
# This is because zip object is EXPENDABLE
next(result)
next(result) # StopIteration after 5 calls of next()
print(len(list(result)))

""" UNZIP """
turtle_masks = [('Raphael','red'), ('Michelangelo','orange'),
                ('Leonardo','blue'), ('Donatello','purple')] # This list is in zip style already
#result = zip(turtle_masks) # Just zipped it but the output will be almost same
result = zip(*turtle_masks) # Now the output will be different
# Unzipping separates a list of tuples into two mixed tuples
print(type(result))
for items in result:print (items)
print(result)

""" LIST -> ZIP -> DICT -> DATAFRAME """
keys = ['movie','year','director']
values = [['Forest Gump','Goddfellas','Se7en'],
          [1994,1990,1995],
          ['A','B','C']]
movies = dict(zip(keys,values)) # Without zip, a Dict will not be created from list of Lists
# However, if the list contained tuples, Dict would be created
newdict = dict([(1,2),(3,4)]) 
print(newdict)
# Even three tuples can be made intop a Dict using Zip
newdict = dict([(1,2),(3,4),(5,6)]) 
print(newdict)

print(movies)
for item in movies.items(): # Both print styles work with Dictionary
    print (item)
import pandas as pd
df_movies = pd.DataFrame(movies)
print(df_movies)

""" Zipping a matrix transposes it """ 
mat = [[1,2,3], [4,5,6]]
trans_mat = zip(*mat)
print(tuple(trans_mat))