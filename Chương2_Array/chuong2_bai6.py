def Tru(a, b):
    result = []  # Khởi tạo mảng kết quả

    # Đảo ngược hai mảng a và b để thực hiện phép trừ từ hàng đơn vị
    a = a[::-1]
    b = b[::-1]

    borrow = 0  # Biến dùng để lưu giá trị nhớ khi trừ các số
    for i in range(len(a)):
        sub_digit = a[i] - borrow

        if i < len(b):
            sub_digit -= b[i]

        # Kiểm tra nếu có mượn từ hàng trước
        if sub_digit < 0:
            sub_digit += 10
            borrow = 1
        else:
            borrow = 0

        result.append(sub_digit)

    # Loại bỏ các số 0 không cần thiết ở đầu kết quả
    while len(result) > 1 and result[-1] == 0:
        result.pop()

    # Đảo ngược kết quả trước khi trả về
    return result[::-1]

# Ví dụ sử dụng:
a = [1, 2, 3, 4, 5]
b = [9, 8, 7]

print("Kết quả của a - b là:", Tru(a, b))
