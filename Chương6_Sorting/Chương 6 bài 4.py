def Hop(a, b):
    # Chuyển mảng a và b thành tập hợp để loại bỏ các số trùng lặp
    set_a = set(a)
    set_b = set(b)
    
    # Kết hợp các phần tử từ hai tập hợp và loại bỏ các số trùng lặp
    result = list(set_a | set_b)  # Lấy hợp của hai tập hợp
    
    # Sắp xếp mảng c theo thứ tự tăng dần
    result_sorted = sorted(result)
    
    return result_sorted

# Ví dụ sử dụng phương thức Hop
a = [1, 5, 3, 7, 9, 4, 2]
b = [9, 6, 2, 3, 8]

c = Hop(a, b)
print("Mảng a:", a)
print("Mảng b:", b)
print("Mảng c (các số có trong a và / hoặc trong b và đã sắp xếp tăng dần):", c)
