# # Aish And XOR
# N = int(input())

# S = list(map(int, input().split()))

# f = [0 for _ in range(N + 1)]

# for i in range(0, N):
#   f[i + 1] = f[i] + (S[i] == 1)

# Q = int(input())

# for _ in range(Q):
#   L, R = list(map(int, input().split()))
#   numOne = f[R] - f[L - 1]

#   numZero = (R - L + 1) - numOne
#   # 0^0^..^0^0 = 0 and 1^1 = 0 and 1^0 = 1
#   if numOne % 2 == 1:
#     xorSum = 1
#   else:
#     xorSum = 0
#   print(xorSum, numZero)

# # Mattey Multiplication
# T = int(input())

# for _ in range(T):
#   N, M = list(map(int, input().split()))

#   m_to_decimal = bin(M).replace("0b", "")

#   result = ''

#   len_a = len(m_to_decimal) - 1
#   index = 0
#   numOne = 0
#   while len_a >= 0:
#     if m_to_decimal[index] == '1':
#       numOne += 1
#       if numOne == 1:
#         result = result + '(' + f'{N}' + '<<' + f'{len_a}' + ')'
#       else:
#         result = result + ' + ' + '(' + f'{N}' + '<<' + f'{len_a}' + ')'
        
#     len_a -= 1
#     index += 1
#   print(result)

# Brexit Negotiations
"""
Đề bài có thể được trình bày lại một cách ngắn gọn như sau, cho một đồ thị DAG với mỗi đỉnh uu có trọng số là e[u]. Yêu cầu tìm một thứ tự Topo π sao cho giá trị: max(e[π[i]]+i) là nhỏ nhất trong các thứ tự Topo thỏa mãn.

Ta có nhận xét là các cuộc họp được thực hiện sau nên có e[u] càng nhỏ càng tốt. Do đó ta thực hiện việc sắp xếp Topo từ cuối về đầu. Tại mỗi bước chọn cuộc họp cho thời điểm thứ ii, ta chọn cuộc họp có trọng số nhỏ nhất trong các ứng cử viên có thể lựa chọn. Để làm tốt việc này, ta chỉ cần thay thế queue hoặc stack trong thuật toán sắp xếp Topo thành priority_queue để tại mỗi bước chọn ta có thể lấy ra nhanh chóng đỉnh thỏa mãn và có trọng số nhỏ nhất.

Độ phức tạp tính toán: O((N+M)*log(n)).
"""
# from heapq import heappush, heappop

# n = int(input())

# d_e = [0 for i in range(n + 1)]

# graph = [[] for i in range(n + 1)]
# result = []

# for i in range(n):
#   e, d, *b = list(map(int, input().split()))
#   d_e[i + 1] = e
#   for j in range(d):
#     graph[i + 1].append(b[j])

# def topological_sort_using_kahn(graph, result):
#   in_degree = [0 for _ in range(n + 1)]

#   zero_in_degree = []

#   # Tính bậc vào của từng đỉnh đỉnhh
#   for u in range(1, n + 1):
#     for v in graph[u]:
#       in_degree[v] += 1

#   # Tìm các đỉnh có bậc vào là 0
#   for i in range(1, n + 1):
#     if (in_degree[i] == 0):
#       heappush(zero_in_degree, (d_e[i], i))
  
#   i = n - 1
#   ans = -1

#   # Thực hiện thuật toán Kahn
#   while (len(zero_in_degree)):
#     ei, u = heappop(zero_in_degree)
#     result.append(u)
#     cost = d_e[u] + i;
#     i -= 1
#     ans = max(ans, cost);
#     # Mapping u with position in result
#     for v in graph[u]:
#       in_degree[v] -= 1
#       if (in_degree[v] == 0):
#         heappush(zero_in_degree, (d_e[v], v))
  
#   print(ans)

# topological_sort_using_kahn(graph, result)

# Samu and her Birthday Party
"""
Ý tưởng: Duyệt qua tất cả các cách chọn món ăn có thể có từ KK món ăn được cho và kiểm tra xem cách chọn đó có thỏa yêu cầu mỗi người đều có một món ăn yêu thích hay không. Nếu có thì đó là một cách chọn hợp lệ. Ta chọn cách chọn nào có ít món ăn nhất trong các cách chọn hợp lệ này.

Cho rằng mỗi cách chọn sẽ được biểu diễn bằng một dãy bit 00 và 11. Trong đó, bit 11 tại vị trí xx nghĩa là ta sẽ chọn món ăn thứ xx vào menu. Như vậy, để phát sinh ra tất cả các cách chọn món ăn từ K món ăn được cho, ta chỉ việc duyệt qua các dãy bit 000...001, 000...010, 000...011, ..., 111...111, tương ứng với các số từ 11 đến 2^K −1.

Các món ăn yêu thích của một người cũng được biểu diễn bằng một dãy bit 00 và 11. Do đó để kiểm tra xem cách chọn hiện tại có bao gồm ít nhất một món ăn yêu thích của người đó hay không, ta chỉ việc AND hai dãy bit với nhau. Nếu kết quả khác 00 là đúng.

Tìm số lượng bit 11 nhỏ nhất trong số các dãy bit của những cách chọn hợp lệ chính là kết quả của bài toán.

Độ phức tạp: O(T * 2^K * (N + log(K))) với T là số lượng bộ test, N là tổng số bạn của Samu và K là số món ăn có sẵn cần chọn. Trong đó, với mỗi bộ test:

O(N * K) là chi phí chuyển chuỗi các món ăn yêu thích của N người bạn thành NN dãy bit.
O(2^K * (N + log(K))) là chi phí tìm ra tất cả các dãy bit tương ứng với các cách chọn phù hợp thỏa yêu cầu và tính số bit 11 trong dãy bit hợp lệ để cho ra dãy bit có ít bit 11 nhất.
"""

# t = int(input())
# for _ in range(t):
#   n, k = list(map(int, input().split()))
#   dishes = list()
#   select = list()
#   for i in range(n):
#     dishes.append(input())
#   # Translate string to bit style number
#   for i in range(n):
#     a = 0
#     for j in range(k):
#       if dishes[i][j] == '1':
#         a = a | (1 << (k-1-j))
#     select.append(a)
#   # Brute force all possible plan
#   result = k
#   for i in range(1, 1 << k):
#     correct = True
#     for j in range(n):
#       if (select[j] & i) == 0:
#         correct = False
#     if correct:
#       count = 0
#       mask = i
#       # Count 1-bit in i
#       while mask:
#         if mask % 2 == 1:
#           count += 1
#         mask //= 2
#       result = min(result, count)
#   print(result)

# Sansa and XOR
"""
Ta có 3 ⊕ 3 = 0 và 3 ⊕ 3 ⊕ 3 = 3.
Từ đó ta có nhận xét sau nếu XOR n lần a với nhau:
Nếu n lẻ thì kết quả là a
Nếu n chẳn thì kết quả là 0
"""
T = int(input())
for _ in range(T):
  n = int(input())
  arr = list(map(int, input().split()))
  if n % 2 == 1:
    result = arr[0]
  else:
    result = 0
  
  for i in range(1, n):
    if (n - i)*(i + 1) % 2 == 1:
      result = result ^ arr[i]
    else:
      result = result ^ 0

  print(result)

# # Online Courses in BSU
# import sys
# sys.setrecursionlimit(100000)

# def dfs(u, graph, res, visited):
#   cycle = False
  
#   if visited[u] == 0:
#     visited[u] = 0
#     for v in graph[u]:
#       cycle = cycle or dfs(v, graph, res, visited)
#     # visited[u] == 2, đỉnh u đã được thăm bởi 1 đường đi trước đó
#     visited[u] = 2
#     res.append(u + 1)
#   # Đỉnh đang được thăm trên đường đi hiên tại
#   elif visited[u] == 1:
#     cycle = True
#   return cycle


# def schedule(n, graph, needed_courses, visited):
#   cycle = False
#   res = []
#   for u in needed_courses:
#     if dfs(u, graph, res, visited):
#       cycle = True
#       break

#   if cycle:
#     return -1
  
#   return res
# if __name__ == '__main__':
#   n, k = list(map(int, input().split()))
#   needed_courses = list(map(int, input().split()))

#   visited = [0 for _ in range(n)]

#   graph = [[] for _ in range(n)]

#   for i in range(n):
#     t, *course = list(map(int, input().split()))
#     for c in course:
#       graph[i].append(c - 1)

#   res = schedule(n, graph, needed_courses, visited)
#   if res == -1:
#     print(res)
#   else:
#     print(len(res))
#     print(' '.join(map(str, res)))
