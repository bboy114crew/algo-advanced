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

# Fox and Names
import queue
ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
alpha_dict = dict()

for i in range(len(ALPHABETS)):
  alpha_dict[ALPHABETS[i]] = i

n = int(input())

graph = [[] for _ in range(len(ALPHABETS))]
result = []
authors = []

def topological_sort_using_kahn(graph, result):
  in_degree = [0 for _ in range(len(ALPHABETS))]
  zero_in_degree = queue.Queue()

  # Tính bậc vào của từng đỉnh đỉnhh
  for u in range(0, len(ALPHABETS)):
    for v in graph[u]:
      in_degree[v] += 1

  # Tìm các đỉnh có bậc vào là 0
  for i in range(0, len(ALPHABETS)):
    if (in_degree[i] == 0):
      zero_in_degree.put(i)
  
  # Thực hiện thuật toán Kahn
  while not zero_in_degree.empty():
    u = zero_in_degree.get()
    result.append(chr(u + 97))

    for v in graph[u]:
      in_degree[v] -= 1
      if (in_degree[v] == 0):
        zero_in_degree.put(v)

  if (len(result) < len(ALPHABETS)):
    return False
  
  return True

for i in range(n):
  author = input()
  authors.append(author)

current_index = 0

while current_index < n - 1:
  current_au = authors[current_index]
  next_au = authors[current_index + 1]
  
  loop_count = min(len(current_au), len(next_au))
  for i in range(loop_count):
    if current_au[i] != next_au[i]:
      graph[alpha_dict[current_au[i]]].append(alpha_dict[next_au[i]])
      break
    if i == len(next_au) - 1 and len(next_au) < len(current_au):
      print("Impossible")
      exit()
  current_index += 1

if (topological_sort_using_kahn(graph, result)):
  print("".join(str(r) for r in result))
else:
  print("Impossible")
