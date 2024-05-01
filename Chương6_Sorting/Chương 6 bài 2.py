def Hieu(a, b):
    # Chuyen mang a va b thanh tap hop de loai bo cac trung lap 
    set_a = set(a)
    set_b = set(b)

    # Tao mang ma co trong a ma khong co trong b 
    result = [x for x in set_a if x not in set_b]

    # Sap xep ket qua theo thu tu tang dan
    sorted_result = sorted(result)
    return sorted_result

a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

c = Hieu(a,b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c (các số có trong a mà không có trong b và đã sắp xếp tăng dần):", c)

