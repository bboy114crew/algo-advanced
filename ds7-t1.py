# Palindromic series
T = int(input())

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def isPalindrome(s):
  return s == s[::-1]

for i in range(T):
  N = str(input())
  N_word = ''
  totalCh = 0
  new_N = ''
  for ch in N:
    N_word += characters[int(ch)]
    totalCh += int(ch)
  q = totalCh // len(N)
  r = totalCh % len(N)
  for j in range(q):
    new_N += N_word
  if r != 0:
    new_N = new_N + N_word[0:r]

  if isPalindrome(new_N):
    print('YES')
  else:
    print('NO')