def NhomCot(arr):
    n = len(arr)
    nhom_cot = {}  # Sử dụng một từ điển để lưu trữ các nhóm chỉ mục cột giống nhau

    for j in range(n - 1):  # Duyệt qua từng cột, trừ cột cuối cùng
        for k in range(j + 1, n):  # Duyệt qua các cột sau cột j
            cot_j = [row[j] for row in arr]  # Lấy ra giá trị của cột j
            cot_k = [row[k] for row in arr]  # Lấy ra giá trị của cột k
            if cot_j == cot_k:  # So sánh hai cột
                nhom = [j, k]
                if tuple(nhom) not in nhom_cot:
                    nhom_cot[tuple(nhom)] = True

    # In ra các nhóm chỉ mục cột giống nhau
    for nhom in nhom_cot.keys():
        print("Nhóm cột:", nhom)

matrix = [[1, 1, 3],
          [4, 4, 6],
          [7, 7, 9]]

print("Các nhóm chỉ mục cột giống nhau:")
NhomCot(matrix)
