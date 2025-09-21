# prime no. b/w certain interval
# 1 is not prime

def presentPrime(n1, n2):
    for num in range(n1, n2+1):
        if num==2 or num==3 or num==5:
            print(num)
        elif num%2 != 0 and num%3 !=0 and num%5 !=0:
            print(num)
presentPrime(49, 107)
