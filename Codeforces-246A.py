# A. Buggy Sorting

# Tìm mảng để chứng minh thuật toán sai
""" loop integer variable i from 1 to n-1
    loop integer variable j from i to n-1
        if (aj>aj+1), then swap the values of elements aj and aj+1 """

# Tại sao thuật toán sắp xếp đề cho bị sai?
# i đi từ 1 -> n - 1 , => kh đảm bảo các vị trí đầu tiên được sắp đứng đúng thứ tự

# !! Lời giải: tạo ra 1 mảng sao chi phần tử tại ví trí đầu tiên bị sai khi vòng for j đã swap
# Thuật toán đúng:
# i: 1 --> n - 1
#   j: n - 1 --> i

# các base case: n = 1, n = 2
# các case xử lý: n > 2

n = int(input())
if n < 3:
    print(-1)
else:
    a = (i for i in range(1, n + 1))
      

