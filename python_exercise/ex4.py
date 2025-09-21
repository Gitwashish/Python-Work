def factorsOfNumber(N):
    factors=[]
    for i in range(1, N+1):
        if N % i == 0:
         factors.append(i)
    return factors    

factorsOfNumber(12)
         

