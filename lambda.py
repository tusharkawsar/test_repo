#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" LAMBDA is a replacement for small function definitions. 
Another name - anonymous function """

print((lambda x: x**2)(4)) # Idea of ANONYMITY
square = lambda x: x**2
print(square(4))
power = lambda x,y: x**y
print(power(2,3)) # Missing an argument results in TYPEERROR
(lambda :print("hello"))() # Calling LAMBDA without a parameter, notice the required braces
def function_with_callback(num, callback_function): # Useful when one parameter is dependent on another
    return square(num)
print(function_with_callback(8, square)) # This is inefficient
print(function_with_callback(8, lambda x: x**2)) # Thsi is EFFICIENT

# Odd/Even - If/Else in lambda
odd_even = lambda x: "odd" if x%2==1 else  "even"
print(odd_even(4))

import math
lambda3 = lambda *nums: math.sqrt(sum([item**2 for item in nums])) # You need the first * but not on the body of LAMBDA
print(str(str(lambda3(3, 4))))
print(str(str(lambda3(3, 4, 5))))

words = ['tequila','area','job','time','service','phone','advantage','shape','atmosphere','creature','plane','bag','truck','cell','call','item','chicken','transaction','car','leader','government','height','unit','interview','country']
words.sort(key=lambda s:s[-1])
#print(words)
words.sort(key=lambda s: len(s))
#print(words)
words.sort(key=lambda s: s.count('a')+s.count('b')+s.count('c'))
#print(words)
https://github.com/donnemartin/system-design-primer

""" MAP - how items with same index in iterables will be mapped to a new object """
nums = [i for i in range(1,6)]
def squared(x):
    return x**2
squares = map(squared, nums)
print(squares, type(squares)) # This object is ITERABLE + can be made into a LIST
# Map is also an ITERATOR # print(next(squares))
squares = map(lambda x: x**2, nums)

nums1 = [i for i in range(1,6)]
nums2 = [i for i in range (10,60,10)]
mult = map(lambda x,y: x*y, nums1, nums2) # We take each element from each list/iterable and perform operation
print(list(mult)) # Map objects cannot be directly printed

""" FILTER - takes ONE iterable and maps to boolean values and filters """
nums = [i for i in range(-3,4)]
obj = filter(lambda x: True if x>0 else False, nums) # I could just return x>0
print(list(obj)) # Similar properties as MAP OBJECT

""" REDUCE """
from functools import reduce 




















