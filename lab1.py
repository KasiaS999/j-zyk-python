import sys
import math
import cmath


if len(sys.argv)!=5:
  sys.exit()

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
eps = float(sys.argv[4])


if (d:=b**2-4*a*c)>eps :
  x1=(-b - math.sqrt(d))/(2*a)
  x2 =(-b + math.sqrt(d))/(2*a)
  print(f'{x1=:.3f}, {x2=:.3f}')
elif math.fabs(d) < eps:
   
  print(f'x1=x2={-b/(2*a):.3f}')
else:
  x1=(-b - cmath.sqrt(d))/(2*a)
  x2 =(-b + cmath.sqrt(d))/(2*a)
  print(f'{x1=:.3f}, {x2=:.3f}')


'''
from math import sqrt
from cmath import sqrt as csqrt

a=[]
print(type(a))
a=[2]
print(type(a))
a=[2,]
print(type(a))
a = (1, 2.34, (4.5, 7), [1,2,3])
print(len(a))
a[-1][1]=7
print(a)

a = float(input('a= '))
b = float(input('b= '))
c = float(input('c= '))
eps = 1e-6
d = b**2-4*a*c

if d>eps:
  x1=(-b - sqrt(d))/(2*a)
  x2 =(-b + sqrt(d))/(2*a)
  print(f'x1 = {x1: .3f}, x2 = {x2: .3f}')
elif abs(d) < eps:
  x = -b/(2*a)
  print(f'x1=x2={x}')
else:
  x1=(-b - csqrt(d))/(2*a)
  x2 =(-b + csqrt(d))/(2*a)
  print(f'x1 = {x1: .3f}, x2 = {x2: .3f}')


import math
print(dir(math))

a, *b= 1,1, 2
print(type(a))
A=math.modf(1/3)
print(A)
print(type(A))
k =(1 ,2.3 ,'3',(4,7), [ 2 , 3 , 4 ] ,)
print(len(k))
print(k[-1])

w= [1 ,2.3 ,'3',(4,7), [ 2 , 3 , 4 ] ,]
w[-1] = 'w'
print(len(w))


k=[2,4]

k=[1,2,3,4,5]
k[1] =2,3
print(k)

'''
