import sys
#1

if len(sys.argv) < 2:
  print("Program uruchomiony bez parametrów")
  sys.exit()

s = ''.join(sys.argv[1:])
print(s)

#2
male = []
duze = []
cyfry =[]
nie_litery = []

for i in s:
  if i.isalpha():
    if i.islower():
      male.append(i)
    else:
      duze.append(i)
  else:
    if i.isdigit():
      cyfry.append(int(i))
    nie_litery.append(i)

print(male)
print(duze)
print(cyfry)
print(nie_litery)


#3
male2 = []
for i in male:
  if i not in male2:
    male2.append(i)
print(male2)
male3 = [ (i, male.count(i)) for i in male2]
print(male3)

#4
print(sorted(male3, key=lambda x: x[1], reverse = True))

#5
sam ='aeiouyAEIOUY'
a=0
b=0
for i in s:
  if i in sam:
    a+=1
  elif i.isalpha():
    b+=1
print(f'y={a}x+{b}')
cyfry2 = [(i, a*i+b) for i in cyfry]
print(cyfry2)

#6
x_sr = 0
y_sr = 0

for x,y in cyfry2:
  x_sr+=x
  y_sr+=y
x_sr=x_sr/len(cyfry2)
y_sr=y_sr/len(cyfry2)

D=0
a=0
for x,y in cyfry2:
  D += (x-x_sr)**2
  a += y*(x-x_sr)
  
a = a/D
b = y_sr -a*x_sr
print(f'y={a: .3f}x+{b: .3f}')
