class Fibonacci:
  def __init__(self, max):
    self.max = max
    self.a = 0
    self.b = 1
  def __iter__(self):
    return self
  def __next__(self):
    self.b, self.a = self.a+self.b, self.b
    while True:
      if self.a > self.max:
        raise StopIteration
      return self.a
      self.b, self.a = self.a+self.b, self.b
print("Zadanie pierwsze, jedna funkcja")

test = Fibonacci(30)
for j in test:
  for i in test:
    print((j, i), end = ' ')
  print()
print()
for j in Fibonacci(30):
  for i in Fibonacci(30):
    print((j, i), end = ' ')
  print()
    
class Fibonacci2:
  def __init__(self, max):
    self.max = max
    self.a = 0
    self.b = 1
  def __iter__(self):
    return FiboNext(self.max)

class FiboNext:
  def __init__(self, max):
    self.max = max
    self.a = 0
    self.b = 1

  def __next__(self):
    self.b, self.a = self.a+self.b, self.b
    while True:
      if self.a > self.max:
        raise StopIteration
      return self.a
      self.b, self.a = self.a+self.b, self.b
print("\nZadanie pierwsze, dwie funkcje")
test = Fibonacci2(30)
for j in test:
  for i in test:
    print((j, i), end = ' ')
  print()
print()
for j in Fibonacci2(30):
  for i in Fibonacci2(30):
    print((j, i), end = ' ')
  print()
#####################################################

import random

class Pseudolosowe:
  def __init__(self):
    self.m = 2**31 -1
    self.a = 7**5
    self.c = 0
    self.x = 1
  def __iter___(self):
    return self
  def __next__(self):
    self.x = (self.a* self.x + self.c)%self.m 
    return self.x/self.m

def miesci_sie(punkt, n):
  if punkt[0] < 0.1*n and punkt[1] < 0.1*n:
    return True
  return False


los = Pseudolosowe()
moj_los = [(next(los), next(los)) for _ in range(10**5)]
rand_los = [(random.random(), random.random()) for _ in range(10**5)]

for n in range(1, 11):
  m_w_kwadracie = 0
  r_w_kwadracie = 0
  for i in range(10**5):
    x = next(los)
    y = next(los)
    if miesci_sie(moj_los[i], n): 
      m_w_kwadracie+=1
    if miesci_sie(rand_los[i], n):
      r_w_kwadracie +=1
  print(f'w kradracie o boku 0.1*{n} miesci sie: moim losownikiem {m_w_kwadracie/(10**5) *100}% punktow, wbudowanym {r_w_kwadracie/(10**5)*100}%')
print()
#######################################################

import math
import scipy.misc

class NewtonRaphson:
  def __init__(self, f, x, eps):
    self.f = f
    self.x =x
    self.eps =eps
  def __iter__(self):
    return self
  def __next__(self):    
    self.x = self.x-self.f(self.x)/scipy.misc.derivative(self.f, self.x)
    if abs(self.f(self.x)) <= self.eps:
      raise StopIteration
    return self.x
    
t = NewtonRaphson(lambda x: math.sin(x)- (0.5*x)**2, 1.5, 1e-5)
for i in t:
  print(i)
print()