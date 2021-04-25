import time
import sys
import random
from functools import reduce
import math
#1
powt=1000
N=10000
print(sys.version)

def forStatement(n):
  l = []
  for i in range(n):
    l.append(i)

def listComprehension(n):
  l = [i for i in range(n)]

def mapFunction(n):
  l= map(lambda i: i, range(n))


def generatorExpression(n):
  l = (i for i in range(n))

def tester(function):
  t = time.time_ns()
  for i in range(powt):
    function(N)
  return time.time_ns() -t


test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))


#2

pi = len(list(filter(lambda i: (random.uniform(-1,1)**2 + random.uniform(-1,1)**2)**0.5 < 1, range(N))))/N *4
print(pi)

#3

A =[[1,2,3], [4,5,6], [7,8,9]]
max_w = list(map(lambda x: max(x), A))
print(max_w)
max_k = list(map(lambda x: max(x), zip(*A)))
print(max_k)
B = [[1,1,3], [4,5,1], [7,0,9]]
print(list(zip(A,B)))
suma = [list(map(sum, zip(*i))) for i in zip(A,B) ]
print(suma)

#4

l1 = [[1,2], [7,3], [8,4], [9,5], [5,6]]
l2 = []
l2 = list(reduce(lambda x,y: map(lambda x,y: [x,y] if not isinstance(x,list) else x+[y],x,y),l1))
print(l2)


#5

def fun(x, y):
  x_s = reduce(lambda x, y: x+y, x)/len(x)
  D = reduce(lambda x, y: x+y, map(lambda x: (x - x_s)**2, x))
  a = reduce(lambda x, y: x+y, map(lambda x, y: y*(x- x_s), x, y))/D
  y_s =  reduce(lambda x, y: x+y, y)/len(y)
  b = y_s - x_s*a
  d_y = math.sqrt(reduce(lambda x, y: x+y, map(lambda x,y: (y - (a*x + b))**2,x ,y ))/(len(x)-2))
  d_a = d_y/math.sqrt(D)
  d_b = d_y*math.sqrt(1/len(x) + (x_s**2)/D)
  return a,b,d_a,d_b
print(fun([1,2,3,4],[3,5,7,9.2]))
