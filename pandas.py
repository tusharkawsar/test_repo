#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from clearmodule import clear

clear()

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
brics_df.index = ['br', 'ru', 'in', 'ch', 'sa'] # This index is NOT 
# a function, as in list. This index is ROW INDEX.

# print(brics_df)
# print(brics_df.iloc[0])
# print(brics_df.loc['ch'])
# print(brics_df.loc[brics_df['capital']=='new delhi'])


''' Creating DF - Method 2 '''
print('============================')
# brics_df = pd.read_csv('data/brics.csv') # This will say that the 
# first row header is Unnamed:0
brics_df = pd.read_csv('data/brics.csv', index_col=0)

''' Q. index versus index_col for pandas DataFrame?
A. Basically, to set up rows/observations with labels, we do df.index
To set up columns/variables with labels, we pass index_col while 
reading from csv '''

# print(brics_df)


''' Accessing Data '''

# Strip whitespace from column headers
col = list(brics_df.columns)
col_no_ws = [x.strip() for x in col]
brics_df.columns = col_no_ws
# print(brics_df.columns) 

# Select entire column
print(brics_df["capital"]) # The type is object
print(type(brics_df['capital'])) # The type is PD Series
# A series is a 1D labelled array. Multiple series make up a DF

# Double square brackets return a DF object, NOT series
# Basically putting together a list of Series
# Also prints column header(s)
print(brics_df[['capital']])
print(type(brics_df[['capital']]))

# Single square bracket cannot print 2 columns at once.
# Double square brackets can
print(brics_df[['country', 'capital']])


# Selecting entire row
print(brics_df[1:4])


''' Square brackets have limited functionality.
Ideally, we want something similar to Numpy 2D arrays. 
LOC -> label-based
ILOC -> position-based '''

# Print Russia row
print(brics_df[1:2])
print('hello')










































