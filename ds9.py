# # Camp Schedule

# """
# Giả sử như xâu ss không thể tạo ra bất kì xâu t nào. Đáp là sẽ là một hoán vị bất kì của xâu s.
# Nhận xét 1: giả sử xâu kết quả không bắt đầu bằng xâu t, ta có thể chuyển các kí tự đầu về phía sau, như vậy xâu kết quả bắt đầu bằng xâu tt luôn không thể tệ hơn.
# Nhận xét 2: Trong xâu đáp án ta muốn sự xuất hiện của xâu t tiếp theo là càng gần đầu xâu càng tốt. Hay nói cách khác, ta cần xét xâu con chung dài nhất (độ dài nhỏ hơn độ dài t) của tiền tố xâu tt và hậu tố xâu t.
# Giả sử: xâu t = 10101, để xây dựng xâu t tiếp theo ta chỉ cần thêm 01 vào cuối, hay nói cách khác ta không cần thêm 101 là xâu chung dài nhất của tiền tố t và hậu tố t.

# Bước 1: Khởi tạo xâu t.
# Bước 2: Tìm xâu con chung dài nhất của tiền tố tt và hậu tố tt có độ dài maxPrefixDuplicate.
# Bước 3: Thêm vào kết quả đoạn hậu tố có độ dài (|t| - maxPrefixDuplicate + 1), nếu không đủ kí tự 0 hoặc 1 thì các kí tự cuối điền cho đủ số lượng.
# Độ phức tạp O(max(|s|, |t|)) với |s|, |t| là độ dài xâu s, t.
# """

# def CreatHash(s):
#     power[0] = 1
#     for i in range(len(s)):
#         hash[i + 1] = (hash[i] * BASE + ord(s[i])) % MOD
#         power[i + 1] = (power[i] * BASE) % MOD

# def GetHash(l, r):
#     return ((hash[r] - (hash[l - 1] * power[r - l + 1]) % MOD + MOD) % MOD)

# BASE = 29
# MOD = int(1e9) + 7
# maxn = int(5e5) + 100
# cnt = [0] * 2
# cntNeed = [0] * 2
# power = maxn * [0]
# hash = maxn * [0]
# st = ''
# s = input()
# t = input()
# n = len(s)
# m = len(t)
# for i in range(n):
#   cnt[ord(s[i]) - ord('0')] += 1
# for i in range(m):
#   cnt[ord(t[i]) - ord('0')] -= 1
# if cnt[0] < 0 or cnt[1] < 0:
#   print(s)
#   exit()
# CreatHash(t)
# MaxPrefixDuplicate = 0
# for len in range(m - 1, -1, -1):
#   if GetHash(1, len) == GetHash(m - len + 1, m):
#     MaxPrefixDuplicate = len
#     break 

# for i in range(MaxPrefixDuplicate, m):
#   cntNeed[ord(t[i]) - ord('0')] += 1
#   st += t[i]

# mNeed = m - MaxPrefixDuplicate
# sb = t
# while (cnt[0] >= cntNeed[0] and cnt[1] >= cntNeed[1]):
#   cnt[0] -= cntNeed[0]
#   cnt[1] -= cntNeed[1]
#   for i in range(mNeed):
#     sb += st[i]

# for i in range(cnt[0]):
#   sb += '0'
# for i in range(cnt[1]):
#   sb += '1'
# print(sb)

# Watto and Mechanism
"""
Ý tưởng thuật toán: Sử dụng Polynomial Hash. Đầu tiên ta sẽ có 1 bảng băm tính hashValuehashValue cho mỗi chuỗi trong n chuỗi của máy. Sau đó với mỗi chuỗi t trong m chuỗi truy vấn, ta sẽ tìm tất cả các chuỗi có thể thu được bằng cách thay thế 1 kí tự của chuỗi t bằng 1 kí tự khác (ví dụ chuỗi t là abc thì sau khi thay thế 1 kí tự sẽ có 6 chuỗi như sau: bbc, cbc, aac, acc, aba, abb).

Tiếp theo ta lấy hashValue của tất cả chuỗi vừa tạo được so sánh với hashValue của bảng băm n chuỗi ở trên, Nếu chuỗi đó xuất hiện trong bảng băm thì in ra YES, ngược lại là NO.

Bước 1: Khai báo các giá trị là hằng số, chọn a = 257, table_size = 10^9 + 7, L = 1000001. Trong đó aa là hằng số; table_size là kích thước của bảng băm, kích thước này càng lớn thì độ phân biệt các hashValue càng cao; L là độ dài lớn nhất có thể có của chuỗi.
Bước 2: Khởi tạo mảng f có độ dài L. Trong công thức tính hashValue của Polynomial Hash, f_i tương ứng với a^{l-i-1}.
Bước 3: Tạo hàm polyHash để tính hashValue của từng chuỗi trong nn chuỗi của máy.
Bước 4: Hàm check để kiểm tra xem giá trị new_hashValuenew_hashValue của tất cả những chuỗi thu được bằng cách thay thế 1 kí tự của chuỗi t bằng 1 kí tự khác, nó có bằng với hashValue của bảng băm n chuỗi ở trên hay không.
Giá trị new_hashValue tính bằng công thức:
- new_hashValue = ((((c - query_i) * f_{len - i - 1}) % table_size + table_size) + h) % table_size
Trong đó ((c - query_i) * f_{len - i - 1}) % table_size + table_size là độ chênh lệch giữa 2 chuỗi sau khi biến đổi, khi độ chênh lệch âm thì phải cộng với table_size; h là giá trị hashValue ban đầu của chuỗi truy vấn.

Tiếp theo, ta dùng hàm find để kiểm tra new_hashValue có nằm trong bảng băm hay không. Nếu không thì trả về true, ngược lại là false.
Độ phức tạp: O(L*log(n)) với L là tổng độ dài của tất cả các chuỗi, log(n) là độ phức tạp khi tìm kiếm trong bảng băm.

Lưu ý: Cách làm trên vẫn có thể cho ra kết quả sai do có sự đụng độ (Collision) khi dùng dùng Polynomial Hash, để giải quyết vấn đề này ta sẽ cần dùng 2 bảng băm với 2 kích thước khác nhau
"""
# def init():
#   f1[0] = f2[0] = 1
#   for i in range(1, L):
#     f1[i] = (f1[i - 1] * a) % table_size_1
#     f2[i] = (f2[i - 1] * a) % table_size_2
        

# def polyHash(keys, mod):
#   hashValue = 0
#   for i in range(len(keys)):
#     hashValue = (hashValue * a + ord(keys[i])) % mod

#   return hashValue

# def check(query):
#   h1 = polyHash(query, table_size_1)
#   h2 = polyHash(query, table_size_2)
  
#   leng = len(query)
#   for i in range(leng):
#     for c in range(3):
#       c_char = chr(ord('a') + c)
#       if c_char == query[i]:
#         continue
#       new_hashValue_1 = ((((ord(c_char) - ord(query[i])) * f1[leng - i - 1]) % table_size_1 + table_size_1) + h1) % table_size_1
#       new_hashValue_2 = ((((ord(c_char) - ord(query[i])) * f2[leng - i - 1]) % table_size_2 + table_size_2) + h2) % table_size_2
#       if (new_hashValue_1, new_hashValue_2) in dic:
#         return True
#   return False

# L = 1000001
# table_size_1 = int(1e9) + 7
# table_size_2 = int(1e9) + 9

# a = 257
# f1 = [0] * L
# f2 = [0] * L

# init()

# n, m = map(int,input().split())
# dic = set()
# for i in range(n):
#   keys = input()
#   dic.add((polyHash(keys, table_size_1), polyHash(keys, table_size_2)))

# buf = []

# for i in range(m):
#   t = input()
#   buf.append('YES' if check(t) else 'NO')
# print('\n'.join(buf))