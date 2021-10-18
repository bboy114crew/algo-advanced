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

# # Painting Fence
# import sys

# """
# Ta sẽ xem hàng rào như một phân đoạn các tấm ván [0, n-1][0,n−1].
# Sau đó, ta sẽ sơn lần lượt các đường theo chiều ngang từ dưới lên nhiều nhất có thể cho đến khi một đường sơn của chúng ta sẽ không thể sơn qua mọi tấm ván trong đoạn này nữa.
# Lúc này, chúng ta sẽ có các phần tấm ván chưa được sơn nằm tách biệt nhau.
# Ta sử dụng đệ quy để tính số lần sơn tối thiểu đối với các phần này và trả về tổng của chúng.
# Hàm tính số đường cọ tối thiểu strokesNeeded(left, right, paintedHeight) (left và right đại diện cho vị trí bắt đầu và kết thúc của phân đoạn đang xét, paintedHeight là chiều cao của phần ván trước đó đã được sơn):
# """

# def strokesNeeded(left, right, paintedHeight):
#   if left > right:
#     return 0
#   # Khởi tạo biến mini (dùng để lưu lại vị trí của miếng ván có độ cao nhỏ nhất) bằng left. Sau đó duyệt các phần tử từ left đến right để tìm vị trí phần tử nhỏ nhất.
#   mini = left + a[left:right+1].index(min(a[left:right+1]))
#   # Số đường sơn tính theo chiều dọc
#   allVerticle = right - left + 1
#   # Lúc này, số các đường sơn ngang tối đa mà ta có thể thực hiện là a[mini]- paintedHeight
#   """
#   Nếu một trong 2 đoạn [left, mini-1] hoặc [mini+1, right] rỗng thì ở lần đệ quy tiếp theo left > right và lần đệ quy đối với phân đoạn ấy sẽ trả về 0. Tức là:
#   Nếu [left, mini – 1] rỗng thì recursive = a[mini] - paintedHeight + 0 + strokesNeeded(mini + 1, right, a[mini])
#   Nếu [mini+1, right] rỗng thì recursive = a[mini] - paintedHeight + strokesNeeded(left, mini+1, a[mini]) + 0
#   Ngoài ra, ta còn phải kiểm tra xem rằng nếu ta sơn phân đoạn này hoàn toàn theo chiều dọc thì kết quả nhận được có nhỏ hơn là sơn ngang: allVertical = right - left + 1
#   Kết quả trả về sẽ là số nhỏ hơn trong hai cách sơn: return min(allVertical, recursive).
#   """
#   recursive = a[mini] - paintedHeight + strokesNeeded(left, mini - 1, a[mini]) + strokesNeeded(mini + 1, right, a[mini])

#   return min(allVerticle, recursive)
 
 
# sys.setrecursionlimit(10000)
 
# n = int(input())
# a = list(map(int, input().split()))

# print(strokesNeeded(0, n - 1, 0))

# Bit Maps

"""
Bài toán này sẽ giải chia thành 2 phần chính
Chuyển từ chuỗi loại B sang chuỗi loại D.
Ta đưa hết toàn bộ ký tự trong chuỗi s về thành một ma trận 22 chiều kích thước W * H.

Gọi hàm B2D(x, y, w, h) là hàm chuyển ma trận gồm các phần tử gồm các hàng đánh số từ x đến x + w - 1 và các cột đánh số từ y đến y + h - 1.

Trước hết, nếu như w = 0 hoặc h = 0, hiển nhiên ma trận này hoàn toàn không tồn tại, ta sẽ return về một chuỗi rỗng.

Nếu toàn bộ ký tự trong ma trận này bằng 0 hoặc bằng 1 thì ta return về chuỗi 0 hoặc 1 tương ứng. Ta có thể kiểm tra đoạn này trong O(W * H).

Ngược lại, ta sẽ tách ma trận này thành 44 ma trận con
B2D(x, y, (h + 1) / 2, (w + 1) / 2)

B2D(x, y + (w + 1) / 2, (h + 1) / 2, w / 2)

B2D(x + (h + 1) / 2, y, h / 2, (w + 1) / 2)

B2D(x + (h + 1) / 2, y + (w + 1) / 2, h / 2, w / 2)

Và ta return D ghép với 4 chuỗi của 4 ma trận con.

Đối với bài toán chuyển từ chuỗi loại D sang chuỗi loại B, ta thực hiện như sau:
Gọi D2B(A, x, y, w, h, is) là ta chuyển chuỗi s loại D sang ma trận nhị phân và đưa vào ma trận A, gồm các phần tử đánh số các hàng từ xx đến x+w-1 và từ y đến y+h-1. Phần tử của chuỗi s hiện tại ta xét là khi với hiện tại, ta đang nhập chúng vào bằng istream is.
Nếu như w = 0 hoặc h = 0 thì không làm gì ở hàm này nữa.
Nếu như ký tự đang xét hiện tại là 0 hoặc 1, ta điền toàn bộ các phần tử trong ma trận từ xx đến x+w-1x+w−1 và từ yy đến y + h - 1 toàn là số 0 và số 1 tương ứng.
Ngược lại là ký tự D, ta chia thành 4 ma trận con theo đúng cách chia ở trên và gọi lại hàm này. Kết quả là toàn bộ các ký tự trong ma trận A.
Độ phức tạp: Mỗi phần tử trong chuỗi s đều xét đúng 1 lần. Do đó, độ phức tạp là O(T * W * H) với T là số lượng test và W, H là kích thước của ma trận.
"""

# def get(x,y,h,w):
#   res = 0
#   for i in range(x,x+h):
#     for j in range(y,y+w):
#       if a[i][j] == '1':
#         res += 1
#   return res

# def B2D(x,y,h,w):
#   if h == 0 or w == 0:
#     return ""

#   sum = get(x,y,h,w)
  
#   if sum == 0:
#     return "0"
#   elif sum == h * w:
#     return "1"

#   s1 = B2D(x, y, (h + 1) // 2, (w + 1) // 2)
#   s2 = B2D(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
#   s3 = B2D(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
#   s4 = B2D(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)

#   return "D" + s1 + s2 + s3 + s4

# def D2B(x,y,h,w):
#   global string_it
#   if h == 0 or w == 0:
#     return

#   c = stream[string_it]
#   string_it += 1

#   if c == '1':
#     for i in range(x, x + h):
#       for j in range(y, y + w):
#         dest[i][j] = '1'
#     return 
#   elif c == '0':
#     for i in range(x, x + h):
#       for j in range(y, y + w):
#         dest[i][j] = '0'
#     return
  
#   D2B(x, y, (h + 1) // 2, (w + 1) // 2)
#   D2B(x, y + (w + 1) // 2, (h + 1) // 2, w // 2)
#   D2B(x + (h + 1) // 2, y, h // 2, (w + 1) // 2)
#   D2B(x + (h + 1) // 2, y + (w + 1) // 2, h // 2, w // 2)


# line = input()
# while True:
#   if line == '#':
#     break
#   line = line.split()
#   h = int(line[1])
#   w = int(line[2])
#   x = line[0]
#   iterator = 0
#   stream = ""
#   while True:
#     line = input()
#     if line == "#" or ' ' in line:
#       break
#     stream += line

#   if x == 'B':
#     a = [stream[i:i + w] for i in range(0, h * w, w)]
#     print('D', end = '')
#     res = B2D(0, 0, h, w)
#   else:
#     print('B',end='')
#     string_it = 0
#     dest = [ ['0' for i in range(w)] for j in range(h)]
#     D2B(0, 0, h, w)
#     res = ''.join([''.join(line) for line in dest])

#   print("%4d %3d" % (h, w))
#   l = len(res)
#   for i in range(l):
#     print(res[i],end='')
#     if (i + 1) % 50 == 0 or i == l - 1:
#       print()

# Tricky Function
"""
Ta nhận xét g(i,j)g(i,j) là tổng các phần tử mảng aa tại các vị trí từ min(i,j) + 1min(i,j)+1 đến max(i,j)max(i,j).
Gọi d[i] = a[1] + a[2] + ... + a[i].
Khi đó g(i,j) = d_{max(i,j)} - d_{min(i,j)}.
Từ đó, f(i,j) = (i - j)^2 + (d_{max(i,j)} - d_{min(i,j)})^2 = (i - j)^2 + (d[j] - d[i]) ^2

Ta nhận xét rằng f(i,j) chính là bình phương của khoảng cách giữa hai điểm (i,d_i) và (j,d_j) trên mặt phẳng tọa độ OxyOxy.

Với mỗi chỉ số i từ 1 đến n, ta thêm điểm có tọa độ (i,d_i). Sau đó, ta cần tìm cặp điểm có khoảng cách nhỏ nhất trong tập điểm này.
Đây là bài toán kinh điển, có thể giải được bằng phương pháp chia để trị trong O(n log n) với n là số lượng điểm trong tập điểm.
Độ phức tạp: O(n log n) với n là số phần tử của dãy số a.
"""

INF = int(1e9)
class Point:
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
 
 
def distance(p1, p2):
  x = p1.x - p2.x
  y = p1.y - p2.y
  return x*x + y*y
 
 
def bruteForce(point_set, left, right):
  min_dist = INF
  for i in range(left, right):
    for j in range(i+1, right):
      min_dist = min(min_dist, distance(point_set[i], point_set[j]))
  return min_dist
 
 
def stripClosest(point_set, left, right, mid, min_dist):
  point_mid = point_set[mid]
  splitted_points = []
  for i in range(left, right):
    if (point_set[i].x - point_mid.x) ** 2 <= min_dist:
      splitted_points.append(point_set[i])
  splitted_points.sort(key=lambda point: point.y)
  l = len(splitted_points)
  smallest = INF
  for i in range(l):
    for j in range(i+1, l):
      if (splitted_points[i].y - splitted_points[j].y) ** 2 >= min_dist:
        break
      d = distance(splitted_points[i], splitted_points[j])
      smallest = min(smallest, d)
  return smallest

 
def closestUtil(point_set, left, right):
  if right - left <= 3:
    return bruteForce(point_set, left, right)

  mid = (left + right) // 2
  dist_left = closestUtil(point_set, left, mid)
  dist_right = closestUtil(point_set, mid+1, right)
  dist_min = min(dist_left, dist_right)

  return min(dist_min, stripClosest(point_set, left, right, mid, dist_min))
 
 
n = int(input())
a = list(map(int, input().split()))
 
pref = [0]
for i in range(n):
  pref.append(pref[i] + a[i])
 
point_set = []
for i in range(n):
  point_set.append(Point(i, pref[i+1]))
 
ans = closestUtil(point_set, 0, n)

print(str(ans))