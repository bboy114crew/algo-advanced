# Bytelandian gold coins
import math
dp = [-1 for _ in range(int(1e7))] 
 
def cal(n):
  if n < 3:
    return n
  if n < 1e7 and dp[n] != -1:
    return dp[n]
 
  result = max(cal(math.floor(n / 2)) + cal(math.floor(n / 3)) + cal(math.floor(n / 4)), n)
 
  if n < 1e7:
    dp[n] = result
 
  return result
 
while True:
  try:
    n = int(input())
    print(cal(n))
  except EOFError:
    break
