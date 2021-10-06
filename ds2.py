# Aish And XOR

N = int(input())

S = list(map(int, input().split()))

f = [0 for _ in range(N)]

if N > 1:
  if S[0] == 1:
    f[1] = 1 + (S[1] == 1)
  else:
    f[1] = 0 + (S[1] == 1)

  for i in range(2, N):
    f[i] = f[i - 1] + (S[i] == 1)

Q = int(input())

for _ in range(Q):
  L, R = list(map(int, input().split()))
  L -= 1
  R -= 1

  if N == 1:
    if S[0] == 1:
      print(1, 0)
    else:
      print(0, 1)
    continue
  numOne = f[R] - f[L]

  numZero = (R - L + 1) - numOne
  if numOne % 2 == 1:
    xorSum = 1
  else:
    xorSum = 0
  print(xorSum, numZero)
