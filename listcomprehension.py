#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" LIST COMPREHENSION - Performing perations to create a list/tuple/set """
nums = [num*2 for num in range(1,6)]
nums = [num for num in range(1,11) if num%2==0] # NOT where
print(nums)

text = 'list COMPREHENSION is A way TO create LISTS'
text_list = text.split(' ')
text_lower_pos = [text_list.index(word) for word in text_list if word.islower()]
print(text_lower)
text_lower_len = [len(word) for word in text_list if word.islower()]
print(text_lower_len)

numbers = [1,2,3]
letters = ['a','b','c']
convo = [(a,b) for a in numbers for b in letters] # There is no comma between loops
convo_1 = [[(a,b) for a in numbers] for b in letters] # List of lists, the first loop is not internal loop
print(convo_1)