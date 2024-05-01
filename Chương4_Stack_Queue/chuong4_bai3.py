class BieuThuc:
    def __init__(self, bt):
        self.bt = bt

    def GiaTri(self):
        stack_operand = []
        stack_operator = []

        # Hàm tính toán giá trị khi gặp một phép toán
        def evaluate(operator):
            operand2 = stack_operand.pop()
            operand1 = stack_operand.pop()
            if operator == '+':
                stack_operand.append(operand1 + operand2)
            elif operator == '-':
                stack_operand.append(operand1 - operand2)
            elif operator == '*':
                stack_operand.append(operand1 * operand2)
            elif operator == '/':
                stack_operand.append(operand1 / operand2)

        # Xử lý biểu thức từ trái sang phải
        for char in self.bt:
            if char.isdigit():
                stack_operand.append(int(char))
            elif char in ['+', '-', '*', '/']:
                while stack_operator and stack_operator[-1] in ['*', '/'] and char in ['+', '-']:
                    evaluate(stack_operator.pop())
                stack_operator.append(char)
            elif char == '(':
                stack_operator.append(char)
            elif char == ')':
                while stack_operator[-1] != '(':
                    evaluate(stack_operator.pop())
                stack_operator.pop()

        # Xử lý các phần tử còn lại trong stack
        while stack_operator:
            evaluate(stack_operator.pop())

        # Trả về giá trị cuối cùng
        return stack_operand[0]

# Chuỗi biểu thức
bt = "3+(4*5)-2"

# Tính toán giá trị của biểu thức
bieuthuc = BieuThuc(bt)
print("Giá trị của biểu thức", bt, "là:", bieuthuc.GiaTri())
