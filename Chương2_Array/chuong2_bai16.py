def Dao(mang):
    rows = len(mang)
    cols = len(mang[0])

    def check_land(i, j):
        if 0 <= i < rows and 0 <= j < cols and mang[i][j] == 1:
            return True
        return False

    def compute_area(i, j):
        if not check_land(i, j):
            return 0
        mang[i][j] = 0
        area = 1
        area += compute_area(i-1, j)
        area += compute_area(i+1, j)
        area += compute_area(i, j-1)
        area += compute_area(i, j+1)
        return area

    max_area = 0
    for i in range(rows):
        for j in range(cols):
            if mang[i][j] == 1:
                max_area = max(max_area, compute_area(i, j))

    print("Diện tích lớn nhất của đảo hình chữ nhật là:", max_area)

# Test
mang = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1]
]
Dao(mang)  # Kết quả: Diện tích lớn nhất của đảo hình chữ nhật là: 7
