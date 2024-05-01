def TrungCot(arr):
    n = len(arr)
    for j in range(n - 1):  # Duyệt qua từng cột, trừ cột cuối cùng
        for k in range(j + 1, n):  # Duyệt qua các cột sau cột j
            column_j = [row[j] for row in arr]  # Lấy ra giá trị của cột j
            column_k = [row[k] for row in arr]  # Lấy ra giá trị của cột k
            if column_j == column_k:  # So sánh hai cột
                return True
    return False

# Co 2 cot giong nhau 
matrix = [[1, 1, 3],
          [4, 4, 6],
          [7, 7, 9]]
# khong co cot nao giong nhau
matrix = [[1, 1, 3],
          [4, 4, 6],
          [7, 8, 9]]
print("Có ít nhất hai cột giống nhau:", TrungCot(matrix))
