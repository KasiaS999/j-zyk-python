################1####################
import datetime

def czy_poprawny(pesel, data, plec):
  rok = int(pesel[:2])
  miesiac = int(pesel[2:4])
  dzien = int(pesel[4:6])
  plec_liczba = int(pesel[7:10])
  kontrolna = int(pesel[10])

  if 0<miesiac<13:
    rok+=1900
  elif 20<miesiac<33:
    rok+=2000
    miesiac-=20
  elif 40<miesiac<53:
    rok+=2100
    miesiac-=40
  elif 60<miesiac<73:
    rok+=2200
    miesiac-=60
  elif 80<miesiac<93:
    rok+=1800
    miesiac-=80

  
  if data.year != rok:
    raise ValueError("niepoprawny rok")

  if data.month != miesiac:
    raise ValueError("niepoprawny miesiac")
 
  if data.day != dzien:
    raise ValueError("niepoprawny dzien")
 
  if plec_liczba%2:
    
    if plec != 'mezczyzna':
      raise ValueError("niepoprawna liczba z oznaczeniem plci") 
  else:
    if plec != 'kobieta':
        raise ValueError("niepoprawna liczba z oznaczeniem plci")
 

  waga = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
  suma = 0 
  for i in range(10):
    suma+= waga[i]*int(pesel[i])
    
  suma %=10
  suma = 10 - suma 
  suma %=10
  if suma != kontrolna:
    raise ValueError("niepoprawna liczba kontrolna")
  return True

try:
  czy_poprawny( '02070803628' , datetime.date(1902, 7, 8) , 'kobieta')
  print("pesel ok")
except ValueError as error:
  print(error)
try:
  czy_poprawny( '02270803624' , datetime.date(2002, 7, 8) , 'kobieta')
  print("pesel ok")
except ValueError as error:
  print(error)
try:
  czy_poprawny( '02270812350' , datetime.date(2002, 7, 8) , 'mezczyzna')
  print("pesel ok")
except ValueError as error:
  print(error)

######2##########
def czy_przestepny(rok):
  if rok%100!=0 and rok%4 == 0:
    return True
  if rok%400 == 0:
    return True
  return False

def srednia(nazwa, tryb):
  wiek = []
  with open(nazwa, "r") as pl:
    t= pl.readlines()
  for data in t:
    data = data.split(' ')
    if len(data) != 3:
      if tryb == 'restrykcyjny':
        raise ValueError("brak jakiejs danej w dacie")
    else:  
      dzien = int(data[0])
      miesiac = int(data[1])
      rok =int(data[2])
      if miesiac == 2 and dzien == 29 and not czy_przestepny(rok) :        
          if tryb == 'restrykcyjny':
            raise ValueError("za duzo dni w lutym i rok nie przestepny")
      elif miesiac ==2 and dzien>29:
        if tryb == 'restrykcyjny':
            raise ValueError("za duzo dni w lutym")
      elif miesiac in [1,3,5,7,8,10,12] and dzien >31:
          if tryb == 'restrykcyjny':
            raise ValueError("za duzo dni w miesiacu")
      elif miesiac in [4,6,9,11] and dzien >30:
        if tryb == 'restrykcyjny':
            raise ValueError("za duzo dni w miesiacu")
      else:
        w=0
        if miesiac > 5:
            w = 2020 - rok
        elif miesiac == 5:
          if dzien >5:
            w = 2020 -rok
          else:
            w = 2021-rok
        else:
            w = 2021 - rok
        wiek.append(w)
  srednia =0
  for i in wiek:
    srednia += i
  srednia = srednia/len(wiek)
  return(srednia)

try:
  print(srednia('daty.in', 'restrykcyjny'))
except ValueError as error:
  print(error) 
print(srednia('daty.in', 'liberalny'))


################3################

def pitagorejska(lista, n):
  if len(lista) < n:
    raise ValueError("n wieksze od dlugosci listy")
  ilosc = 0
  for i in range(len(lista)-n+1):
    suma = 0
    powinno = lista[i+n-1]**2
    #print(powinno)
    np = 0
    for j in range(n-1):
      suma+=lista[i+j]**2
      if lista[i+j]%2:
        np+=1
      #print(suma)
    if suma == powinno:
      ilosc +=1
      print("Ta trojka/czworka ma:", np, " liczb nieparzystych")

  if ilosc == 0:
    raise ValueError("nie ma trojek/czworek w tej liscie")
  else:
    print("W tej liscie jest ", ilosc, "trojek/czworek")


l1=[1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29,2]
l2=[1,2,2,3,2,3,6,7,1,4,8,9,4,4,7,9,2,6,9,13,6,6,7,11,3,4,12,13,2,5,14,15,2,10,11,15,1,12,12,17,8,9,12,17,1,6,18,19,6,6,17,19,6,10,15,21,4,5,20,21,4,8,19,21,4,13,16,21,8,11,16,21,3,6,22,23,3,13,18,23,6,13,18,23,9,14,20,25,12,15,16,25,2,7,26,27,2,10,25,27,2,14,23,27,7,14,22,27,10,10,23,27,3,16,24,29,11,12,24,29,12,16,21,29]
l3=[3,4,5,5,12,13,7,24,25,9,40,41,6,8,10,60,80,100,18,24,30,15,8,17]
l4=[1,2,3,4,5,6,7,8,9]

print("\nTrojki\n")
print("\nl1:  ")
try:
  pitagorejska(l1, 3)
except ValueError as error:
  print(error) 
print("\nl2:  ")
try:
  pitagorejska(l2, 3)
except ValueError as error:
  print(error) 
print("\nl3:  ")
try:
  pitagorejska(l3, 3)
except ValueError as error:
  print(error) 
print("\nl4:  ")
try:
  pitagorejska(l4, 3)
except ValueError as error:
  print(error) 

print("\nCzworki\n")
print("\nl1:  ")
try:
  pitagorejska(l1, 4)
except ValueError as error:
  print(error) 
print("\nl2:  ")
try:
  pitagorejska(l2, 4)
except ValueError as error:
  print(error) 
print("\nl3:  ")
try:
  pitagorejska(l3, 4)
except ValueError as error:
  print(error) 
print("\nl4:  ")
try:
  pitagorejska(l4, 4)
except ValueError as error:
  print(error) 