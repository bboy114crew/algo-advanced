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

# Hierarchy
import queue
N, K = list(map(int, input().split()))
graph = [[] for i in range(N + 1)]
boss = dict()
pos = [[] for i in range(N + 1)]
result = []

for u in range(1, K + 1):
  arr = list(map(int, input().split()))
  first, rest = arr[0], arr[1:]
  for v in rest:
    graph[u].append(v)

def topological_sort_using_kahn(graph, result):
  in_degree = [0 for _ in range(N + 1)]
  zero_in_degree = queue.Queue()
  index = 0

  # Tính bậc vào của từng đỉnh đỉnhh
  for u in range(1, N + 1):
    for v in graph[u]:
      in_degree[v] += 1

  # Tìm các đỉnh có bậc vào là 0
  for i in range(1, N + 1):
    if (in_degree[i] == 0):
      zero_in_degree.put(i)
  
  # Thực hiện thuật toán Kahn
  while not zero_in_degree.empty():
    u = zero_in_degree.get()
    result.append(u)

    # Mapping u with position in result
    if len(result) == 1:
      boss[u] = 0
      index += 1
    else:
      boss[u] = result[index - 1]
      index += 1

    for v in graph[u]:
      in_degree[v] -= 1
      if (in_degree[v] == 0):
        zero_in_degree.put(v)
  
  sorted_boss = sorted(boss.items())

  for r in sorted_boss:
    print(r[1])

topological_sort_using_kahn(graph, result)
