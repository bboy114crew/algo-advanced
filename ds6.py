# Drazil and His Happy Friends
import math
n, m = list(map(int, input().split()))
 
happy_boy = [False] * n
happy_girl = [False] * m
 
nb, *b = list(map(int, input().split()))
for i in b:
  happy_boy[i] = True
 
ng, *g = list(map(int, input().split()))
for i in g:
  happy_girl[i] = True
 
numDay = 2 * n * m // math.gcd(n, m)
for i in range(numDay):
  id_boy = i % n
  id_girl = i % m
  if happy_boy[id_boy] == True or happy_girl[id_girl] == True:
    happy_boy[id_boy] = happy_girl[id_girl] = True
 
count = 0
for i in range(n):
  count += happy_boy[id_boy] == True
 
for i in range(m):
  count += happy_girl[id_girl] == True
 
if count == n + m:
  print('Yes')
else:
  print('No')