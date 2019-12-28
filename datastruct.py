# -*- coding: utf-8 -*-

""" LIST """
my_list = [x for x in range(1,5+1)]
my_list[2]
my_list[-1]
my_list[1:3]
my_list[2:]
my_list[2] = 30
my_list[3:] = [31,32]
my_list.append("a")
my_list.remove(30)
#print(my_list.pop())
#print(my_list.count(31))
#print(my_list)


""" TUPLE - immutable but ordered """
my_tuple_list = [(x,x) for x in range(1,5)]
my_tuple = tuple(my_tuple_list)
my_tuple_2 = 1, 'apple', 3
# my_tuple[0] = 10 -> TypeError


""" SET """
my_set = set([1,1,2,2,2,3,4,5])
my_set.add(600)
my_set.remove(2)
my_set = my_set.union({1,55,66})
my_set = my_set.intersection({2,3,5,55})
my_set = my_set.difference({55})
#print(my_set)

""" DICTIONARY - key is immutable, lists cannot be keys """
fruits = {'apple':10, 'orange':6, 'banana':9}
fruits = dict([('apple',1), ('orange',2), ('banana',3)])
fruits['apple'] = 10
fruits.items()
list(fruits.items())
fruits.keys()
list(fruits.keys())
fruits.values()
list(fruits.values())
fruits.popitem()
print(fruits)

""" OPERATIONS """
len(my_list)
len(my_tuple)
len(my_set)
len(fruits)

2 in my_list
2 in my_tuple
2 in my_set
'apple' in fruits