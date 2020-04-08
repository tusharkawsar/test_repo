#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" ROW == observation; COLUMN = variable 
2D numpy ararys cannot handle different data types 
Pandas is built on Numpy
"""

import pandas as pd

''' Creating DF - Method 1 '''
my_dict = {'country': ['brazil', 'russia', 'india', 'china', 'south africa'],
        'capital': ['brasilia', 'moscow', 'new delhi', 'beijing', 'pretoria'],
        'area': [1,2,3,4,5],
        'pop':[10,20,30,40,50] }

brics_df = pd.DataFrame(my_dict)
brics_df.index = ['br', 'ru', 'in', 'ch', 'sa']# This index is NOT a function, as in list
# print(brics_df)
# print(brics_df.iloc[0])
# print(brics_df.loc['ch'])
# print(brics_df.loc[brics_df['capital']=='new delhi'])


''' Creating DF - Method 2 '''
print('============================')
# brics_df = pd.read_csv('data/brics.csv') # This will say that the 
# first row header is Unnamed:0
brics_df = pd.read_csv('data/brics.csv', index_col=0)
print(brics_df)
