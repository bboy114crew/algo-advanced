# # Closest Pair of Points

# import math
# INF = 1e9

# class Point:
#   def __init__(self, x = 0, y = 0):
#     self.x = x
#     self.y = y
  
# def distance(p1, p2):
#   x = p1.x - p2.x
#   y = p1.y - p2.y
#   return (x * x + y * y) ** 0.5

# def brute_force(points, left, right):
#   min_dist = INF
#   for i in range(left, right):
#     for j in range(i + 1, right):
#       min_dist = min(min_dist, distance(points[i], points[j]))
#     return min_dist

# def strip_closest(point_set, left, right, mid, dist_min):
#   point_mid = point_set[mid]
#   splitted_points = []
#   for i in range(left, right):
#     if abs(point_set[i].x - point_mid.x) <= dist_min:
#       splitted_points.append(point_set[i])
  
#   splitted_points.sort(key=lambda p: p.y)
#   smallest = dist_min
#   l = len(splitted_points)
#   for i in range(0, l):
#     for j in range(i + 1, l):
#       if not (splitted_points[i].y - splitted_points[j].y) < smallest:
#         break
#       d = distance(splitted_points[i], splitted_points[j])
#       smallest = min(smallest, d)
#   return smallest

# def minimal_distance(point_set, left, right):
#   if right - left <= 3:
#     return brute_force(point_set, left, right)
#   mid = (right + left) // 2
#   dist_left = minimal_distance(point_set, left, mid)
#   dist_right = minimal_distance(point_set, mid + 1, right)
#   dist_min = min(dist_left, dist_right)
#   return min(dist_min, strip_closest(point_set, left, right, mid, dist_min))

# n = int(input())
# point_set = []
# for i in range(n):
#   x, y = map(int, input().split())
#   point_set.append(Point(x, y))

# point_set.sort(key=lambda point: point.x)
# ans = minimal_distance(point_set, 0, n)
# print("{}".format(ans))

# # The Closest Pair Problem
# import math
# INF = 1e9

# class Point:
#   def __init__(self, x = 0, y = 0):
#     self.x = x
#     self.y = y
  
# def distance(p1, p2):
#   x = p1.x - p2.x
#   y = p1.y - p2.y
#   return (x * x + y * y) ** 0.5

# def brute_force(points, left, right):
#   min_dist = INF
#   for i in range(left, right):
#     for j in range(i + 1, right):
#       min_dist = min(min_dist, distance(points[i], points[j]))
#     return min_dist

# def strip_closest(point_set, left, right, mid, dist_min):
#   point_mid = point_set[mid]
#   splitted_points = []
#   for i in range(left, right):
#     if abs(point_set[i].x - point_mid.x) <= dist_min:
#       splitted_points.append(point_set[i])
  
#   splitted_points.sort(key=lambda p: p.y)
#   smallest = dist_min
#   l = len(splitted_points)
#   for i in range(0, l):
#     for j in range(i + 1, l):
#       if not (splitted_points[i].y - splitted_points[j].y) < smallest:
#         break
#       d = distance(splitted_points[i], splitted_points[j])
#       smallest = min(smallest, d)
#   return smallest

# def minimal_distance(point_set, left, right):
#   if right - left <= 3:
#     return brute_force(point_set, left, right)
#   mid = (right + left) // 2
#   dist_left = minimal_distance(point_set, left, mid)
#   dist_right = minimal_distance(point_set, mid + 1, right)
#   dist_min = min(dist_left, dist_right)
#   return min(dist_min, strip_closest(point_set, left, right, mid, dist_min))

# while True:
#   n = int(input())
#   if n == 0:
#     exit()
#   point_set = []
#   for i in range(n):
#     x, y = map(int, input().split())
#     point_set.append(Point(x, y))
#   point_set.sort(key=lambda point: point.x)
#   ans = minimal_distance(point_set, 0, n)
#   if ans >= 10000:
#     print('INFINITY')
#   else:
#     print('{:.4f}'.format(ans))

# Painting Fence
import sys

"""
Ta sẽ xem hàng rào như một phân đoạn các tấm ván [0, n-1][0,n−1].
Sau đó, ta sẽ sơn lần lượt các đường theo chiều ngang từ dưới lên nhiều nhất có thể cho đến khi một đường sơn của chúng ta sẽ không thể sơn qua mọi tấm ván trong đoạn này nữa.
Lúc này, chúng ta sẽ có các phần tấm ván chưa được sơn nằm tách biệt nhau.
Ta sử dụng đệ quy để tính số lần sơn tối thiểu đối với các phần này và trả về tổng của chúng.
Hàm tính số đường cọ tối thiểu strokesNeeded(left, right, paintedHeight) (left và right đại diện cho vị trí bắt đầu và kết thúc của phân đoạn đang xét, paintedHeight là chiều cao của phần ván trước đó đã được sơn):
"""

def strokesNeeded(left, right, paintedHeight):
  if left > right:
    return 0
  # Khởi tạo biến mini (dùng để lưu lại vị trí của miếng ván có độ cao nhỏ nhất) bằng left. Sau đó duyệt các phần tử từ left đến right để tìm vị trí phần tử nhỏ nhất.
  mini = left + a[left:right+1].index(min(a[left:right+1]))
  # Số đường sơn tính theo chiều dọc
  allVerticle = right - left + 1
  # Lúc này, số các đường sơn ngang tối đa mà ta có thể thực hiện là a[mini]- paintedHeight
  """
  Nếu một trong 2 đoạn [left, mini-1] hoặc [mini+1, right] rỗng thì ở lần đệ quy tiếp theo left > right và lần đệ quy đối với phân đoạn ấy sẽ trả về 0. Tức là:
  Nếu [left, mini – 1] rỗng thì recursive = a[mini] - paintedHeight + 0 + strokesNeeded(mini + 1, right, a[mini])
  Nếu [mini+1, right] rỗng thì recursive = a[mini] - paintedHeight + strokesNeeded(left, mini+1, a[mini]) + 0
  Ngoài ra, ta còn phải kiểm tra xem rằng nếu ta sơn phân đoạn này hoàn toàn theo chiều dọc thì kết quả nhận được có nhỏ hơn là sơn ngang: allVertical = right - left + 1
  Kết quả trả về sẽ là số nhỏ hơn trong hai cách sơn: return min(allVertical, recursive).
  """
  recursive = a[mini] - paintedHeight + strokesNeeded(left, mini - 1, a[mini]) + strokesNeeded(mini + 1, right, a[mini])

  return min(allVerticle, recursive)
 
 
sys.setrecursionlimit(10000)
 
n = int(input())
a = list(map(int, input().split()))

print(strokesNeeded(0, n - 1, 0))