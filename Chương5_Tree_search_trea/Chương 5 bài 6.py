class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None
            self.height = 1  # Chiều cao ban đầu của mỗi nút là 1

    def KiemTraAVL(self):
        def get_height(node):
            if node is None:
                return 0
            return node.height

        def get_balance_factor(node):
            if node is None:
                return 0
            return get_height(node.left) - get_height(node.right)

        def is_avl(node):
            if node is None:
                return True
            
            # Kiểm tra độ cân bằng của cây con bên trái và cây con bên phải của nút hiện tại
            balance = get_balance_factor(node)
            if abs(balance) > 1:
                return False
            
            # Kiểm tra đệ quy độ cân bằng của các cây con
            return is_avl(node.left) and is_avl(node.right)
        
        # Gọi hàm đệ quy để kiểm tra AVL bắt đầu từ nút gốc
        return is_avl(self.root)

# Ví dụ sử dụng
# Xây dựng cây nhị phân AVL
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   20
tree = BinaryTree()
tree.root = tree.Node(10)
tree.root.left = tree.Node(5)
tree.root.right = tree.Node(15)
tree.root.left.left = tree.Node(3)
tree.root.left.right = tree.Node(7)
tree.root.right.right = tree.Node(20)

# Kiểm tra xem cây nhị phân có phải là AVL hay không
is_avl = tree.KiemTraAVL()
if is_avl:
    print("Cây là một cây AVL.")
else:
    print("Cây không phải là một cây AVL.")
