# # Aish And XOR
# N = int(input())

# S = list(map(int, input().split()))

# f = [0 for _ in range(N + 1)]

# for i in range(0, N):
#   f[i + 1] = f[i] + (S[i] == 1)

# Q = int(input())

# for _ in range(Q):
#   L, R = list(map(int, input().split()))
#   numOne = f[R] - f[L - 1]

#   numZero = (R - L + 1) - numOne
#   # 0^0^..^0^0 = 0 and 1^1 = 0 and 1^0 = 1
#   if numOne % 2 == 1:
#     xorSum = 1
#   else:
#     xorSum = 0
#   print(xorSum, numZero)

# Mattey Multiplication
T = int(input())

for _ in range(T):
  N, M = list(map(int, input().split()))

  m_to_decimal = bin(M).replace("0b", "")

  result = ''

  len_a = len(m_to_decimal) - 1
  index = 0
  numOne = 0
  while len_a >= 0:
    if m_to_decimal[index] == '1':
      numOne += 1
      if numOne == 1:
        result = result + '(' + f'{N}' + '<<' + f'{len_a}' + ')'
      else:
        result = result + ' + ' + '(' + f'{N}' + '<<' + f'{len_a}' + ')'
        
    len_a -= 1
    index += 1
  print(result)