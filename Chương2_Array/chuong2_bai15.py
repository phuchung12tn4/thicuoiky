def DayConDaiNhat(a, b):
    max_length = 0
    result = []

    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                k = 1
                while i+k < len(a) and j+k < len(b) and a[i+k] == b[j+k]:
                    k += 1
                if k > max_length:
                    max_length = k
                    result = a[i:i+k]

    return result

# Test
a = [1, 6, 2, 5, 3, 7, 9, 4, 2, 8, 1, 5]
b = [6, 2, 5, 3, 7, 9, 8, 1, 5]
print(DayConDaiNhat(a, b))  # Kết quả: [6, 2, 5, 3, 7, 9]
