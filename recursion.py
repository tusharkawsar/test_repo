#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(5))

def fibonacci(n):
    if n==1 or n==2:
        return 1
    return fibonacci(n-2)+fibonacci(n-1)
print(fibonacci(15))

def fib(n):

  if n < 2:
    return (n, 1)

  fib1 = fib(n-1)
  fib2 = fib(n-2)

  return (fib1[0] + fib2[0], fib1[1] + fib2[1] + 1)

print(fib(15))

def average(nums):
  
    # Base case
    if len(nums) == 1:
        return nums[0]
    
    n = len(nums)
    func_ret = average(nums[1:])
    avg = (((n-1)*func_ret) + nums[0]) / n
    return avg

print(average([1, 2, 3, 4, 5]))

# Write an expression to get the k-th element of the series 
get_elmnt = lambda k: ((-1)**k)/(2*k+1)

def calc_pi(n):
    curr_elmnt = get_elmnt(n)
    
    # Define the base case 
    if n == 0:
    	return 4
      
    # Make the recursive call
    return 4 * curr_elmnt + calc_pi(n-1)
  
# Compare the approximated Pi value to the theoretical one
print("approx = {}, theor = {}".format(calc_pi(500), math.pi))