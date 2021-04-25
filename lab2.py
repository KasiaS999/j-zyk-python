import copy

k=[8, 0, 1, 16, 9, 5, 4, 3, 2, 1, 7,]

#WYCINEK
print(type(k))
print(len(k))
print(k)
print(k[::-2])
print(k[-1])
a = k[2:9]
print(a)
b = k[2:9:2]
print(b)
print(b[:-3])
#KOPIOWANIE PŁYTKIE
k=[1, 2.3, '3', (4,7), [2,3,4],]
c=k
#c[1] =[7,8,9]

#coś jak adres
print(id(c))
print(id(k))

#KOPIOWANIE "PÓŁPŁYTKIE"
c = k[:]
c[2] = 999
c[-1][1] = 88
print("k: ")
print(k)

c = k.copy()
c[-1][1] = 0 
c[-1][2] = 999
print("k: ")
print(k)

c= copy.copy(k)
c[-1][1] = 10009
print("k: ")
print(k)
#KOPIOWANIE GŁĘBOKIE
c= copy.deepcopy(k)
c[-1][1] = 10009
print("k: ")
print(k)

#ZLICZANIE
k = [1,1,1,19,1,1,20,]
print(k.count(-11))
print(k.count(1))

#ZNAJDOWANIE ELEMENTU
print(k.index(20))
#print(k.index(-1)) pokaże się wyjątek

print(13 not in k)
print(19 in k)
if 13 in k:
  print("AAAA")

if 13 not in k:
  print("BBBB")


#DODAWANIE ELEMENTU DO LISTY
k.insert(4, -13)
#dodany na indeks 4, reszta przesunięta w prawo
k.insert(-205, 9999)
k.insert(1000, -888)
print(k)
k[1:4] = [6,[7,9,0],12,45,17]
k[-3:-1]  = "ALA"
print(k)


#USUWANIE ELEMENTÓW Z LISTY
k.remove(-888) #wartość którą chcemy usunąć, jedną, pierwszą
#k.remove(-3)   chce usunac cos czego nie ma, pojawi sie blad
print(k)

del k[3] #to juz usuwa po indeksie 
#del k[-23]  bedzie blad 
print(k)
del k[-3:]
print(k)

#pop  nie tylko  usuwa, domyslnie ostatnia, wartosc, ale rowniez ja zwraca
print(k.pop())
print(k)
print(k.pop(-2))
print(k)

#WYCZYSZCZENIE ZAWARTOSCI LISTY
k.clear()
print(k)


#ROZBUDOWYWANIE LISTY

k=[1]*10 #różne 1, kopiowane przez wartość
k[3]+=1
print(k)
k=[[]]*10 #skopiowalismy referencje do tej listy co sie pojawila, mamy 10 tej listy
k[3].append(1)
print(k)

#chce utworzyc liste ktora ma 10 list w sobie 

#lista składana 
k=[[] for _ in range(10)] #_ bo i potem już nie wykorzystujemy
#tablice są niezależne teraz 
k[3].append(1)
k[1].append([1,2,3,4]) #doda jako całość
k[1].append(7)
print(k)

k[-1].extend([7,7,7]) #doda osobno kazda 7 do tablicy k[-1]
print(k)

#RANGE
k=list(range(10))
print(k)

k=list(range(3,10))
print(k)
k=list(range(3,10,2))
print(k)
k=list(range(10,0,-1))
print(k)

#żeby bylo ładnie lista skladana
k = [i for i in range(10, 18, 2)]
print(k)


#PĘTLA
k=[8, 0, 17, 1, 10, 13, 19, 13, 10, 3,]
for i in k:
  i*=2
  
  print(i, end=', ')
  #zamiast przechodzenia do nowej linii, ma koncu bedzie ', '
print('\n k: ', k)

for i in range(len(k)):
  k[i]*=2
print('k: ', k)

for i, v in enumerate(k):
  k[i] = 1 if v>0 else -1  #!!!!
print(k)
#enumerate zwraca dwuelementowe krotki (i, v), i to indeks, v to wartosc 

if 5<7<8:
  print('AAAA')

#ELSE ZWIAZANY Z FORem
k = [2,4,8,]
for i in k:
  if i%2:
    print(i)
    break;
else:
  print('Kiedy?')


#else w for sie wykona jesli nie doszlo do przerwania, sprawdzamy tak czy doszło do breaka w pętli czy nie


#LISTA SKŁADANA
k=[8, 0, 17, 1, 10, 13, 19, 13, 10, 3,]
print('k:', k)
np = [i for i in k if i%2]
#w np beda liczby ktore spelniaja warunek w if (liczby nieparzyste)
print(np)
np= [1 if i%2 else -1 for i in k]
#warunek gdy zawsze cos dodajemy
print(np)

k=[(k[i], k[-i-1]) for i in range(len(k)//2)]
#k//2 oddaje wartosc całkowite, a w range musza byc calkowite 
#-1 bo byłby problem przy i=0
print(k)

for i, j in k:
  print('i =', i)
  print('j =', j)

#SORTOWANIE LIST

k = [(89, 34), (92, 31), (96, 0), (48, 30), (38, 10), ]
print(k)
c=k[:]
c.sort() 
#c=c.sort() Można tak napisać ale będzie wartość c = None, bo to jest wartosc ktore zwraca sortowanie
print(c) #posortowane wzgledem pierwszego parametru
c=k[:]
c.sort(key=lambda x: x[1]) #sortuje wzgledem tego drugiego parametru
print(c)

#malejąco sortowanie
c=k[:]
c.sort(reverse=True)
print(c)

c=k[:]
#tylko w petli posortowane, za petla juz bedzie w starej kolejnosci
for i, j in sorted(c):
  print(i,j)

print(c)
#ODWRÓCONE C (od konca)
c.reverse()
print(c)
c=k[::-1]
print(c)


#korzystajac z petli for, usunac wszystkie wystapiemnia okreslonej wartosci z listy
k=[7, 8,9, 7,6,7,2]
for i in k:
  if i==7:
    k.remove(i)
print(k)

#j.w korzystajac z while

k=[7, 8,9, 7,6,7,2]
while 7 in k:
  k.remove(7)
print(k)


#wypisac co drugi element z listy bez id
k=[7, 8,9, 7,6,7,2]
for i in range(1,len(k),2):
  print(k[i], end=', ' )
print('\n')

#co drugi bez range
c=k[1::2]
print(c)

#co drugi od konca
b=[7, 8,9, 7,6,7,2]
print(b)


for i in range(len(b)-1,-1,-2):
  
  print(b[i], end=',')
print('\n')

c=b[-1::-2]
print(c)

k=[8, 0, 17, 1, 10, 13, 19, 13, 10, 3,]
print('k:', k)
np = [(i, k[i]) for i in range(len(k))]
print(np)
np.sort(key=lambda x: x[1])
print(np)

k=[8, 0, 17, 1, 10, 13, 19, 13, 10, 3,]
print('k:', k)
np = [(i, k[i]) for i in range(len(k)) if not k[i]%2]
print(np)

np= [(i, k[i]) if i<k[i] else (k[i], i) for i in range(len(k))]
print(np)