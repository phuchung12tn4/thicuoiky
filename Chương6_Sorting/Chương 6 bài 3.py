def Giao(a, b):
    set_a = set(a)
    set_b = set(b)

    result = list(set_a & set_b)

    sorted_result = sorted(result)
    return sorted_result

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

c = Giao(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c (các số xuất hiện đồng thời trong cả a và b và đã sắp xếp tăng dần):", c)