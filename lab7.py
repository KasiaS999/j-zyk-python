import math
import random
#1

def licz():
  a=1
  while 1:
    yield a
    a+=1

def f(x, i):
  if not i%x: 
    print (x)
    print(i)
    return x

def dosk(l):
  
  
  for i in l:
    d = []
    for dzielnik in range(1,i):
      if not i%dzielnik:
        d.append(dzielnik)
    if sum(d)== i:
      yield i

def f1(a,b):
  for i in a:
    if i>b:
      return
    yield i

print(list(f1(dosk(licz()), 100)))

#2

def f2(b):
  u = 0
  x =1
  a =0.05
  

  while abs(x-b)>1e-6: 
      x += a
      u = u+a/x    
      yield x, u, math.log(x)

print(list(f2(1.5))) 

3

def f3(a):
  l = [ i for i in range(a-1,0, -1)]

  #print(l)
  for i in l:
    b = i
    t=[]
    while a>0:
      
      if a-sum(t)-b > 0:
        t.append(b)
        #print(t)
      if a-sum(t)-b == 0:
        t.append(b)
        yield t
        break
      if a-sum(t)-b<0:
        b-=1
      
print(list(f3(4)))


#4

def f4():
  x = random.random()
  y = random.random()
  #print(x,y)
  while 1:
    if abs(x-y)>0.4:
      yield x,y
    y=x
    x=random.random()
    if x < 0.1:
      return 
    #print(x)

print(list(f4()))

#5

def myrange(p, k=None, krok = 1):

  if k is None:
    k=p
    p=0

  if  (p<k and krok <0) or (p>k and krok >0):
    return 
 
  if p>=k:
    while p>=k:
      yield p
      p+=krok

  else:
    while p<k:
      yield p
      p+=krok


print(list(myrange(8)))
print(list(myrange(-8)))
print(list(myrange(1,8)))
print(list(myrange(8,1)))
print(list(myrange(1,8,2)))
print(list(myrange(1,8,-2)))
print(list(myrange(8,1,2)))
print(list(myrange(8,1,-2)))
