#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:31:31 2020

https://learn.datacamp.com/courses/data-manipulation-with-pandas
"""

import pandas as pd
import numpy as np
import pickle
from IPython.display import display, HTML
pd.set_option("display.max_columns", 10)

path_avoplotto = 'data/pandas_datamanipulation/avoplotto.pkl'
path_homeless = 'data/pandas_datamanipulation/homeless_data.pkl'
path_walmart = 'data/pandas_datamanipulation/walmart_sales.pkl'

homelessness = pickle.load(open(path_homeless, 'rb')) # Pickle returns a DF
sales = pickle.load(open(path_walmart, 'rb'))


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


''' Summary Statistics '''
# 1) Basic/Individual Column
# print(homelessness['individuals'].mean())
# print(homelessness['individuals'].median())
# print(homelessness['individuals'].mode()) # NOT SURE what happens
# print(homelessness['individuals'].min()) # Can also do this on DATE column
# print(homelessness['individuals'].var())
# print(homelessness['individuals'].std())
# print(homelessness['individuals'].sum())
# print(homelessness['individuals'].quantile(0.6)) # need PARAMETER
# print(homelessness[['individuals', 'state_pop']].mean()) # MULTIPLE columns

# 2) Cumulative
# print(homelessness['individuals'].cumsum()) # First, First+Second, First+Second+Third ...
# print(homelessness['individuals'].cumprod())
# print(homelessness['individuals'].cummax(axis=0))
# print(homelessness[['individuals', 'state_pop']].cummax(axis=0)) # Each cell is populated with the maximum value seen so far.

# 3) Aggregate
# print(homelessness['individuals'].agg(np.mean)) # ONLY MEAN does not work, because mean is not a function but a method
# print(homelessness[['individuals', 'state_pop']].agg(np.mean)) # multiple COLUMNS
# print(homelessness['individuals'].agg([np.mean, np.median])) # multiple FUNCTIONS
# print(homelessness[['individuals', 'state_pop']].agg([np.mean, np.median])) # Output is 2D

# print(sales['weekly_sales'].mean(), sales['weekly_sales'].median()) # Relation between median and mean can tell us something. 
# E.g. if median is much lower than mean, this means there are a handful of very high sales that is dragging mean forward
# print(sales['date'].max(), sales['date'].min()) # The date range


''' Counting '''
# print(sales)
# print(sales.drop_duplicates(subset="type")) # TEMPORARY change
# print(sales.drop_duplicates(subset="store")[['store', 'type', 'department']])

# Only drops DUPLICATE DEPARTMENTS-STORE pairs, then prints bottom 30 in sorted fashion
# print(sales.drop_duplicates(subset=['store', 'department']).tail(30).sort_values(['store','department'], ascending=[True, True])[['store', 'type', 'department']]) 
unique_dept = sales.drop_duplicates(subset=['store', 'department'])
print(unique_dept['department'].value_counts().reset_index().sort_values('index')) # value_counts() does NOT WORK on df, only on column
''' reset_index() stores the previous index into a new column called 'index' '''




















# print(sales)
# print(sales.groupby('type').count()[['store']])
# print(sales.groupby('store').count())

# df.drop

















