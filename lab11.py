####1#####

import random
import matplotlib.pyplot 


class IFS:
  def __init__(self, przeksz, prawd):
    self.x = [0]
    self.y = [0]
    self.prz = przeksz
    self.prawd = prawd

  def przeksztalcenia(self, N):
    for i in range(1,N):
      w = random.choices(self.prz, weights = self.prawd, k = 1)[0]
      self.x.append(w[0]*self.x[i-1] + w[1]*self.y[i-1]+w[2])
      self.y.append(w[3]*self.x[i-1] + w[4]*self.y[i-1]+w[5])

  def rysuj(self):
    matplotlib.pyplot.plot([i for i in self.x], [i for i in self.y], linestyle="", marker=",")
    matplotlib.pyplot.show()

prz = ((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065), (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236), (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035))
pra = (0.90, 0.05, 0.05)
ifs1 = IFS(prz, pra)
ifs1.przeksztalcenia(10000)
ifs1.rysuj()

prz = ((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513), (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43), (0.119, 0, -2.555, 0, 0.053, 4.536), (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235), (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569), (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113), (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37), (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43), (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487), (0, 0.053, 3.972, 0.429, 0, 4.569), (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716), (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298), (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487))
pra = (1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
ifs2 = IFS(prz, pra)
ifs2.przeksztalcenia(10000)
ifs2.rysuj()

prz = ((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607), (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795))
pra = (0.8, 0.2)
ifs2 = IFS(prz, pra)
ifs2.przeksztalcenia(10000)
ifs2.rysuj()

#####2#####
import math

class Wektor:
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def __add__(self, wektor):
    return Wektor(self.x+ wektor.x, self.y+ wektor.y, self.z+ wektor.z)
  
  def __sub__(self, wektor):
    return Wektor(self.x- wektor.x, self.y- wektor.y, self.z- wektor.z)

  def __mul__(self, liczba):
    return Wektor(liczba*self.x, liczba*self.y, liczba*self.z)

  __rmul__ = __mul__

  def __str__(self):
    return f"({self.x}, {self.y}, {self.z})"
  
  def dlugosc_wektor(self):
    return math.sqrt(self.x**2+ self.y**2+ self.z**2)

  def iloczyn_skalarny(self, wektor):
    return self.x*wektor.x+self.y*wektor.y+self.z*wektor.z

  def iloczyn_wektorowy(self, wektor):
    x = self.y*wektor.z-self.z*wektor.y
    y = self.z*wektor.x-self.x*wektor.z
    z = self.x*wektor.y-self.y*wektor.x
    return Wektor(x,y,z)

  def iloczyn_mieszany(self, wektor1, wektor2):
    wektor1 = wektor1.iloczyn_wektorowy(wektor2)
    return self.iloczyn_skalarny(wektor1)

a = Wektor(1,2,-1)
b = Wektor(3,4,5)
print("\n\n")
print(f"a = {a}")
print(f"b = {b}")
print(f"a+b = {a+b}")
print(f"b-a = {b-a}")
print(f"3*b = {3*b}")
print(f"b*2 = {b*2}")
print(f"dlugosc wektora a = {a.dlugosc_wektor()}")
print(f"a*b = {a.iloczyn_skalarny(b)}")
print(f"axb = {a.iloczyn_wektorowy(b)}")

c = Wektor(4,3,5)
print(f"c = {b}")
print(f"a*(bxc) = {a.iloczyn_mieszany(b,c)}")


#####3#####
print("\n\n")
def strumien(B, S):
  return B.iloczyn_skalarny(S)

def Lorentz(q, E, v, B):
  return q*(E + v.iloczyn_wektorowy(B))

def praca(q, E, v):
  return q*E.iloczyn_skalarny(v)

B = Wektor(1, 0, 3)
S = Wektor(22, 4, -6)
print(f"strumien: {strumien(B, S)}")

q = 2
E = Wektor(12, 9, 6)
v = Wektor(3, 0, 7)
print(f"sila Lorenza: {Lorentz(q, E, v, B)}")
print(f"praca: {praca(q, v, E)}")
