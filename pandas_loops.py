#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 07:53:13 2020

@author: tushar
"""

import pandas as pd
import numpy as np
brics_df = pd.read_csv('data/brics.csv', index_col=0)
brics_df.columns = brics_df.columns.str.strip()

for item in brics_df:
    # print(item) # Only gives you the columns names
    pass

# 2 ways to PRINT ROWS
for item in brics_df.iterrows():
    # print(item) # a row label and a row Series
    # print(type(item)) # TUPLE containing row index and all other data
    pass
for label, row in brics_df.iterrows():
    # print(label + ": " + str(row))
    # print(label + ": " + row['capital']) # print individual item from row Series
    pass

# 2 ways to ADD NEW COLUMN
# 1) One-liner list comprehension
brics_df['len_listcompr'] = [len(row['country'].strip()) 
                             for label, row in brics_df.iterrows()]

''' For the above line. we do not need to use row['country'].str 
because we are only accessing individual elements from a row 
and the element countryname is already a string. 
STR should be used when we want to make all elements in a 
list/Series str and perform string operations on all of them 
Example: Way 3 below '''
# print(brics_df)

# 2) Using a loop to do the above thing
for label, row in brics_df.iterrows():
    brics_df.loc[label, 'len_loop'] = len(row['country'].strip())
    brics_df.loc[label, 'len_loop'].astype(int)
# print(brics_df)

# 3) apply() method with FUNCTION
# apply() always takes a function, and optionally axis
brics_df['len_apply'] = brics_df['country'].str.strip().apply(len) 

# Example of apply() with METHOD
brics_df['upper_apply'] = brics_df['country'].apply(str.upper) 
# Here str is not needed because we are not stripping whitespace
print(brics_df)





































