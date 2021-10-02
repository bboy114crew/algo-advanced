# Topological Sorting
from heapq import heappush, heappop

n, m = map(int, input().split())

def topological_sort_using_kahn(graph, result):
  in_degree = [0 for i in range(n + 1)]
  zero_in_degree = []

  # Tính bậc vào của từng đỉnh đỉnhh
  for u in range(1, n + 1):
    for v in graph[u]:
      in_degree[v] += 1
  # Tìm các đỉnh có bậc vào là 0
  for i in range(1, n + 1):
    if (in_degree[i] == 0):
      heappush(zero_in_degree, i)
  # Thực hiện thuật toán Kahn
  while (len(zero_in_degree)):
    u = heappop(zero_in_degree)
    result.append(u)

    for v in graph[u]:
      in_degree[v] -= 1
      if (in_degree[v] == 0):
        heappush(zero_in_degree, v)
  
  if (len(result) < n):
    return False
  
  return True

graph = [[] for i in range(n + 1)]
result = []

for i in range(m):
  u, v = map(int, input().split())
  graph[u].append(v)

if (topological_sort_using_kahn(graph, result)):
  print(" ".join(str(r) for r in result))
else:
  print("Sandro fails.")
