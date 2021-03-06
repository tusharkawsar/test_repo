#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:31:31 2020

https://learn.datacamp.com/courses/data-manipulation-with-pandas
"""

import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy import stats
from IPython.display import display, HTML
pd.set_option("display.max_columns", 8)

path_avoplotto = 'data/pandas_datamanipulation/avoplotto.pkl'
path_homeless = 'data/pandas_datamanipulation/homeless_data.pkl'
path_walmart = 'data/pandas_datamanipulation/walmart_sales.pkl'

homelessness = pickle.load(open(path_homeless, 'rb')) # Pickle returns a DF
sales = pickle.load(open(path_walmart, 'rb'))
avocados = pickle.load(open(path_avoplotto, 'rb'))


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
# homelessness['state-region'] = homelessness['state'].values + ' in ' + homelessness['region']
# del homelessness['individuals']
# del homelessness['family_members']
# display(homelessness.head())
x = homelessness[homelessness['individuals'] > 10000].sort_values('family_members', ascending=True).loc[:, ['state-region', 'individuals', 'state_pop']]
# print(x)


''' Summary Statistics (no group, all rows) '''
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

# How many different departments in all stores?
unique_dept = sales.drop_duplicates(subset=['store', 'department'])
# print(unique_dept['department'].value_counts(sort=True, normalize=True)) # value_counts() does NOT WORK on df, only on column
# Notice the parameters above: SORT, not sorted
# print(unique_dept['department'].value_counts().reset_index().sort_values('index')) # If we want to sort based on index
''' reset_index() stores the previous index into a new column called 'index' '''


# Q. Count the number of stores of each store type.
# Count the proportion of stores of each store type.
# Count the number of different department numbers, sorting the counts in descending order.
# Count the proportion of different department numbers, sorting the proportions in descending order.
stores = sales.drop_duplicates(subset=['store', 'type']) # No duplicate stores
departments = sales.drop_duplicates(subset=['store', 'department']) # No duplicate dept in a store
store_count = stores['store'].value_counts(sort=True) # How many stores
store_prop = stores['store'].value_counts(normalize=True)
dept_count = departments['department'].value_counts(normalize=True)
dept_prop = departments['department'].value_counts(normalize=True, sort=True) # How many depts across stores



''' Grouped Summary Statistics '''
# Only considers a subset of rows in a column
# print(homelessness[homelessness['region']=='Mountain']['individuals'].mean())
# print(sales[sales['department']==10]['weekly_sales'].mean())
# Can check if one store has better weekly sales than others
# print(sales[sales['store']==20]['weekly_sales'].mean())

# Q. Calculate the total weekly sales over the whole dataset.
# Subset for type "A" stores, and calculate their total weekly sales.
# Do the same for type "B" and type "C" stores.
# Combine the A/B/C results into a list, and divide by overall sales to get the proportion of sales by type.
sales_a = sales[sales['type']=='A']['weekly_sales'].sum()
sales_b = sales[sales['type']=='B']['weekly_sales'].sum()
sales_c = sales[sales['type']=='C']['weekly_sales'].sum()
# print([sales_a, sales_b, sales_c]/sales['weekly_sales'].sum())


# The same can be easily achieved without specifying each store number using GROUPBY
# print(sales.groupby('store')['weekly_sales']) # Only returns a groupby object, need to specify statistical method
# print(sales.groupby('store')['weekly_sales'].mean())
# print(sales.groupby('store')['is_holiday'].mean()) # provides a number for int, float, and BOOLEAN!!
# print(sales.groupby('store').mean()) # Provides group stats summary for all columns if column not specified
# print(sales.groupby('store').agg([min, max, sum, np.mean, np.median, stats.mode]))
# Cannot specify a column in the end, may specify it right after groupby
# sales.groupby('store).mean()['date'] -> INVALID SYNTAX
# print(sales.groupby(['store', 'department']).agg([min]).tail(20)) # groupny on multiple columns

# Q. Group sales by "type", take the sum of "weekly_sales", and store as sales_by_type.
# Calculate the proportion of sales at each store type by dividing by the sum of sales_by_type. Assign to sales_propn_by_type.
sales_by_type = sales.groupby('type')['weekly_sales'].sum()
sales_prop_by_type = sales_by_type/sum(sales_by_type)
# print(sum(sales_by_type))


''' Pivot Tables - df with sorted index '''
# print(sales.groupby('type')['store'].mean())
# print(sales.pivot_table(index='type', values='store')) # Same as above, default is mean()
# print(sales.pivot_table(index=['type','is_holiday'], values='store', aggfunc=np.sum))
# Different look but same result as two indexes below
# print(sales.pivot_table(index='type', columns='department', values='store')) # columns contain the secondary index
# print(sales.pivot_table(index='type', values='is_holiday', columns='store', aggfunc=np.min)) # lots of NaN values
# Fills NaN with ZERO
# print(sales.pivot_table(index='type', values='is_holiday', columns='store', fill_value=0, aggfunc=np.min))
# print(sales.pivot_table(index='type', values='weekly_sales', margins=True, columns='is_holiday', aggfunc=[np.sum, np.mean])) # Last row & column have summary

# Pivot Table Slicing
sales_pivot = sales.pivot_table(index='type', values='weekly_sales', columns='store')
# print(sales_pivot)
# print(sales_pivot.loc['A':'B', 1:3])

# Access only YEAR FROM DATE
# sales['year'] = sales['date'].dt.year
# print(sales)

# Summary with Axis on Pivot Table - makes sense because EVERY COLUMNS HAS SAME DATA TYPE
# print(sales_pivot.mean(axis=0)) # Taking each COLUMN at a time
# print(sales_pivot.mean(axis=1)) # Taking each ROW at a time
# print(sales_pivot.mean(axis='index')) # Same as AXIS=0
# print(sales_pivot.mean(axis='columns')) # Same as AXIS=1


''' Index - makes subsetting code cleaner - index may not be unique - left-aligned'''
# print(sales.set_index('is_holiday')) # does NOT CHANGE the original df
# print(sales.set_index('is_holiday').reset_index())
# print(sales.set_index('is_holiday').reset_index(drop=True)) # GETS RID OF prev index column

# Code EASIER after SETTIGN INDEX
# print(sales[sales['unemployment'].isin([8.106, 8.3])])
x = sales.set_index('unemployment')
# print(x.loc[[8.106, 8.3], :])

# Duplicate indexes
# print(sales.set_index('department').loc[1])

# Multi-level index - second index is nested inside the first one
multi_index_sales = sales.set_index(['type', 'department'])
# print(multi_index_sales)
# print(multi_index_sales.loc[['A'], :])
# print(multi_index_sales.loc[["A"]])
# The command below needs pairing items each from one level of index
# print(multi_index_sales.loc[[('A',98), ('B',9)]])
# Sort will start from outer to inner, ascending
# print(multi_index_sales.sort_index())
# print(multi_index_sales.sort_index(level=['department','type'], ascending=[False,True]))

''' Problems with indexes:
    1) Index values are just data
    2) Violated "tidy data" principle of data getting its own column
'''
multi_index_sales2 = sales.set_index(['type', 'store'])
# print(multi_index_sales)
multi_index_sales2 = multi_index_sales2.sort_index()
# If index not sorted, SLICING WON'T WORK
# print(multi_index_sales2.loc['A':'B']) # Final value INCLUDED
# print(multi_index_sales2.loc[[('B',43), ('B',45)]]) # Tuples do not have colon inside
# print(multi_index_sales2.loc[('B',43) : ('B',45)]) # using COLON needs single square brackets
# print(multi_index_sales2.loc[:, 'department':'weekly_sales']) # COLUMN SLICING

# Date slicing
# print(sales[(sales["date"] >= "2010") & (sales["date"] < "2012")]) # Adjusts for month/day
multi_index_sales3 = sales.set_index('date').sort_index()
# print(multi_index_sales3)
# print(multi_index_sales3.loc['2010-02-05':'2010-02-06'])
# print(multi_index_sales3.loc['2010':'2010']) # PARTIAL dates slicing

''' iloc - final value not included - row & column both needed '''
# print(sales.iloc[1:3, 2:3])


''' Visualization '''
# sales['type'].hist() # sales['store'].hist() or sales['date'].hist()
# sales['date'].hist()

# x = sales.groupby('type')['weekly_sales'].mean() # AGG func in MANDATORY
# print(x)
# x.plot(kind='bar', title='The groupby argument is on X axis vertically')
# sales.plot(x='type', y='unemployment', kind='bar') -> DOES NOT WORK

# sales.plot(x='date', y='weekly_sales', kind='line', rot=45) # rot -> rotate xlabel

# sales.plot(x='weekly_sales', y='store', kind='scatter')

# sales[sales['type']=='A']['weekly_sales'].hist(alpha=0.7)
# sales[sales['type']=='B']['weekly_sales'].hist(alpha=0.7) # Only when 2 has index and column same, then they will show together
# plt.legend(['type A', 'type B'])
plt.show()


''' Missing Values '''
# Introduce missing values to avocados dataframe
def introduce_missing_values(df, pct):
    for col in df:
        ori_rat = df[col].isna().mean()
        if ori_rat >= pct: continue
        add_miss_rat = (pct - ori_rat) / (1 - ori_rat)
        vals_to_nan = df[col].dropna().sample(frac=add_miss_rat).index
        df.loc[vals_to_nan, col] = np.NaN
introduce_missing_values(avocados, 0.2)
# print(avocados.isna().sum()) # How many missing values for each column
# print(avocados.isna().any()) # Is there any missing value at all in a column?
# avocados.isna().sum().plot(kind='bar')
# print(avocados.shape)
# avocados = avocados.dropna()
# print(avocados.shape)

# avocados.fillna(0) # Only fills numerical columns
# print(avocados.head(10))