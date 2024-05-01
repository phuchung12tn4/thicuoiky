def Nhan(a, b):
    n = len(a)  # Số chữ số của số a
    m = len(b)  # Số chữ số của số b

    # Tạo một mảng kết quả với tất cả các phần tử ban đầu là 0
    result = [0] * (n + m)

    # Duyệt qua từng chữ số của số a
    for i in range(n):
        carry = 0  # Biến lưu giá trị nhớ khi nhân các số
        for j in range(m):
            # Nhân từng chữ số của a với từng chữ số của b, cộng vào kết quả
            temp = a[n - 1 - i] * b[m - 1 - j] + result[i + j] + carry
            carry = temp // 10  # Lưu giá trị nhớ mới
            result[i + j] = temp % 10  # Lưu phần đơn vị vào kết quả

        # Lưu giá trị nhớ cuối cùng (nếu có) vào kết quả
        result[i + m] += carry

    # Loại bỏ các số 0 không cần thiết ở đầu kết quả
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Kiểm tra nếu kết quả bị tràn số
    if len(result) > n + m:
        return [-1]

    # Đảo ngược kết quả trước khi trả về
    return result[::-1]

# Ví dụ sử dụng:
a = [1, 2, 3]
b = [9, 8, 7]

print("Kết quả của a * b là:", Nhan(a, b))
