def primeOrNOt(N):
    for i in range(2, N):
        if N % i == 0:
         return 'not prime'
        else:
         return'prime number'

result = primeOrNOt(12)
print(result)
