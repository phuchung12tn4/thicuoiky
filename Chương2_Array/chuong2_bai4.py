def mang_nhom_hang(arr):
    n = len(arr)
    nhom_hang = {}  # Sử dụng một từ điển để lưu trữ các nhóm chỉ mục hàng giống nhau

    for i in range(n):
        hang = tuple(arr[i])  # Chuyển đổi list hàng thành một tuple để sử dụng làm khóa
        if hang not in nhom_hang:
            nhom_hang[hang] = [i]  # Tạo một nhóm mới nếu hàng chưa được ghi nhận
        else:
            nhom_hang[hang].append(i)  # Thêm chỉ mục hàng vào nhóm đã tồn tại

    # In ra các nhóm chỉ mục hàng
    for nhom in nhom_hang.values():
        print("Nhóm hàng:", nhom)

# Ví dụ sử dụng:
matrix = [[1, 2, 3],
          [4, 5, 6],
          [1, 2, 3],
          [7, 8, 9],
          [4, 5, 6]]

print("Các nhóm chỉ mục hàng giống nhau:")
mang_nhom_hang(matrix)
