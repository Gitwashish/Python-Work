# print number up to N that not divide by 3,6 and 9

def number(num):
    for i in range(1, num + 1):
        if i % 3 != 0 and i % 6 != 0 and i % 9 !=0:
            print(i) 

number(12)           
          


            