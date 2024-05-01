def mang_doi_xung(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if arr[i][j] != arr[j][i]:  
                return False
    return True
# kiem tra doi xung 
matrix1 = [[1, 2, 3],
           [2, 4, 5],
           [3, 5, 6]]
# kiem tra khong doi xung 
matrix2 = [[1, 2, 3],
           [2, 4, 4],
           [3, 5, 6]]
print(mang_doi_xung(matrix1))
print(mang_doi_xung(matrix2))
