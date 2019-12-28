#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd

s = 'hello'
s = "hello"
str("hello")
str("11.5")
str([1,2,3])

""" Pass any class to String """
class NewClass:
    def __init__(self, num):
        self.num = num
    def __str__(self):
        return str(self.num)
nc = NewClass(2)
#print(str(nc))

s[1]
s[-1]
s[1:4]
s[2:]
s[:3]
s.index('l')

""" METHODS """
#s[0] = 'a' <- TypeError, strings are IMMUTABLE
s2 = s + 'Git'
s2 = s.replace('ll', 'r')
l = ['I', 'like', 'to', 'study']
s = ' '.join(l)
s2 = ''.join(l)
l = s.split(' ') # reverse of join

""" DATAFRAME """
d = {'name':['john', 'amanda', 'rick'], 'age':[35,29,19]}
#print(list(d.items()))
D = pd.DataFrame(d)
D['name'] = D['name'].str.capitalize()
print(D)




























