# use of if else sattemet
# n=2
# if n>3:
#     print('val is >3')
# elif n==3:
#     print('vval is 3')
# else:
#     print('val is lesser then 3')        

# use of while loop
# count=1
# while(count<=10):
#     print(count)
#     count +=1
# print('Outside while loop')  
# cal factorial using while
# n=5
# i=1
# f=1
# while(i<=n):
#     f=f*i
#     i+=1
# print('fact is:',f)    

# use of for loop
# lang=['wer','ter','yer']
# for i in lang:
#     print('i lov lang:', i )

# list=[2,23,54,67,89]
# input=5
# for i in list:
#     if input==i:
#         print('in the list')
#         break
#     else:
#         print('not in list')

# print('hello {0} {1} {2}!'.format('bachha','goodmorning','ashish'))

#   cal factorial using for loop
# n=4
# for i in range(1,n+1):
#     f=1
#     for j in range(1,i+1):
#         f=f*j
#     print("fact of {0} is {1}".format(n,f))    
# use of break
# for i in range(0,9):
#     if i==6:
#         break
#     else:
#         print(i)
# print('exit for')   

# 
# use of continue      
# for i in range(0,9):
#     if(i==6):
#         continue
#     else:
#         print(i)
# print('exit for')        

# use of pass
# for i in range(0,9):
#     if(i==6):
#         # pass
#         print('this is pass statemant')
#     print(i) 
# print('exit for')    
    # comparision among 3 no.s
# a,b,c=int(input('enter a b c:'))
# if a>b:
#     if a>c:
#         print('a is grtest')
#     else:
#         print('c is the grtest')
# else:
#      print('b is the grtest')           

# my_list=['apple','banana','grapes']
# for i in range(len(my_list)):
#     print('index:',i,'value:',my_list[i])

# my_list=['apple','banana','grapes']
# for i in my_list:
#     print('value:',i)

# list=[3,4,9,6,1,7]
# print(list(2:5))    
# list=(3,4,9,6,1,7) 
# print(list[2:5])    

# printing mulipliction table 1-5
# for i in range(1,6):
#     for j in range(1,11):
#         print(i*j, end='\t')
#         print()