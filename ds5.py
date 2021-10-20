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
n, k = map(int, input().split())
incomes = list(map(int, input().split()))

res, min_income = 0, 100000

for t in incomes:
	res += t
	min_income = min(min_income, abs(t))

i, idx = 1, 0

while (i <= k):
	if (idx >= n or incomes[idx] >= 0):
		break
	res += incomes[idx] * -2
	idx += 1
	i += 1

if (i <= k):
	if ((i - k + 1) % 2 != 0):
		res -= min_income * 2
		
print(res)
# a = list(map(int, input().split()))

# sorted_a = sorted(a)

# negative_a = sorted(list(filter(lambda ele: ele < 0, sorted_a)), reverse=True)
# positive_a = sorted(list(filter(lambda ele: ele >= 0, sorted_a)))

# len_ne = len(negative_a)
# len_po = len(positive_a)

# ans = 0

# if n == 1:
#   if k % 2 == 0:
#     ans = a[0]
#   else:
#     ans = a[0] * -1
# elif k <= len_ne:
#   for i in range(0, k):
#     sorted_a[i] = sorted_a[i] * -1
#   ans = sum(sorted_a)
# else:
#   if len_ne != 0:
#     new_count = k % len_ne
#     if new_count > 0:
#       for i in range(0, len_ne):
#         negative_a[i] = negative_a[i] * -1
#       new_a = negative_a + positive_a
#       sorted_new_a = sorted(new_a)
#       if new_count % 2 == 1:
#         sorted_new_a[0] = sorted_new_a[0] * -1
#       ans = sum(sorted_new_a)
#     else:
#       for i in range(0, len_ne):
#         negative_a[i] = negative_a[i] * -1
#       new_a = negative_a + positive_a
#       sorted_new_a = sorted(new_a)
#       if (k - len_ne) % 2 == 1:
#         sorted_new_a[0] = sorted_new_a[0] * -1
#       ans = sum(sorted_new_a)
#   else:
#     if k % 2 == 1:
#       a[0] = a[0] * -1
#     ans = sum(a)

# print(ans)
