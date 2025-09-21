# polndrome means aage and peeche se same ex word like 'level' 
# 12321, 121 these are ex of plondrome
def is_polndrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False
    
uttar = is_polndrome('level')
print('is plondrome?:',uttar) 

           
