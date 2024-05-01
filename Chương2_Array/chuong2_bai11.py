def Cong(a, b):
    # Xác định phần dấu của a và b
    sign_a = a[0]  # Phần dấu của a (0 cho số dương, 1 cho số âm)
    sign_b = b[0]  # Phần dấu của b (0 cho số dương, 1 cho số âm)
    
    # Lấy phần số của a và b từ mảng một chiều (loại bỏ phần dấu)
    digits_a = a[1:]  # Phần số của a
    digits_b = b[1:]  # Phần số của b
    
    # Chuyển phần số từ mảng một chiều sang số nguyên
    num_a = int(''.join(map(str, digits_a)))
    num_b = int(''.join(map(str, digits_b)))
    
    # Xác định phần dấu của kết quả cộng
    if sign_a == sign_b:
        # Cùng dấu
        result_sign = sign_a
    else:
        # Khác dấu
        # Kiểm tra trường hợp số tràn (overflow)
        result_sign = sign_a  # Đặt kết quả theo dấu của số lớn hơn tuyệt đối
        if abs(num_a) < abs(num_b):
            num_a, num_b = num_b, num_a  # Đảm bảo num_a là số lớn hơn tuyệt đối
    
    # Thực hiện phép cộng
    result = num_a + num_b
    
    # Kiểm tra trường hợp tràn số (overflow)
    max_value = (10 ** len(digits_a)) - 1  # Giới hạn của phần số
    if abs(result) > max_value:
        # Tràn số, trả về mảng gồm các số -1
        return [-1] * len(digits_a)
    else:
        # Không tràn số, trả về kết quả
        # Chuyển kết quả thành mảng một chiều với phần dấu ở đầu
        result_digits = list(map(int, str(abs(result))))
        if result_sign == 1:
            result_digits.insert(0, 1)  # Thêm dấu âm vào đầu mảng
        else:
            result_digits.insert(0, 0)  # Thêm dấu dương vào đầu mảng
        return result_digits

# Ví dụ sử dụng phương thức Cong(a, b)
a = [1, 1, 2, 3]  # Số -123
b = [0, 4, 5]     # Số 45
result = Cong(a, b)
if result == [-1] * len(a) or result == [-1] * len(b):
    print("Kết quả bị tràn số.")
else:
    print("Kết quả của a + b là:", result)


