def modular_exp(a, b, m):
  result = 1
  for i in range(1, b + 1):
    result *= a
    result %= m
  return result

# print(modular_exp(50, 100, 13))

def modular_exp_plus(a, b, m):
  result = 1
  a %= m

  while b > 0:
    # If b is odd, multiply a with result
    if b % 2 == 1:
      result = (result * a) % m
    # b must be even now
    b //= 2
    a = (a * a) % m
  
  return result

print(modular_exp_plus(50, 100, 13))

# # Drazil and His Happy Friends
# import math
# n, m = list(map(int, input().split()))
 
# happy_boy = [False] * n
# happy_girl = [False] * m
 
# nb, *b = list(map(int, input().split()))
# for i in b:
#   happy_boy[i] = True
 
# ng, *g = list(map(int, input().split()))
# for i in g:
#   happy_girl[i] = True
 
# numDay = 2 * n * m // math.gcd(n, m)
# for i in range(numDay):
#   id_boy = i % n
#   id_girl = i % m
#   if happy_boy[id_boy] == True or happy_girl[id_girl] == True:
#     happy_boy[id_boy] = happy_girl[id_girl] = True
 
# count = 0
# for i in range(n):
#   count += happy_boy[id_boy] == True
 
# for i in range(m):
#   count += happy_girl[id_girl] == True
 
# if count == n + m:
#   print('Yes')
# else:
#   print('No')