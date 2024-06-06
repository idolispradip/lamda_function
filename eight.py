factorial = (lambda f: (lambda x: f(f, x)))(lambda f, n: 1 
if n == 0 else n * f(f, n - 1))


print(factorial(5))  
