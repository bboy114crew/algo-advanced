# # Bytelandian gold coins
# import math
# dp = [-1 for _ in range(int(1e7))] 
 
# def cal(n):
#   if n < 3:
#     return n
#   if n < 1e7 and dp[n] != -1:
#     return dp[n]
 
#   result = max(cal(math.floor(n / 2)) + cal(math.floor(n / 3)) + cal(math.floor(n / 4)), n)
 
#   if n < 1e7:
#     dp[n] = result
 
#   return result
 
# while True:
#   try:
#     n = int(input())
#     print(cal(n))
#   except EOFError:
#     break

# # OR in Matrix
# """
# Đầu tiên, ta thấy rằng phần tử B_{ij} mang giá trị 11 khi tồn tại ít nhất một giá trị trên dòng i hoặc cột j của A bằng 1. Ngược lại thì B_{ij} sẽ bằng 00.

# Như vậy, ta có thể giải bài toán bằng cách sau:

# Giả sử ma trận A của ta ban đầu đều mang giá trị 1.
# Duyệt ma trận B, nếu tại một vị trí B_{ij} mà nó bằng 0 thì ta sẽ gán toàn bộ dòng i và cột j của A bằng 0.
# Kiểm tra lại xem ma trận A của ta có thể sinh ra được một ma trận giống B hay không.
# Để làm bước 3, gọi C là một ma trận được sinh ra từ ma trận A như đề bài đã nói. Sau khi có C, ta sẽ kiểm tra xem C có giống B hay không.
# Ở đây, ta có thể sử dụng Hash Table để so sánh giá trị hash của từng dòng trong B và C có giống nhau hay không.
# Nếu B không giống với C thì ta in ra “NO”. Ngược lại thì ta in ra “YES” và mảng A.

# Độ phức tạp: O(n * m * (n + m)) với n là số cột và m là số dòng của ma trận.
# """

# def rs_hash(keys):
#   a = 63689
#   b = 378551
#   hash_value = 0
#   for i in range(len(keys)):
#     hash_value = hash_value * a + keys[i] & 0x7FFFFFFF
#     a = a * b
#   return hash_value & 0x7FFFFFFF

# m, n = list(map(int, input().split()))
# a = [[1 for _ in range(n)] for _ in range(m)]

# b = []

# for _ in range(m):
#   b_i = list(map(int, input().split()))
#   b.append(b_i)

# for i in range(m):
#   for j in range(n):
#     if b[i][j] == 0:
#       for k in range(m):
#         a[k][j] = 0
#       for k in range(n):
#         a[i][k] = 0

# correct = True
# for i in range(m):
#   for j in range(n):
#     if b[i][j] == 1:
#       found = False
#       for k in range(m):
#         if a[k][j] == 1:
#           found = True
#       for k in range(n):
#         if a[i][k] == 1:
#           found = True
      
#       if not found:
#         correct = False

# if (correct):
#   print("YES")
#   for i in range(m):
#     print(" ".join(str(r) for r in a[i]))
# else:
#   print("NO")

# 
"""
Với N = 1, thì kết quả chắc chắn là KK. Đối với các trường hợp còn lại:

Giả sử, ta có các số biễu diễn dưới dạng cơ số KK với chiều dài ii. Vậy ta có thể tạo được bao nhiêu số cơ số KK chiều dài i + 1?
Chiều dài tăng thêm 11 có nghĩa là chúng ta cần thêm 1 chữ số nữa (các chữ số bao gồm 0,1,2,...,K - 1) vào các số có độ dài i với cơ số K thỏa mãn yêu cầu đề bài.
Nếu số kết thúc là 00 thì ta có thể thêm một trong (K - 1) số từ 00 đến K - 1, ngược lại thì ta có thể thêm một trong (K - 2) số từ 11 đến K - 1.
Lúc này chúng ta cần dùng 2 mảng một chiều gồm các cặp endNot0 và endWith0 với:

endNot0[i] là số lượng chữ số chiều dài ii cơ số K và kết thúc là một số khác 0.
endWith0[i] là số lượng chữ số chiều dài ii cơ số K và kết thúc là 0.
Chúng ta có thể thấy số endWith0[i+1] = endNot0[i] vì ta chỉ được thêm 1 số 0 vào sau những số có độ dài i mà chữ số cuối cùng khác 0.
Còn endNot0[i+1] = (endNot0[i] + endWith0[i]) * (K-1) vì chúng ta có thể thêm bất kì chữ số khác 0 nào vào sau số có độ dài i đã có được.
Khi đó ta sẽ có được công thức:

endWith0[i] = endNot0[i - 1]
endNot0[i] = (endWith0[i - 1] + endNot0[i - 1]) * (K- 1)
Kết quả cuối cùng thu được là: endNot0[N] + endWith0[N].
"""
N = int(input())
K = int(input())

if N == 1:
  print(K)
else:
  endWith0 = [0 for _ in range(20)]
  endNot0 = [0 for _ in range(20)]
  endNot0[1] = K - 1
  for i in range(2, N + 1):
    endWith0[i] = endNot0[i - 1]
    endNot0[i] = (endNot0[i - 1] + endWith0[i - 1]) * (K - 1)
  print(endNot0[N] + endWith0[N])