# The Number on the Board
k = int(input())
n = str(input())

digits = []
curSum = 0

for ch in n:
  digits.append(int(ch))
  curSum += int(ch)

digits.sort()

ans = 0

while curSum < k:
  curSum += 9 - digits[ans]
  ans += 1

print(ans)
