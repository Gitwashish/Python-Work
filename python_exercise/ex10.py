# armstrong means that value equal sum raise to the power their own digit.
# ex 153,  1^3 + 5^3 + 3^3 = 153

def is_armstrong(num):
    num_digit = len(str(num))
    sum =0
    # temprory varible to store the original number
    temp = num 
    # caculat the sum digit raised to power of number of digits
    while temp>0:
        digit = temp % 10 
        sum += digit ** num_digit
        temp//=10

    if num == sum:
        return True
    else:
        return False     

print(is_armstrong(153))  
    