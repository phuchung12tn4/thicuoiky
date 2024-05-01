def Cong(a, b):
    def convert_to_int(number):
        # Lấy dấu của số từ phần tử đầu tiên của mảng
        sign = 1 if number[0] == 0 else -1
        # Chuyển phần số từ mảng sang dạng số nguyên
        num = int(''.join(map(str, number[1:])))
        return sign * num

    # Chuyển a và b thành số nguyên
    int_a = convert_to_int(a)
    int_b = convert_to_int(b)

    # Kiểm tra nếu kết quả tràn số nguyên
    if int_a + int_b > 2**31 - 1 or int_a + int_b < -2**31:
        return [-1] * len(a)

    # Trả về kết quả của a + b
    result = int_a + int_b
    result_array = [0] * (len(str(abs(result))) + 1)
    result_array[0] = 0 if result >= 0 else 1
    result_array[1:] = list(map(int, str(abs(result))))
    return result_array

# Test
a = [0, 1, 2, 3]  # Số 123
b = [0, 0, 1]     # Số 1
print(Cong(a, b))  # Kết quả: [0, 1, 2, 4]
