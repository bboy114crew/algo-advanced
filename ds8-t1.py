# # Palindromic series
# T = int(input())

# characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# def isPalindrome(s):
#   return s == s[::-1]

# for i in range(T):
#   N = str(input())
#   N_word = ''
#   totalCh = 0
#   new_N = ''
#   for ch in N:
#     N_word += characters[int(ch)]
#     totalCh += int(ch)
#   q = totalCh // len(N)
#   r = totalCh % len(N)
#   for j in range(q):
#     new_N += N_word
#   if r != 0:
#     new_N = new_N + N_word[0:r]

#   if isPalindrome(new_N):
#     print('YES')
#   else:
#     print('NO')

# The Sultan's Successors
N = 8

valid_board = []

def print_solution(board):
  output = set()
  for i in range(N):
    for j in range(N):
      if board[i][j] == 1:
        output.add((i, j))
  valid_board.append(output)

def check(board, row, col):
  # check vertical
  for i in range(row):
    if board[i][col]:
      return False

  # check main diagonal
  i = row
  j = col
  while i >= 0 and j >= 0:
    if board[i][j]:
      return False
    i -= 1
    j -= 1

  # check secondary diagonal
  i = row
  j = col
  while j < N and i >= 0:
    if board[i][j]:
      return False
    i -= 1
    j += 1

  return True

def N_Queen(board, row):
  if row == N:
    print_solution(board)
    return True
  for j in range(N):
    # check if queen can be placed on chessboard
    if check(board, row, j) == True:
      # place this queen in board[row][j]
      board[row][j] = 1
      N_Queen(board, row + 1)
      # backtracking
      board[row][j] = 0
  return False

board = [[0] * N for _ in range(N)]

N_Queen(board, 0)

k = int(input())
for _ in range(k):
  graph = []
  for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)

  max_total = 0
  total = 0
  for i in range(len(valid_board)):
    total = 0
    for j in range(N):
      x, y = list(valid_board[i])[j]
      total += graph[x][y]
    if (total > max_total):
      max_total = total

  print("     " + str(max_total))
