def DayConDauTien(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                k = 1
                while i+k < len(a) and j+k < len(b) and a[i+k] == b[j+k]:
                    k += 1
                if k > 1:
                    return a[i:i+k]
    return []

# Test
a = [1, 6, 2, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 5, 3, 7, 8]
print(DayConDauTien(a, b))  # Kết quả: [6, 2]
