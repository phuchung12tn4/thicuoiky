def mang_tam_giac_tren(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i][j] != 0:
                return False
    return True
# kiem tra ma tren tren 
matrix = [[1, 0, 0],
          [2, 3, 0],
          [4, 5, 6]]

print(mang_tam_giac_tren(matrix))
