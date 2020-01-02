#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" PASSING VARIABLE NUMBER OF ARGUMENTS """
# Positional Arguments
def func_with_var_pos_arg(*args): # Can use other names instead of ARGS
    print(args) # No asterisk necessary when dealing with ARGS
func_with_var_pos_arg(1,2)
func_with_var_pos_arg(1,2,3,"string")
def multiply(num1,num2,num3):
    return num1 * num2 * num3
nums = [1,2,5] # Also works with TUPLES
print(multiply(*nums))
nums_2 = [1,2] 
print(multiply(*nums_2,5))

# Keyword Arguments - they have default values in func parameter
def func_with_kwargs(arg1=1, arg2=2):
    print(str(arg1) + ":" + str(arg2))
func_with_kwargs(5,"sad")
func_with_kwargs()
def func_with_var_kwargs(**kwargs):
    print(kwargs)
func_with_var_kwargs(arg1=1, arg2=2, arg3=3) # Will print a DICT
#func_with_var_kwargs(1, 2, arg3=3) --> Will generate an error
def multiply_kwargs(**kwargs):
    result = 1
    for (key,value) in kwargs.items():
        result *= value
    return result
print(multiply_kwargs(arg1=1,arg2=2,argXX=3))
def multiply(num1=1, num2=2, num3=3):
    return num1 * num2 * num3
nums = {'num1':10, 'num3':30}
print(multiply(**nums)) # Only 2 arguments are sufficient for the function to run
# Inserting other keys -> TYPEERROR
print(multiply_kwargs(**nums)) # Without **, generates error

""" The single * means that there can be any number of extra positional arguments.
The double ** means there can be any number of extra named parameters. 
SERIAL: def func(arg1, arg2, *args, kwarg1, kwarg2, **kwargs) """
