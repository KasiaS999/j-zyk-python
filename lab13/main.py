# Proszę napisać abstrakcyjną klasę Calka z metodą inicjalizacyjną określającą granice całkowania, liczbę kroków oraz funkcję podcałkową (proszę skontrolować poprawność przekazanych parametrów) oraz metodą abstrakcyjną obliczającą wartość całki.
# Następnie proszę utworzyć klasy dziedziczące po klasie Calka z metodami obliczającymi wartość całki odpowiednio metodą trapezów lub Simpsona, w metodzie proszę umieścić komentarz dokumentacyjny. Potrzebne wzory są w pliku: calki.pdf (3.(3)p)
print('\n###################### 1 ####################')
import abc

class Calka(abc.ABC):
  def __init__(self, x_p, x_k, n, f):
    self.x_p = x_p
    self.x_k = x_k
    self.n = n
    self.f = f  
    if not callable(self.f):
      raise ValueError("Cos nie tak z funkcja")
    if not isinstance(self.x_p, int) or not isinstance(self.x_k, int):
      raise ValueError("przedzial nie jest poprawny")
    if not isinstance(self.n, int ):
      raise ValueError("Ilosc krokow nie jest liczba calkowita")

  @abc.abstractmethod
  def calka(self):
    '''Definicja metody abstrakcyjnej'''


class Trapez(Calka):
    def calka(self):
      '''Metoda trapezow obliczania calki'''
      h = (self.x_k - self.x_p)/self.n
      s = 0
      for i in range(1, self.n):
        s+=(self.f(self.x_p+i*h)+self.f(self.x_p+(i+1)*h))
      return s*(h/2)

try:      
  tr = Trapez(1, 'a', 10, lambda x: x)
except ValueError as error:
  print(error)

try:      
  tr = Trapez(1, 3, 10, 'w')
except ValueError as error:
  print(error)

tr = Trapez(1, 3, 100, lambda x: x**2)
print(tr.calka())

class Simpson(Calka):
  def calka(self):
    '''Metoda Simpsona obliczasnia calki'''
    h = (self.x_k - self.x_p)/(2*self.n)
    s = self.f(self.x_p)
    for i in range(1, 2*self.n):
      if i%2:
        s+=4*self.f(self.x_p+i*h)
      else:
        s+=2*self.f(self.x_p+i*h)
    s+= self.f(self.x_p+2*self.n*h)
    return s*(h/3)

sim = Simpson(1,3,100, lambda x: x**2)
print(sim.calka())

# Proszę napisać klasę implementującą stos, klasa ma obsługiwać możliwość tworzenia pustego stosu bądź inicjalizacji istniejącym stosem (obiektem klasy), dodawania i usuwania elementu, dodawania elementów innego stosu, zwracania rozmiaru i wypisywania stosu.
# Następnie proszę napisać klasę dziedziczącą po klasie stosu i implementującą stos posortowany (rosnąco lub malejąco). W tym przypadku element/elementy innego stosu można do stosu dodać pod warunkiem zachowania porządku sortowania.
# Proszę sprawdzić jaki jest średni rozmiar posortowanego stosu, który wypełniamy całkowitymi liczbami losowymi z przedziału [0,100] losując 100 wartości (średnia po 100 powtórzeniach) (3.(3)p)
print('\n###################### 2 ####################')
import random

class Stos:
  def __init__(self, st = None):
    self.stos = []
    if st:
      self.stos.extend(st.stos)
  def dodaj(self, elem):
    self.stos.append(elem)
  def dodaj_st(self, st):
    self.stos.extend(st.stos)
  def usun(self):
    self.stos.pop()
  def rozmiar(self):
    return len(self.stos)
  def __str__(self):
    s =""
    for i in self.stos:
      s+=str(i)
      s+=" "
    return s 


s = Stos()
s.dodaj(2)
s.dodaj(3)
print(f"rozmiar: {s.rozmiar()}")
s.dodaj(20)
s.dodaj(13)
print(s)
s1 = Stos(s)
s1.dodaj(-1)
print(s1)
s1.dodaj_st(s)
s1.usun()
print(s1)

class StosPosortowany(Stos):
  def __init__(self, st = None):
    self.stos = []
    if isinstance(st, StosPosortowany):
      self.stos.extend(st.stos)

  def dodaj(self, elem):
    if len(self.stos) == 0:
      self.stos.append(elem)
    else:
      if self.stos[-1]<=elem:
        self.stos.append(elem)

  def dodaj_st(self, st):
    if isinstance(st, StosPosortowany) and self.stos[-1]<=st.stos[0]:
      self.stos.extend(st.stos)

s = StosPosortowany()
s.dodaj(1)
s.dodaj(4)
s.dodaj(100)
s.dodaj(2)
s.dodaj(101)
s.dodaj(101)
print(s)
s1 = StosPosortowany()
s1.dodaj(-10)
s1.dodaj(-8)
s1.dodaj(-100)
s1.dodaj(-6)
s1.dodaj(-2)
s1.dodaj(0)
print(s1)
s1.dodaj_st(s)
print(s1)
s2 = StosPosortowany(s)
s2.dodaj_st(s1)
print(s2)

srednia = 0
for _ in range(100):
  s = StosPosortowany()
  for _ in range(100):
    s.dodaj(random.randint(0, 100))
  srednia+=len(s.stos)
print(f'Sredni rozmiar stosu to {srednia/100}' )

# Proszę zaimplementować klasę pozwalającą na zliczanie linii, słów i znaków w pliku (metody inicjalizująca i zliczająca). W klasie proszę także zaimplementować bezparametrową metodę statyczną zwracają komunikat analogiczny do komunikatu zwracanego przez polecenie systemowe linuxa wc w przypadku jednoczesnego zliczania dla kilku plików (3.(3)p)
# Przykład:
# $wc AA.py BB.py
#    50    91   944 AA.py
#    80  117 1281 BB.py
#  130  208 2225 razem

print('\n###################### 3 ####################')
class Zliczanie:
  linie = 0
  slowa = 0
  znaki = 0
  def __init__(self, file):
    self.file = file
  
  def zlicz(self):
    with open(self.file) as pl:
      t = pl.readlines()
    l = len(t)
    s = 0
    z = 0
    for i in t:
      s+=len(i.split())
      z+=len(i)
    print(f'{l} {s} {z} {self.file}')
    Zliczanie.linie+=l
    Zliczanie.slowa+=s
    Zliczanie.znaki+=z
  
  @staticmethod
  def wszystkie():
    print(f'{Zliczanie.linie} {Zliczanie.slowa} {Zliczanie.znaki} razem')

w = Zliczanie("1.dat")
w.zlicz()

w = Zliczanie("2.dat")
w.zlicz()
Zliczanie.wszystkie()
w = Zliczanie("3.dat")
w.zlicz()
Zliczanie.wszystkie()