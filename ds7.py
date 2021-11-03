# Dynamic Frog
def getMinimaxLeap(l, r):
  if l + 1 == r:
    return x[r] - x[l]
  leap = 0
  for i in range(l, r - 1):
    leap = max(leap, x[i + 2] - x[i])
  return leap

nTest = int(input())
for iTest in range(1, nTest + 1):
  n, D = map(int, input().split())
  isLarge = [False] * (n + 2)
  x = [0] * (n + 2)
  stones = input().split()
  for i in range(1, n + 1):
    s = stones[i - 1]
    isLarge[i] = s[0] == 'B'
    x[i] = int(s[2:])

  isLarge[0] = True
  x[0] = 0
  isLarge[n + 1] = True
  x[n + 1] = D

  ans = 0 
  lastLarge = 0
  for i in range(1, n + 2):
    if isLarge[i]:
      ans = max(ans, getMinimaxLeap(lastLarge, i))
      lastLarge = i
  print('Case {}: {}'.format(iTest, ans))