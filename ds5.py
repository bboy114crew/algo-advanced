# # The Number on the Board
# k = int(input())
# n = str(input())

# digits = []
# curSum = 0

# for ch in n:
#   digits.append(int(ch))
#   curSum += int(ch)

# digits.sort()

# ans = 0

# while curSum < k:
#   curSum += 9 - digits[ans]
#   ans += 1

# print(ans)

# Roma and Changing Signs
"""
Để tổng lợi nhuận thu về là lớn nhất, ta sẽ thực hiện đổi dấu trên các số âm theo thứ tự từ bé đến lớn (vì khi đổi dấu số âm càng nhỏ thì kết quả thu được là một số dương càng lớn).
Nếu đã đổi dấu toàn bộ số âm mà vẫn chưa đủ k lần đổi dấu theo yêu cầu, ta xét:
Nếu số lần đổi dấu còn lại là chẵn, ta có thể giữ nguyên lợi nhuận hiện tại bằng cách thực hiện đổi dấu trên một số duy nhất bất kỳ.
Ngược lại nếu số lần đổi dấu còn lại là lẻ,
để lợi nhuận giảm đi ít nhất có thể ta sẽ thực hiện đổi dấu trên số nhỏ nhất hiện có trong dãy, tạm gọi là xx. Khi này, tổng lợi nhuận sẽ giảm đi một lượng là 2 * x.

Độ phức tạp: O(n) với nn là số lượng số nguyên trong dãy.
"""
# n, k = map(int, input().split())
# incomes = list(map(int, input().split()))

# res, min_income = 0, 100000

# for t in incomes:
# 	res += t
# 	min_income = min(min_income, abs(t))

# i, idx = 1, 0

# while (i <= k):
# 	if (idx >= n or incomes[idx] >= 0):
# 		break
# 	res += incomes[idx] * -2
# 	idx += 1
# 	i += 1

# if (i <= k):
# 	if ((i - k + 1) % 2 != 0):
# 		res -= min_income * 2
		
# print(res)

# Making Jumps
"""
Ta thấy rằng, để số ô không thể đến được là ít nhất, thì đường đi của con mã phải là dài nhất, như vậy nhiệm vụ ta cần chính là tìm được đường đi dài nhất của con mã.
Đệ quy DFS của chúng ta sẽ có cấu trúc như sau:

# Function DFS(int u, int v): 
# // u, v là tọa độ ô đang xét, tương tự như đỉnh v
#     visited[u][v] = true;
#     Duyệt các ô (x, y) kề với (u, v) theo quân mã:
#         nếu ô (x, y) trong giới hạn bàn cờ, có thể đến được và chưa duyệt:
#             DFS(x, y);
            
#     // Điểm thay đổi so với thuật DFS cơ bản
#     visited[u][v] = false // giải phóng đỉnh (u, v)
Tuy nhiên, trong quá trình duyệt, ta cần phải lưu lại được độ dài đường đi dài nhất của quân mã. Thì lúc này sẽ có 2 cách thực thi:

Thêm một tham số là cnt để lưu lại số bước đi khi đi đến ô (u, v) đang xét.
Tức hàm DFS sẽ được khai báo thành DFS(int u, int v, int cnt).
Thì sau mỗi bước duyệt đến ô (u, v) mình chỉ việt cập nhật lại result theo cnt (result khai báo ngoài hàm).
Biến hàm DFS thành hàm có giá trị trả về, và giá trị trả về của DFS(u, v) là độ dài đường đi dài nhất mà tính từ đỉnh (u, v).
Thì theo như cấu trúc hàm đã nêu ở trên, DFS(u, v) = max(DFS(x, y)) + 1 với mọi cặp (x,y) kề với (u, v) và có thể duyệt.
Để lấy kết quả ta chỉ việc gọi DFS(0,0).
Một lưu ý là nếu kết quả bằng 1, thì xuất ra “square”, còn lại thì xuất ra “squares”.

Độ phức tạp
Rất khó để đánh giá được độ phức tạp cụ thể cho một bài toán BackTracking.
Ở đây analysis chỉ đánh giá trong trường hợp xấu nhất có thể.
Với mỗi một ô có 8 trạng thái đến hoặc không đến, do đó độ phức tạp là O(8^{mn}).
Mỗi ô có 8 cách đi, nhưng những ô nào bị đánh dấu rồi sẽ không đi đến nữa.
"""
graph = [[False for _ in range(10)] for _ in range(10)]
direct = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
          (1, -2), (1, 2), (2, -1), (2, 1)]

def DFS(x, y):
  global graph
  path = 0
  graph[x][y] = False
  for i in range(8):
    ux = x + direct[i][0]
    uy = y + direct[i][1]
    if 0 <= ux < 10 and 0 <= uy < 10 and graph[ux][uy]:
      path = max(path, DFS(ux, uy))
  graph[x][y] = True
  return path + 1

test = 1
while True:
  area = 0
  graph = [[False for _ in range(10)] for _ in range(10)]

  case = list(map(int, input().split()))
  n = case.pop(0)
  if n == 0:
    break

  start_col = case[0]
  for _ in range(n):
    area += case[1]
    for i in range(case[1]):
      graph[_][case[0] + i] = True
    case = case[2:]

  result = area - DFS(0, start_col)
  if result == 1:
    print("Case {}, {} square can not be reached.".format(test, result))
  else:
    print("Case {}, {} squares can not be reached.".format(test, result))
  test += 1