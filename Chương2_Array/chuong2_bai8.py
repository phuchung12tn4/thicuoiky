def TamGiacDuoi(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i):  # Chỉ cần kiểm tra phần tử ở phía dưới đường chéo chính
            if arr[i][j] != 0:  # Nếu có phần tử khác 0, không phải ma trận tam giác dưới
                return False
    return True

# Ví dụ sử dụng:
matrix = [[1, 0, 0],
          [2, 3, 0],
          [4, 5, 6]]

print(TamGiacDuoi(matrix))
