def Cong(a, b):
    result = []  # Khởi tạo mảng kết quả

    # Đảo ngược hai mảng a và b để thực hiện phép cộng từ hàng đơn vị
    a = a[::-1]
    b = b[::-1]

    carry = 0  # Biến dùng để lưu giá trị nhớ khi cộng các số
    for i in range(max(len(a), len(b))):
        sum_digit = carry

        if i < len(a):
            sum_digit += a[i]
        if i < len(b):
            sum_digit += b[i]

        # Kiểm tra nếu có tràn số
        if sum_digit > 9:
            result.append(-1)
            carry = 1
        else:
            result.append(sum_digit)
            carry = 0

    # Nếu còn giá trị nhớ sau khi cộng các số, thì thêm nó vào kết quả
    if carry == 1:
        result.append(1)

    # Đảo ngược kết quả trước khi trả về
    return result[::-1]

# Ví dụ sử dụng:
a = [1, 2, 3]
b = [9, 8, 7]

print("Kết quả của a + b là:", Cong(a, b))
