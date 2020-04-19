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










