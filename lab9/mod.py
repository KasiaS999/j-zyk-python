#1

def tri_pascal(n):
  ''' funkcja tworzaca trojkat Pascala '''
  t = [[0 for i in range(n)] for _ in range(n)]
  for line in range(n):
    for _ in range(n-line):
      print(" ", end = "")

    for i in range(line+1):
      if i == 0 or i is line:
        t[line][i]= 1
      else:
        t[line][i] = t[line -1][i] + t[line-1][i-1]

      print(f" {t[line][i]} ", end = "")
    print("\n",end = "")
  
    
#2

def euler(n, k):
  ''' funkcja rekurencyjna liczaca wartosci w trojkacie Pascala '''
  if n == 0 and k == 0:
    return 1
  elif k == 0:
    return 1
  elif k is n:
    return 0
  else:
    return (k+1)*euler(n-1, k) + (n-k)*euler(n-1, k-1)

def tri_euler(n):
  ''' funkcja tworzaca trojkat Eulera '''
  t = [[0 for i in range(n+1)] for _ in range(n+1)]
  for line in range(n+1):
    for i in range(line+1):
      t[line][i] = euler(line, i)
      print(f" {t[line][i]} ", end = "")
    print("\n",end = "")
    

#3

def cezar_kod(nazwa, przesuniecie):
  '''funkcja kodujaca plik szyfrem cezara, zapisujaca wynik do pliku'''
  dl_alfabetu = 26
  male = 'abcdefghijklmnopqrstuvwxyz'
  duze = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  zakodowany = ""
  
  with open(nazwa, "r") as f:
    text = f.read()
    for l in text:
      if l.isalpha():
        if l.isupper():
          pozycja = duze.index(l)
          pozycja+=przesuniecie
          if pozycja >= dl_alfabetu:
            pozycja-=dl_alfabetu
          zakodowany += duze[pozycja]
        if l.islower():
          pozycja = male.index(l)
          pozycja+=przesuniecie
          if pozycja >= dl_alfabetu:
            pozycja-=dl_alfabetu
          zakodowany += male[pozycja]
      else:
        zakodowany += l
  with open("zakodowane.txt", "w") as f:
    f.write(zakodowany)  

#4

def cezar_odkod(nazwa, przesuniecie):
  ''' funkcja dekodujaca plik zakodowany szyfrem cezara, zapisujaca wynik do pliku'''
  dl_alfabetu = 26
  male = 'abcdefghijklmnopqrstuvwxyz'
  duze = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  odkodowany = ""
  
  with open(nazwa, "r") as f:
    text = f.read()
    for l in text:
      if l.isalpha():
        if l.isupper():
          pozycja = duze.index(l)
          pozycja-=przesuniecie
          if pozycja < 0:
            pozycja+=dl_alfabetu
          odkodowany += duze[pozycja]
        if l.islower():
          pozycja = male.index(l)
          pozycja-=przesuniecie
          if pozycja < 0:
            pozycja+=dl_alfabetu
          odkodowany += male[pozycja]
      else:
        odkodowany += l
  with open("odkodowane.txt", "w") as f:
    f.write(odkodowany)  

#5
def czest(nazwa):
  '''funkcję dekodującą plik z wykorzystaniem tabeli częstości, na podstawie zaszyfrowanego pliku'''
  #czestosc wystepowania liter 
  male = 'abcdefghijklmnopqrstuvwxyz'
  wszystkie = 0
  litery = {}
  for i in male:
    litery.setdefault(i, 0)


  with open(nazwa, "r") as f:
    text = f.read()
    for lit in text:   
      if lit.isalpha():
        wszystkie += 1
        lit = lit.lower();
        litery[lit] += 1
    for i in male:
      litery[i] = litery[i]/wszystkie *100
    #print(litery)    

    l = []
    for i in male:
      l.append(litery[i])
    l.sort()
    #print(l)


  czestosci = ""
  with open("czestosci.txt", "r") as f:
    czestosci = f.readlines()
  #print(czestosci)
  print(czestosci[1].split("\t")[1])
  litery2 = {}
  for i in range(len(czestosci)):
    litery2[czestosci[i].split("\t")[0]] = czestosci[i].split("\t")[1].split('\n')[0]
 
