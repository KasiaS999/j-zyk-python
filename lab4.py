import random
import string
#1
print('\nzad 1')
k = 10
l = [random.randrange(5*k) for _ in range(k)]
print(l)

dic = {}
for i in range(100):
  l_c = l[:]
  random.shuffle(l)
  a = 0
  for j in range(k):
    if l_c[j] == l[j]:
        a+=1
  if a in dic:
    dic[a] +=1
  else:
    dic[a] = 1 

print(dic)

#2
print('\nzad 2')
s = '.'.join(random.choices(string.ascii_lowercase, k=k) )
print(s)


#3
print('\nzad 3')
l = [random.randrange(20) for _ in range(100)]
print(l)
print('\n3.a')
#a  
dic_a = {}
for i,v in enumerate(l):
  dic_a.setdefault(v, []).append(i)
print(dic_a)
#b
print('\n3.b')
dic_b = {}
for i in l:
  dic_b.setdefault(i, []).append(l.index(i, (dic_b[i][-1]+1) if dic_b[i] else 0)) 
 
print(dic_b)

#4
print('\nzad 4')
dic ={}
for _ in range(1000):
  a = random.randint(100, 999999)
  s = str(a) 
  dic[a] = True if s == s[::-1] else False
print(dic)


#5
print('\nzad 5')
dic1 = {i: random.randrange(1, 100) for i in range(10)}
dic2 = {i: random.randrange(1, 100) for i in range(10)}
print('\ndic1')
print(dic1)
print('\ndic2')
print(dic2)

dic1 = { v: i for i,v in dic1.items()}
dic2 = { v: i for i,v in dic2.items()}

print('\ndic1 po zamianie')
print(dic1)
print('\ndic2 po zamianie')
print(dic2)
dic3 = {i : (dic1[i], dic2[i]) for i in dic1 if i in dic2 }

print('dic3')
print(dic3)