from math import*
summ = sum((2**(2*n)/factorial(2*n)) * log(n) for n in range(1,51))
print(summ)