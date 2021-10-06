# # Topological Sorting
# from heapq import heappush, heappop

# n, m = map(int, input().split())

# def topological_sort_using_kahn(graph, result):
#   in_degree = [0 for i in range(n + 1)]
#   zero_in_degree = []

#   # Tính bậc vào của từng đỉnh đỉnhh
#   for u in range(1, n + 1):
#     for v in graph[u]:
#       in_degree[v] += 1
#   # Tìm các đỉnh có bậc vào là 0
#   for i in range(1, n + 1):
#     if (in_degree[i] == 0):
#       heappush(zero_in_degree, i)
#   # Thực hiện thuật toán Kahn
#   while (len(zero_in_degree)):
#     u = heappop(zero_in_degree)
#     result.append(u)

#     for v in graph[u]:
#       in_degree[v] -= 1
#       if (in_degree[v] == 0):
#         heappush(zero_in_degree, v)
  
#   if (len(result) < n):
#     return False
  
#   return True

# graph = [[] for i in range(n + 1)]
# result = []

# for i in range(m):
#   u, v = map(int, input().split())
#   graph[u].append(v)

# if (topological_sort_using_kahn(graph, result)):
#   print(" ".join(str(r) for r in result))
# else:
#   print("Sandro fails.")

# # Hierarchy
# import queue
# N, K = list(map(int, input().split()))
# graph = [[] for i in range(N + 1)]
# boss = dict()
# result = []

# for u in range(1, K + 1):
#   arr = list(map(int, input().split()))
#   first, rest = arr[0], arr[1:]
#   for v in rest:
#     graph[u].append(v)

# def topological_sort_using_kahn(graph, result):
#   in_degree = [0 for _ in range(N + 1)]
#   zero_in_degree = queue.Queue()
#   index = 0

#   # Tính bậc vào của từng đỉnh đỉnhh
#   for u in range(1, N + 1):
#     for v in graph[u]:
#       in_degree[v] += 1

#   # Tìm các đỉnh có bậc vào là 0
#   for i in range(1, N + 1):
#     if (in_degree[i] == 0):
#       zero_in_degree.put(i)
  
#   # Thực hiện thuật toán Kahn
#   while not zero_in_degree.empty():
#     u = zero_in_degree.get()
#     result.append(u)

#     # Mapping u with position in result
#     if len(result) == 1:
#       boss[u] = 0
#       index += 1
#     else:
#       boss[u] = result[index - 1]
#       index += 1

#     for v in graph[u]:
#       in_degree[v] -= 1
#       if (in_degree[v] == 0):
#         zero_in_degree.put(v)
  
#   sorted_boss = sorted(boss.items())

#   for r in sorted_boss:
#     print(r[1])

# topological_sort_using_kahn(graph, result)

# # Fox and Names
# import queue
# ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
# alpha_dict = dict()

# for i in range(len(ALPHABETS)):
#   alpha_dict[ALPHABETS[i]] = i

# n = int(input())

# graph = [[] for _ in range(len(ALPHABETS))]
# result = []
# authors = []

# def topological_sort_using_kahn(graph, result):
#   in_degree = [0 for _ in range(len(ALPHABETS))]
#   zero_in_degree = queue.Queue()

#   # Tính bậc vào của từng đỉnh đỉnhh
#   for u in range(0, len(ALPHABETS)):
#     for v in graph[u]:
#       in_degree[v] += 1

#   # Tìm các đỉnh có bậc vào là 0
#   for i in range(0, len(ALPHABETS)):
#     if (in_degree[i] == 0):
#       zero_in_degree.put(i)
  
#   # Thực hiện thuật toán Kahn
#   while not zero_in_degree.empty():
#     u = zero_in_degree.get()
#     result.append(chr(u + 97))

#     for v in graph[u]:
#       in_degree[v] -= 1
#       if (in_degree[v] == 0):
#         zero_in_degree.put(v)

#   if (len(result) < len(ALPHABETS)):
#     return False
  
#   return True

# for i in range(n):
#   author = input()
#   authors.append(author)

# current_index = 0

# while current_index < n - 1:
#   current_au = authors[current_index]
#   next_au = authors[current_index + 1]
  
#   loop_count = min(len(current_au), len(next_au))
#   for i in range(loop_count):
#     if current_au[i] != next_au[i]:
#       graph[alpha_dict[current_au[i]]].append(alpha_dict[next_au[i]])
#       break
#     if i == len(next_au) - 1 and len(next_au) < len(current_au):
#       print("Impossible")
#       exit()
#   current_index += 1

# if (topological_sort_using_kahn(graph, result)):
#   print("".join(str(r) for r in result))
# else:
#   print("Impossible")

# King's Path

import queue

limit = 10**9
mark = set()
dist = {}
dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

def calc(x, y):
  global limit
  val = x
  val = val * limit + y
  return val

x0, y0, x1, y1 = list(map(int, input().split()))
x0 -= 1
y0 -= 1
x1 -= 1
y1 -= 1
mark.add(calc(x0, y0))
mark.add(calc(x1, y1))

n = int(input())

for i in range(1, n + 1):
  r, a, b = map(int, input().split())
  r -= 1
  a -= 1
  b -= 1
  for j in range(a, b + 1):
    mark.add(calc(r, j))

def bfs():
  q = queue.Queue()

  start = calc(x0, y0)

  q.put(start)
  dist[start] = 0

  while not q.empty():
    u = q.get()
    x = u // limit
    y = u % limit

    for i in range(8):
      cx = x + dx[i]
      cy = y + dy[i]
      v = calc(cx, cy)
      if (0 <= cx < limit and 0 <= cy < limit and v in mark):
        if v not in dist:
          dist[v] = dist[u] + 1
          if v == calc(x1, y1):
            print(dist[v])
            return
          q.put(v)
  print(-1)

bfs()

# # Beverages
# import queue
# from heapq import heappush, heappop

# case = 0
# while True:
#   try:
#     case += 1
#     N = int(input())

#     graph = [[] for i in range(N)]
#     result = []

#     drink_dict = dict()

#     drink_num_dict = ['' for i in range(N)]

#     for i in range(N):
#       drink = input()
#       drink_dict[drink] = i
#       drink_num_dict[i] = drink

#     M = int(input())
#     for _ in range(M):
#       B1, B2 = list(map(str, input().split()))
#       graph[drink_dict[B1]].append(drink_dict[B2])
    
#     def topological_sort_using_kahn(graph, result):
#       in_degree = [0 for _ in range(N)]

#       # zero_in_degree = queue.Queue()

#       zero_in_degree = []

#       # Tính bậc vào của từng đỉnh đỉnhh
#       for u in range(0, N):
#         for v in graph[u]:
#           in_degree[v] += 1

#       # Tìm các đỉnh có bậc vào là 0
#       for i in range(0, N):
#         if (in_degree[i] == 0):
#           heappush(zero_in_degree, i)
      
#       # Thực hiện thuật toán Kahn
#       while (len(zero_in_degree)):
#         u = heappop(zero_in_degree)
#         result.append(u)
#         t = len(result) - 1

#         # Mapping u with position in result
#         for v in graph[u]:
#           in_degree[v] -= 1
#           if (in_degree[v] == 0):
#             heappush(zero_in_degree, v)

#     topological_sort_using_kahn(graph, result)
    
#     final = ''

#     for r in range(len(result)):
#       index = result[r]
#       final = final + " " + drink_num_dict[index]
#     print('Case #{}: Dilbert should drink beverages in this order:{}.'.format(case, final))
#     print()
#     input()
#   except EOFError:
#       break

# # Answer the boss!
# import queue

# T = int(input())
# for case in range(T):
#   N, R = list(map(int, input().split()))
#   graph = [[] for i in range(N)]
#   result = []
#   rank = [0 for i in range(N)]

#   for _ in range(R):
#     R1, R2 = list(map(int, input().split()))
#     graph[R2].append(R1)
  
#   def topological_sort_using_kahn(graph, result):
#     in_degree = [0 for _ in range(N)]
#     zero_in_degree = queue.Queue()

#     # Tính bậc vào của từng đỉnh đỉnhh
#     for u in range(0, N):
#       for v in graph[u]:
#         in_degree[v] += 1

#     # Tìm các đỉnh có bậc vào là 0
#     for i in range(0, N):
#       if (in_degree[i] == 0):
#         rank[i] = 1
#         zero_in_degree.put(i)
    
#     # Thực hiện thuật toán Kahn
#     while not zero_in_degree.empty():
#       u = zero_in_degree.get()
#       result.append(u)

#       # Mapping u with position in result
#       for v in graph[u]:
#         in_degree[v] -= 1
#         if (in_degree[v] == 0):
#           rank[v] = rank[u] + 1
#           zero_in_degree.put(v)
#   topological_sort_using_kahn(graph, result)

#   people_with_rank = dict()

#   for i in result:
#     people_with_rank[i] = rank[i]
#   print('Scenario #{}:'.format(case + 1))
#   list_data = []
#   for key in people_with_rank:
#     list_data.append((people_with_rank[key], key))
  
#   sorted_list = sorted(list_data, key=lambda element: (element[0], element[1]))

#   for (index, rank) in sorted_list:
#     print(index, rank)

# # Book of Evil
# import queue

# n, m , d = list(map(int, input().split()))

# p = list(map(int, input().split())) # p1, p2, ..., pm

# is_p = [False for _ in range(n)]

# for cur in p:
#   is_p[cur - 1] = True

# graph = [[] for _ in range(n)]

# for _ in range(n - 1):
#   a, b = list(map(int, input().split()))
#   graph[a - 1].append(b - 1)
#   graph[b - 1].append(a - 1)

# dist = [-1 for _ in range(n)]
# dist1 = [-1 for _ in range(n)]
# dist2 = [-1 for _ in range(n)]

# def bfs(graph, start, dist):
#   visited = [False for _ in range(n)]

#   q = queue.Queue()
#   visited[start] = True
#   q.put(start)
#   dist[start] = 0
#   while not q.empty():
#     u = q.get()
#     for v in graph[u]:
#       if (not visited[v]):
#         visited[v] = True
#         q.put(v)
#         dist[v] = dist[u] + 1
# bfs(graph, p[0] - 1, dist)
# v1 = p[0] - 1
# for i in range(0, n):
#   if is_p[i] and dist[i] > dist[v1]:
#     v1 = i

# bfs(graph, v1, dist)
# v2 = v1
# for i in range(0, n):
#   if is_p[i] and dist[i] > dist[v2]:
#     v2 = i

# bfs(graph, v1, dist1)
# bfs(graph, v2, dist2)

# result = 0

# for i in range(0, n):
#   if dist1[i] <= d and dist2[i] <= d:
#     result += 1

# print(result)