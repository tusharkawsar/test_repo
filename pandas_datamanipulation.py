#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 13:31:31 2020

https://learn.datacamp.com/courses/data-manipulation-with-pandas
"""

import pandas as pd
import pickle
from IPython.display import display, HTML

path_avoplotto = 'data/pandas_datamanipulation/avoplotto.pkl'
path_homeless = 'data/pandas_datamanipulation/homeless_data.pkl'
path_walmart = 'data/pandas_datamanipulation/walmart_sales.pkl'

homelessness = pickle.load(open(path_homeless, 'rb')) # Pickle returns a DF
# print(homelessness) # The entire DF
# display(homelessness) # Better output for IPython
print(homelessness.head())



