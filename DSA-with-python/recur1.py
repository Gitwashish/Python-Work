#lec-1
def printN(n):
    if n>0:
        printN(n-1)
        print(n,end=" ")
# printN(10)   

def printNrev(n):
    if n>0:
        print(n,end=" ")
        printNrev(n-1)
# printNrev(10)        

def printOdd(n):
    if n>0:
        printOdd(n-1)
        print(2*n-1,end=" ")
# printOdd(10)        

def printEven(n):
    if n>0:
        printEven(n-1)
        print(2*n,end=" ")
# printEven(10)

def printoddRev(n):
    if n>0:
        print(2*n-1,end=" ")
        printoddRev(n-1)
# printoddRev(10)    

def printevenRev(n):
    if n>0:
        print(2*n,end=" ")
        printevenRev(n-1)
# printevenRev(10)

# lec-2
    
def sumN(n):
    if(n==0):
        return 0
    return n + sumN(n-1) 
print(sumN(10))    

def sumoddN(n):
    if(n==0):
        return 0
    return 2*n-1 + sumoddN(n-1)   
print(sumoddN(10))

def sumevenN(n):
    if(n==0):
        return 0
    return 2*n + sumevenN(n-1)   
print(sumevenN(10))

def fact(n):
    if(n==1 or n==0):
        return 1
    return n*fact(n-1)
print(fact(5))

def sumsqN(n):
    if(n==1):
        return 1
    return (n*n) + sumsqN(n-1)
print(sumsqN(5)) 