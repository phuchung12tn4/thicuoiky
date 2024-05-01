class BieuThuc:
    def __init__(self, bt):
        self.bt = bt

    def HauTo(self):
        stack_operand = []
        stack_operator = []
        result = []

        # Hàm kiểm tra ưu tiên của các phép toán
        def precedence(operator):
            if operator in ['+', '-']:
                return 1
            elif operator in ['*', '/']:
                return 2
            return 0

        # Xử lý biểu thức từ trái sang phải
        for char in self.bt:
            if char.isdigit():
                result.append(char)
            elif char in ['+', '-', '*', '/']:
                while stack_operator and precedence(stack_operator[-1]) >= precedence(char):
                    result.append(stack_operator.pop())
                stack_operator.append(char)
            elif char == '(':
                stack_operator.append(char)
            elif char == ')':
                while stack_operator[-1] != '(':
                    result.append(stack_operator.pop())
                stack_operator.pop()

        # Đẩy toàn bộ các phần tử còn lại trong stack_operator vào result
        while stack_operator:
            result.append(stack_operator.pop())

        # Trả về chuỗi biểu diễn biểu thức ở dạng hậu tố
        return ' '.join(result)

# Chuỗi biểu thức
bt = "2 + 3 * 5"

# Chuyển đổi biểu thức sang dạng hậu tố
bieuthuc = BieuThuc(bt)
print("Biểu thức hậu tố tương ứng với", bt, "là:", bieuthuc.HauTo())
