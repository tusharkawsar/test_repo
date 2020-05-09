#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 14:41:55 2020

@author: tushar
"""

import pytest
import re

'''Ideally, the name of this file should be test_convert_to_int,
because one unit test should be associated with one function only

Also, the filename cannot be unittest.py
'''

def convert_to_int(s):
    s_copy = re.sub(',', '', s)
    # print(s_copy, type(s_copy))
    return s_copy

def test_with_one_comma():
    assert convert_to_int('2,081') == '2081'
    