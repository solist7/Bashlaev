from math import*
a = 0.1
b = 1.2
step = 0.05
n = int(round((b-a)/step)) + 1
for i in range(n):
  x = a+i*step
  y = 3**(asin(x/2)) + log(x*2,3)
  print(y,x)
