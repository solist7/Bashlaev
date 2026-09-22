from math import*
a = 0.1
b = 1,2
n = int(round(b-a)/step)
step = 0.05
for i in range(n):
  x = a+i*step
  y = pow(3,asin(x/2)) + log(3,2*x)
  print(y)
