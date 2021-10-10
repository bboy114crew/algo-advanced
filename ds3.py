# # N-Queen
# N = 4 

# def print_solution(board):
#   for i in range(N):
#     for j in range(N):
#       print(board[i][j], end = ' ')
#     print()
#   print()

# def check(board, row, col):
#   # check vertical
#   for i in range(row):
#     if board[i][col]:
#       return False
    
#   # check main diagonal
#   i = row
#   j = col
#   while i >= 0 and j >= 0:
#     if board[i][j]:
#       return False
#     i -= 1
#     j -= 1

#   # check secondary diagonal
#   i = row
#   j = col
#   while j < N and i >= 0:
#     if board[i][j]:
#       return False
#     i -= 1
#     j += 1

#   return True

# def N_Queen(board, row):
#   if row == N:
#     print_solution(board)
#     return True
#   for j in range(N):
#     # check if queen can be placed on chessboard
#     if check(board, row, j) == True:
#       # place this queen in board[row][j]
#       board[row][j] = 1
#       N_Queen(board, row + 1)
#       # backtracking
#       board[row][j] = 0
#   return False

# board = [[0] * N for _ in range(N)]

# N_Queen(board, 0)

# # Permutations of string
# def permutations(s, l, r):
#   if l == r:
#     print(''.join(s))
#   else:
#     for i in range(l, r):
#       s[l], s[i] = s[i], s[l]
#       permutations(s, l + 1, r)
#       s[l], s[i] = s[i], s[l]

# s = list("ABCD")

# permutations(s, 0, len(s))

# Distinct Permutations Of String
def should_swap(s, start, end):
  for i in range(start, end):
    if s[i] == s[end]:
      return False
  return True

def distinct_permutations(s, l, r):
  if l >= r:
    print(''.join(s))
    return
  for i in range(l, r):
    check = should_swap(s, l, i)
    if check == True:
      s[l], s[i] = s[i], s[l]
      distinct_permutations(s, l + 1, r)
      s[l], s[i] = s[i], s[l]

s = list("AABB")
distinct_permutations(s, 0 , len(s))
