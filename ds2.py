# Aish And XOR

N = int(input())

S = list(map(int, input().split()))

f = [0 for _ in range(N + 1)]

for i in range(0, N):
  f[i + 1] = f[i] + (S[i] == 1)

Q = int(input())

for _ in range(Q):
  L, R = list(map(int, input().split()))
  numOne = f[R] - f[L - 1]

  numZero = (R - L + 1) - numOne
  # 0^0^..^0^0 = 0 and 1^1 = 0 and 1^0 = 1
  if numOne % 2 == 1:
    xorSum = 1
  else:
    xorSum = 0
  print(xorSum, numZero)
