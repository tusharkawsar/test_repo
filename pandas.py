#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from clearmodule import clear
# clear()

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


# Strip whitespace from column headers
col = list(brics_df.columns)
col_no_ws = [x.strip() for x in col]
brics_df.columns = col_no_ws
# print(brics_df.columns) 


''' Accessing Data '''

# Select entire column
print(brics_df["capital"]) # The type is object
print(type(brics_df["capital"])) # The type is PD Series
# A series is a 1D labelled array. Multiple series make up a DF

# Double square brackets return a DF object, NOT series
# Basically putting together a list of Series
# Also prints column header(s)
print(brics_df[['capital']])
print(type(brics_df[['capital']]))

# Single square bracket cannot print 2 columns at once. *****
# Double square brackets can
print(brics_df[['country', 'capital']])

# Selecting entire row
print(brics_df[1:4]) # brics_df[1] -> KeyError


''' Square brackets have limited functionality.
Ideally, we want something similar to Numpy 2D arrays. 
LOC -> label-based
ILOC -> position-based '''

# Print Russia row - 4 ways, Different Object Types and Print Types
# 1) Returns a DF, Prints horizontally
print(brics_df[1:2]) 
print(type(brics_df[1:2])) 
# 2) Returns a DF, Prints horizontally
print(brics_df[brics_df.index == 'ru'])
print(brics_df.loc[brics_df.index == 'ru']) # Same as above
print(type(brics_df[brics_df.index == 'ru']))
# 3) Returns a Series, Prints vertically
print(brics_df.loc['ru'])
print(type(brics_df.loc['ru']))
# 4) Returns a DF, Prints horizontally
print(brics_df.loc[['ru']])
print(type(brics_df.loc[['ru']]))

# Select multiple rows - LOC w/ single brackets CANNOT DO THIS *****
print(brics_df.loc[['ru', 'ch']])
# print(brics_df.loc['ru', 'ch']) -> KeyError


''' Select both row and column - NEED TO USE LOC
To select multiple row/column, use DOUBLE BRACKETS'''

print(brics_df.loc['ru']['capital']) # Again, CANNOT select MULTIPLE 
print(type(brics_df.loc['ru']['capital']))
print(brics_df.loc[['ru', 'ch'], ['capital', 'country']])
print(type(brics_df.loc[['ru', 'ch'], ['capital', 'country']]))
# First one returns a string, second one returns a DF

''' Returned DF can be converted into a Numpy Array by using .values '''

# Select only columns - 4 ways
print(brics_df['capital'])
print(type(brics_df['capital'])) # Series, NO multiple
print(brics_df[:]['capital'])
print(type(brics_df[:]['capital'])) # Series, NO multiple
print(brics_df[['capital', 'country']])
print(type(brics_df[['capital', 'country']])) # DF
print(brics_df.loc[:, ['capital', 'country']])
print(type(brics_df.loc[:, ['capital', 'country']])) # DF


''' NumPy vs LOC-> LOC uses row labels, not row indexes 
Use ILOC if you want to select rows based on index'''

# Rows
print(brics_df.loc[['br'], :])
print(brics_df.iloc[[1], :]) # Same result
print(type(brics_df.iloc[[1], :])) # DF
print(brics_df.iloc[[1,2,3], :])
print(brics_df.iloc[range(1,4,1), :])

# If want to use COLON, DON'T put inside a square bracket of its own
print(brics_df.iloc[1:3, :]) 
# print(brics_df.iloc[[1:3], :]) -> SyntaxError

# Columns
print(brics_df.iloc[:, [1,2]])
print(brics_df.iloc[:, 1:3]) # Same


''' Even to print a single value, I should use LOC or ILOC.
Basically, I should almost never use simple square brackets without LOC/ILOC.
LOC without double brackets prints SERIES.
You cannot print a column with LOC without mentioning ROW. 
'''

# Using LOC with single and double brackets
print(brics_df.loc['ru']) # row Series
print(brics_df['capital']) # column Series - but WITHOUT LOC
print(brics_df.loc[['ru'], :]) # row DF
print(brics_df.loc[:, ['capital']]) # column DF

# The following two prints different values
print(brics_df.loc[['br'], ['capital']]) # DF
print(brics_df.loc['br']['capital']) # A single value


''' Printing Row and Column SERIES'''
# 3 Equivalent Ideas to get COLUMN SERIES
print(brics_df['area'])
print(brics_df.loc[:, 'area'])
print(brics_df.iloc[:, 2])
# 3 Equivalent Ideas to get ROW SERIES
print(brics_df[brics_df.index=='ch'])
print(brics_df.loc['ch', :])
print(brics_df.iloc[3, :])


''' Convert data format in Column '''
# Method 1
brics_df.loc[:, 'pop'] = brics_df.loc[:, 'pop'].astype(float)
# Method 2
brics_df.loc[:, 'area'] = pd.to_numeric(brics_df.loc[:, 'area'], errors='coerce')
print(brics_df.info())    
print(brics_df)


# Check Null Values in each column
print(brics_df.isnull().sum())
print(brics_df.isnull().sum().sum())


# Goupby Sum
print(brics_df.groupby('country').mean())
print(brics_df.groupby('country').var())


# Generating random data
from sklearn.datasets import make_blobs
X, y = make_blobs(n_samples=10, centers=5, n_features=3,
               random_state=0)
print(X.shape)
print(X)
print(y)
print(X[y == 0])