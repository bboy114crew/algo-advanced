# Aish And XOR

N = int(input())

S = list(map(int, input().split()))

f = [0 for _ in range(N)]

for i in range(1, N):
  f[i] = f[i - 1] + (S[i] == 1)

Q = int(input())

for _ in range(Q):
  L, R = list(map(int, input().split()))
  L -= 1
  R -= 1
  numOne = f[R] - f[L-1]

  numZero = (R - L + 1) - numOne

  

