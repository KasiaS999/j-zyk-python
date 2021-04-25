import random
import sys

#1

def fun1(s):

  for i in s:
    if i.isalpha() and i != 'x':
      a = str(random.randrange(10))
      t =s.maketrans(i, a)
      s=s.translate(t)
      
  lista = [(x := random.random(), eval(s)) for _ in range(10)]

  return lista

print(fun1(sys.argv[1]))


#2

def fun2(*p):
  lista = []
  for i in p[0]:
    for j in p[1:]:
      if i not in j:
        break
    else:
      lista.append(i)
  return lista

print(fun2([2,3,4,5], (7,8,3,5 ,4), [4,5,3,2]))

#3
def fun3(p1, p2, f = True):
  if f:
    lista = [(p1[i], p2[i]) for i in range(len(p1) if len(p1) < len(p2) else len(p2) )]
  else:
    lista = [(p1[i] if i<len(p1) else None, p2[i] if i< len(p2) else None ) for i in range(len(p1) if len(p1) > len(p2) else len(p2) )]

  return lista
print(fun3([1,2,3,4], [5,6,7,8,9,10,222,6], False))
print(fun3([1,2,3,4], [5,6,7,8,9,10,222,6]))


#4

def fun4(kwota, nominal = (10, 5, 2)):
  dic = {}
  for i in nominal:
    if kwota >= i:
      aktualna_kwota = kwota
    licznik = 0
    while kwota>=i:
      
      kwota-=i
      licznik +=1
      
    if licznik !=0:
      dic[i] = licznik
    if not kwota:
      return dic
    if kwota == aktualna_kwota:
      return 'nie ma możliwości rozmienienia tej kwoty'
 
print(fun4(37)) 
print(fun4(66, nominal = (8,6,1))) 


#5

def fun5(los, poczatek, koniec, sposob ='r'):
  
  proba = random.randint(poczatek, koniec) if sposob == 'r' else (poczatek+koniec)//2
  licznik = 1
  while proba != los:
    poczatek = poczatek if los < proba else proba
    koniec = koniec if los> proba else proba
    proba = random.randint(poczatek, koniec) if sposob == 'r' else (poczatek+koniec)//2
    licznik+=1
    
  return licznik

print(fun5(3, 2, 65))
print(fun5(13, 2, 100, 'w'))