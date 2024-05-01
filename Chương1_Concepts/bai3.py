def uocchung_dequy(m, n):
    if n == 0:
        return m
    else:
        return uocchung_dequy(n, m % n)

def uocchung_khongdequy(m, n):
    while n != 0:
        m, n = n, m % n
    return m

m = int(input("Nhập số nguyên dương m: "))
n = int(input("Nhập số nguyên dương n: "))

result1 = uocchung_dequy(m, n)
result2 = uocchung_khongdequy(m, n)

print("Ước số chung lớn nhất của", m, "và", n, "là (dùng đệ qui):", result1)
print("Ước số chung lớn nhất của", m, "và", n, "là (không dùng đệ qui):", result2)
