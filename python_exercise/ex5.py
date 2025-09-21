import math

def evalX(P):
    if(P==0):
        x = 1
    elif (P<0):
        x = 2*math.sin(math.pi*P)
    else:
        x = 2*math.cos(math.pi*P ) 
    return x    

result = evalX(6)  
print(result) 
   


        

    

