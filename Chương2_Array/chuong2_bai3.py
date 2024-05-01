def mang_trung_hang(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):  # Chỉ cần so sánh các hàng sau hàng i
            if arr[i] == arr[j]:  # So sánh hàng i với các hàng sau
                return True
    return False

# Hai hàng giống nhau
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [1, 2, 3]]  

# Không có hai hàng giống nhau
matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]  

print(mang_trung_hang(matrix1))
print(mang_trung_hang(matrix2))
