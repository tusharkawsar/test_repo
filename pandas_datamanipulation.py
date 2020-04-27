#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:31:31 2020

https://learn.datacamp.com/courses/data-manipulation-with-pandas
"""

import pandas as pd
import pickle
from IPython.display import display, HTML
pd.set_option("display.max_columns", 10)

path_avoplotto = 'data/pandas_datamanipulation/avoplotto.pkl'
path_homeless = 'data/pandas_datamanipulation/homeless_data.pkl'
path_walmart = 'data/pandas_datamanipulation/walmart_sales.pkl'

homelessness = pickle.load(open(path_homeless, 'rb')) # Pickle returns a DF


''' EDA '''
# print(homelessness) # The entire DF
# display(homelessness) # BETTER OUTPUT for IPython
# print(homelessness.head())
# print(homelessness.info())
# print(homelessness.describe()) # STATISTICS: count (non-missing values), mean, max

# 4 Attrbitutes
# print(homelessness.shape)
# print(homelessness.values) # All VALUES in each row
# print(homelessness.columns)
# print(homelessness.index)


''' SORT '''
# print(homelessness.sort_values(['family_members', 'state_pop'], ascending=True))
# Soting on multiple values ONLY MATTERs if 2 values in the first column are the same
# print(homelessness.sort_values('family_members', inplace=True)) # -> IF inplace
# is True, NOTHING is returned
# print(homelessness.head())

# Check sort on multiple columns
# df = pd.DataFrame({1:1, 2:2}, index=[1]) # If values are NOT LIST, index MUST be passed
df = pd.DataFrame({'a':[1,1,1], 'b':[10,10,30], 'c':[100,200,300]})
# print(df)
# print(df.sort_values(['a', 'b', 'c'], ascending=[True, False, False])) 


''' SUBSET:
For column, only write name of column, meaning DF['col']. 
For row, write boolean condition with DF name, meaning DF[DF['col'] > 100]. '''
# 1) COLUMN =========
# print(homelessness['individuals']) # SQUARE brackets
# print(homelessness[['state', 'individuals']]) # Subset MULTIPLE columns
# 2) ROW =========
# print(homelessness[homelessness['individuals'] > 9000])# Subset ROWS
# print(homelessness[homelessness['state'].str.lower() == 'florida'])
# 2.1) Multiple row conditions
# print(homelessness[(homelessness['region']=='Mountain') &   # Parenthesis MANDATORY
#                     (homelessness['individuals']>5000)])
# 2.2) Subset row by CATEGORICAL VARIABLE: Checking if value in a column matches a set of values
# print(homelessness[homelessness['state'].isin(['California', 'Florida'])])
# Below does not properly work for double columns
# print(homelessness[homelessness['state'].isin(['California', 'Florida'])])
# 3) BOTH row and column =========
# print(homelessness.loc[homelessness['state'].str.lower() == 'florida', 
                        # ['region', 'state']]) # BOTH row and column


''' Create New Column '''
homelessness['state-region'] = homelessness['state'].values + ' in ' + homelessness['region']
# del homelessness['individuals']
# del homelessness['family_members']
# display(homelessness.head())
x = homelessness[homelessness['individuals'] > 10000].sort_values('family_members', ascending=True).loc[:, ['state-region', 'individuals', 'state_pop']]
# print(x)



























