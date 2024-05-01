# a la mang mot chieu 
a = [1, 5, 3, 7, 5, 9, 7]

# Loai bo va sap xep mang a
def Duynhat(a):
    sapxep = sorted(set(a))
    return sapxep

b = Duynhat(a)
print("Mảng a: ", a)
print("Mảng b (sau khi sắp xếp và loại bỏ trùng lặp: )", b)