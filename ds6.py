# def modular_exp(a, b, m):
#   result = 1
#   for i in range(1, b + 1):
#     result *= a
#     result %= m
#   return result

# # print(modular_exp(50, 100, 13))

def modular_exp_plus(a, b, m):
  result = 1
  a %= m

  while b > 0:
    # If b is odd, multiply a with result
    if b % 2 == 1: # Using bit b & 1
      result = (result * a) % m
    # b must be even now
    b //= 2 # Using bit b >>= 1
    a = (a * a) % m
  
  return result

# print(modular_exp_plus(50, 100, 13))

"""
Modular multiplicative inverse
Gọi x là nghịch đảo của b theo module m:
bx mod m = 1 or bx đồng dư với 1 mod m
"""

"""
Fermat's little theorem
If b is prime and b % m != 0 => b^(m - 1) % m = 1
"""

def modInverseUsingFermatLittle(b, m):
  res = modular_exp_plus(b, m - 2, m)
  if (res * b) % m == 1:
    return res
  return -1

"""
Euclidean algorithm
Với a,b là hai số nguyên, ta thực hiện chia a cho b được thương q, số dư r (r >= 0).
Tức là r = a - q * b, khi đó ta có:
if r == 0:
  gcd(a, b) = b
else:
  gcd(a, b) = gcd(b, r)
"""

def gcd(a, b):
  while b != 0:
    remainder = a % b
    a = b
    b = remainder
  return a

def extendedEuclid(b, m):
  result = []
  x1 = 1
  y1 = 0
  x2 = 0
  y2 = 1
  x3 = 1
  y3 = 0
  while m != 0:
    q = b // m
    r = b % m
    x3 = x1 - 1 * x2
    y3 = y1 - 1 * y2
    x1 = x2
    y1 = y2
    x2 = x3
    y2 = y3
    b = m
    m = r

  result.append(b)
  result.append(x1)
  result.append(y1)

def mod_inverse(b, m):
  result = extendedEuclid(b, m)
  gcd = result[0]
  x = result[1]
  y = result[2]
  if gcd != 1:
    print("Inverse doesn't exist")
  else:
    print("Modular multiplicative inverse is:", (x + m) % m)

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
def gcd(a, b):
  while b != 0:
    r = a % b
    a = b
    b = r
  return a

n, m = map(int, input().split())
b, *boys = list(map(int, input().split()))
g, *girls = list(map(int, input().split()))
happy_boys = [False] * n
happy_girls = [False] * m

for x in boys:
  happy_boys[x] = True

for x in girls:
  happy_girls[x] = True

res = n + m - b - g
lcm = n * m // gcd(n, m)

for i in range(2 * lcm):
  if happy_boys[i % n] + happy_girls[i % m] == 1:
    happy_boys[i % n] = happy_girls[i % m] = True
    res -= 1

print('Yes' if res == 0 else 'No')