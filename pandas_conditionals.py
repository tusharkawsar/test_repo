#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 11:38:40 2020

@author: tushar
"""
import pandas as pd
import numpy as np

brics_df = pd.read_csv('data/brics.csv', index_col=0)
# brics_df.columns = [x.strip() for x in list(brics_df.columns)]
brics_df.columns = brics_df.columns.str.strip() # -> BETTER


X = brics_df.loc[:, ['area']].loc[brics_df['area'] > 3].values
X = list(brics_df.loc[brics_df['area'] > 3]['country'])
X = brics_df.loc[brics_df['area'] > 3]
print(X) # All 3 are equivalent

is_huge = brics_df.loc[:, 'area'] > 3
print('================', is_huge)
print(type(is_huge))


''' Utilizing Boolean Series to Subset Pandas Dataset: 
We can just create a list/series/nparray of booleans and 
use it as a knife to cut through original DF
- Do not use double brackets, use single to make bool Series
- If a column is already boolean, that can be directly used: df[df[bool_col]] '''

print(brics_df[is_huge])

# One-liner
print(brics_df[brics_df.loc[:, ["area"]] > 3]) # This will show unexpected
# behavior since we used double brackets, many NaNs
print(brics_df[brics_df.loc[:, 'area'] > 3]) # This shows all data for 2 rows

# is_populous = brics_df.loc[:, 'pop'] < 35
print(brics_df[brics_df.loc[:, 'pop'] < 35]) # one-liner
# print(brics_df[is_populous])

# Using logical AND
criteria_1 = brics_df.loc[:, 'area'] > 1
criteria_2 = brics_df.loc[:, 'pop'] < 40
criteria_all = criteria_1 & criteria_2
print(brics_df[criteria_all])

# 3 Equivalent ways of doing logical AND
print(brics_df[brics_df.loc[:, 'area'].between(2,4)]) # (1)
print(brics_df[np.logical_and(brics_df.loc[:, 'area'] >= 2, 
                              brics_df.loc[:, 'area'] <=4)]) # (2)
# In the following, very important to wrap inner boolean in ()'s
# to maintain operator precedence. Even better to do it outside 
# like criteria_1
print(brics_df[(brics_df.loc[:, 'area'] >= 2) & 
               (brics_df.loc[:, 'area'] <= 4)]) # (3) 


print("=================")
brics_df['country'] = brics_df['country'].str.strip() # Remove space before countryname
# X = brics_df.loc['ru', 'country']
X = list(brics_df.loc[:, 'country'])
print(type(X))
print(X)











































