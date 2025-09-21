# fibonacci means next 0,1,this term = sum of two previous terms and so on
def generate_fibonacciSquence(n):
    fibonacci_squence = [0,1]
     
    while (fibonacci_squence[-1] + fibonacci_squence[-2] <= n):
        fibonacci_squence.append(fibonacci_squence[-1] + 
                                 fibonacci_squence[-2])
    else:
        return fibonacci_squence
    
output = generate_fibonacciSquence(8)
print('{0}\n the generated fibonacci_sequence upto the number'.format(output))

    