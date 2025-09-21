# program for calculating roots of quadratic eqn
import math

def root_find(a,b,c):
    discrement=b**2 - 4*a*c
    if discrement > 0:
        root1=(-b+math.sqrt(discrement))/2*a
        root2=(-b-math.sqrt(discrement))/2*a
        return root1, root2
    elif discrement == 0:
        root=-b/2*a    
        return root
    else:
        real_part=-b/2*a
        img_part=math.sqrt(abs(discrement))

        root1=complex(real_part, img_part)
        root2=complex(real_part, -img_part)
        return root1, root2
    


