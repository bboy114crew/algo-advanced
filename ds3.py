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

# # Distinct Permutations Of String
# def should_swap(s, start, end):
#   for i in range(start, end):
#     if s[i] == s[end]:
#       return False
#   return True

# def distinct_permutations(s, l, r):
#   if l >= r:
#     print(''.join(s))
#     return
#   for i in range(l, r):
#     check = should_swap(s, l, i)
#     if check == True:
#       s[l], s[i] = s[i], s[l]
#       distinct_permutations(s, l + 1, r)
#       s[l], s[i] = s[i], s[l]

# s = list("0011")
# distinct_permutations(s, 0 , len(s))

# # Lotto
# def gen(arr, res, left, n, k):
#   if k == 0:
#     print(" ".join(str(arr[r]) for r in res))
#     return
#   for i in range(left, n):
#     res.append(i)
#     gen(arr, res, i + 1, n, k - 1)
#     res.pop()

# while True:
#   n, *arr = list(map(int, input().split()))
#   res = []
#   if n == 0:
#     break
  
#   gen(arr, res, 0, n, 6)

# # The Hamming Distance Problem
# def should_swap(s, start, end):
#   for i in range(start, end):
#     if s[i] == s[end]:
#       return False
#   return True

# def distinct_permutations(s, l, r):
#   if l >= r:
#     print(''.join(s))
#     return
#   for i in range(l, r):
#     check = should_swap(s, l, i)
#     if check == True:
#       s[l], s[i] = s[i], s[l]
#       distinct_permutations(s, l + 1, r)
#       s[l], s[i] = s[i], s[l]

# T = int(input())
# input()
# for case in range(T):
#   N, H = list(map(int, input().split()))
#   if case != T - 1:
#     input()
#   origin_string = []
#   for i in range(N):
#     if i < N - H:
#       origin_string.append(str(0))
#     else:
#       origin_string.append(str(1))
#   distinct_permutations(origin_string, 0 , len(origin_string))
#   print()

# Digger Octaves
# T = int(input())
# for _ in range(T):
#   N = int(input())
#   graph = []
#   visited = [[0 for _ in range(N)] for _ in range(N)]
#   container = []
#   for i in range(N):
#     row = input()
#     graph.append([*row])

#   m1 = [0 , 0 , -1 , 1]
#   m2 = [-1 , 1 , 0 , 0]

#   def countOctaves(n, r, c, num_of_oct, arr):
#     if(r < 0 or c < 0 or r > n - 1 or c > n - 1):
#       return
    
#     if(graph[r][c] == '.' or visited[r][c] == 1):
#       return
    
#     visited[r][c] = 1 ;

#     set_arr = set(arr)
#     set_arr.add(f'{r}{c}')
#     arr = list(set_arr)

#     if(num_of_oct == 8):
#       arr.sort()
#       container.append(arr)
#       visited[r][c] = 0
#       return
    
#     for i in range(4):
#       tempr = r + m1[i];
#       tempc = c + m2[i];
#       countOctaves(n, tempr, tempc, num_of_oct + 1, arr)
#     visited[r][c] = 0

#   for i in range(N):
#     for j in range(N):
#       list_square = []
#       countOctaves(N, i, j, 1, list_square)
  
#   result = set(tuple(i) for i in container)
#   print(len(result))
# Faster solution
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(sx, sy, step, bits):
  global octaves, graph, n, visited
  visited[sx][sy] = True
  bits |= 1 << (sx * n + sy)

  if step == 8:
    octaves.add(bits)
  else:
    for i in range(4):
      x, y = sx + dx[i], sy + dy[i]
      if x in range(n) and y in range(n) and not visited[x][y] and graph[x][y] == 'X':
        dfs(x, y, step + 1, bits)
              
  bits &= ~(1 << (sx * n + sy))
  visited[sx][sy] = False
    

t = int(input())
for _ in range(t):
  n = int(input())
  visited = [[False] * n for i in range(n)]
  graph = []
  octaves = set()

  for i in range(n):
    graph.append(input())
  
  for i in range(n):
    for j in range(n):
      if graph[i][j] == 'X':
        bits = 0
        dfs(i, j, 1, bits)

  print(len(octaves))