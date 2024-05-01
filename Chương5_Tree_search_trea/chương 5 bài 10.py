class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def CanBangHoanToan(self):
        def is_balanced(node):
            if node is None:
                return True
            
            # Đệ quy tính chiều cao của cây con bên trái và bên phải
            left_height = get_height(node.left)
            right_height = get_height(node.right)
            
            # Kiểm tra độ chênh lệch chiều cao của hai cây con
            if abs(left_height - right_height) > 1:
                return False
            
            # Đệ quy kiểm tra cân bằng hoàn toàn của cây con bên trái và bên phải
            return is_balanced(node.left) and is_balanced(node.right)
        
        def get_height(node):
            if node is None:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1
        
        # Gọi hàm đệ quy để kiểm tra cân bằng hoàn toàn của cây bắt đầu từ nút gốc
        return is_balanced(self.root)

# Ví dụ sử dụng
# Xây dựng cây nhị phân cân bằng hoàn toàn
#        1
#       / \
#      2   3
#     / \
#    4   5
tree = BinaryTree()
tree.root = tree.Node(1)
tree.root.left = tree.Node(2)
tree.root.right = tree.Node(3)
tree.root.left.left = tree.Node(4)
tree.root.left.right = tree.Node(5)

# Kiểm tra xem cây nhị phân có là cây cân bằng hoàn toàn hay không
is_balanced = tree.CanBangHoanToan()
if is_balanced:
    print("Cây nhị phân là cây cân bằng hoàn toàn.")
else:
    print("Cây nhị phân không là cây cân bằng hoàn toàn.")
