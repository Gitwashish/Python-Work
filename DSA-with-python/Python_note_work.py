# list1 = ['physics', 'chemistry', 1997, 2000]
# print (list1)
# list1.remove()
# print ("After deleting value at index 2 : ")
# print (list1)

# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# dict['Age'] = 8; # update existing entry
# dict['School'] = "DPS School"; # Add new entry
# # print ("dict['Age']: ", dict['School'])

# dict.clear(); # remove all entries in dict
# # del dict ; # delete entire dictionary    kaam nhi kr raha

# print ("dict['School']: ", dict['Age'])

# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]

# for r in T:  #r is row 
#    for c in r:  #traversing each row column wise
#      print(c)


# T = [[11, 12, 5, 2], [15, 6,10], [10, 8, 12, 5], [12,15,8,6]]
# T[2] = [11,9]
# T[0][3] = 7
# for r in T:
#     for c in r:
#         print(c,end=" ")
#     print()    


# Matrix is a special case of two dimensional array, where, each data element is of strictly
# same size. So, every matrix is also a two dimensional array but not, vice versa. 
# Matrices are very important data structures for many mathematical and scientific
# calculations. 

# from numpy import *
# m = array([['Mon',18,20,22,17],['Tue',11,18,21,18],
#  ['Wed',15,21,20,19],['Thu',11,20,22,21],
#  ['Fri',18,17,23,22],['Sat',12,22,20,18],
#  ['Sun',13,15,19,16]])

# m_r = append(m,[['Avg',12,15,13,11]],0)
# print(m_r)

# output
# for  m_r = append(m,[['Avg',12,15,13,11]],0)  ,0 is represemting end line after printing 1 row

# [['Mon' '18' '20' '22' '17']
#  ['Tue' '11' '18' '21' '18']
#  ['Wed' '15' '21' '20' '19']
#  ['Thu' '11' '20' '22' '21']
#  ['Fri' '18' '17' '23' '22']
#  ['Sat' '12' '22' '20' '18']
#  ['Sun' '13' '15' '19' '16']
#  ['Avg' '12' '15' '13' '11']]

# output for  m_r = append(m,[['Avg',12,15,13,11]])

# ['Mon' '18' '20' '22' '17' 'Tue' '11' '18' '21' '18' 'Wed' '15' '21' '20'
#  '19' 'Thu' '11' '20' '22' '21' 'Fri' '18' '17' '23' '22' 'Sat' '12' '22'
#  '20' '18' 'Sun' '13' '15' '19' '16' 'Avg' '12' '15' '13' '11']


#  The elements in the set are immutable (cannot be modified), but the set as a whole
# is mutable.
#  There is no index attached to any element in a python set. So they do not support
# any indexing or slicing operation.

# Days= set(['Wed', 'Sun', 'Fri', 'Tue', 'Mon', 'Thu', 'Sat'])
# set(['Jan', 'Mar', 'Feb'])
# set([17, 21, 22])
# # for d in Days:
# #     print(d)

# Days.discard("Sun")
# print(Days)

# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# # AllDays = DaysA & DaysB   #logial "and" (intersection)
# AllDays = DaysA | DaysB   #logial "or" (union)
# print(AllDays)   

# The difference operation on two sets produces a new set containing...

# DaysA = set(["Mon","Tue","Wed"])
# DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
# AllDays = DaysA - DaysB
# print(AllDays)

# We can check, if a given set is a subset or superset of another set The result is True or
# False depending 

# A = set(["Mon","Tue","Wed"])
# B = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
# SubsetRes = A <= B  #A is subset of b or not
# SupersetRes = B >= A  #B is a superset of a or not
# print(SubsetRes)
# print(SupersetRes)

# Python Maps also called ChainMap is a type of data structure to manage multiple
# dictionaries together as one unit.
# The best use of ChainMap is to search through multiple dictionaries at a time and get the proper
#  key-value pair mapping.  

# import collections
# dict1 = {'day1': 'Mon', 'day2': 'Tue'}
# dict2 = {'day3': 'Wed', 'day1': 'Thu'}
# res = collections.ChainMap(dict1, dict2)
# Creating a single dictionary
# print(res.maps,'\n')  #o/p [{'day1': 'Mon', 'day2': 'Tue'}, {'day3': 'Wed', 'day1': 'Thu'}] 
# print('Keys = {}'.format(list(res.keys()))) #Keys = ['day3', 'day1', 'day2']
# print('Values = {}'.format(list(res.values())))   #Values = ['Wed', 'Mon', 'Tue']  
# print()
