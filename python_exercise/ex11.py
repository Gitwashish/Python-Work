def reverse_number(num):
    reversed_num = 0
    remainder = 0

    while num !=0:
      remainder = num%10
      reversed_num = reversed_num*10 + remainder
      num = num//10
      return reversed_num
    
print(reverse_number(10))
      
 