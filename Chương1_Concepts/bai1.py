def Fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci_recursive(n-1) + Fibonacci_recursive(n-2)

# Sử dụng đệ qui để tính số Fibonacci của n
n = int(input("Nhập số nguyên n (n >= 0): "))
if n < 0:
    print("Vui lòng nhập số nguyên không âm.")
else:
    result_recursive = Fibonacci_recursive(n)
    print(f"Số Fibonacci thứ {n} (dùng đệ qui) là: {result_recursive}")
