# hcf of number input by user

def compute_hcf(x,y):
    while(y):
        x,y = y,x%y
    return x    
varr = compute_hcf(14,8)
print('the hcf of numbers is:',varr)