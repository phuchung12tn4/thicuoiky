class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def BSTTuanTu(self):
        def is_sequential_bst(node):
            if node is None:
                return True
            
            # Kiểm tra số lượng nút con của nút hiện tại
            has_left = node.left is not None
            has_right = node.right is not None
            
            # Nút hiện tại không được có cả hai nút con
            if has_left and has_right:
                return False
            
            # Đệ quy kiểm tra các cây con bên trái và bên phải
            return is_sequential_bst(node.left) and is_sequential_bst(node.right)
        
        # Gọi hàm đệ quy để kiểm tra BST tuần tự của cây bắt đầu từ nút gốc
        return is_sequential_bst(self.root)

# Ví dụ sử dụng
# Xây dựng cây nhị phân BST tuần tự
#        1
#       /
#      2
#     /
#    3
tree = BinaryTree()
tree.root = tree.Node(1)
tree.root.left = tree.Node(2)
tree.root.left.left = tree.Node(3)

# Kiểm tra xem cây nhị phân có là BST tuần tự hay không
is_sequential_bst = tree.BSTTuanTu()
if is_sequential_bst:
    print("Cây nhị phân là BST tuần tự.")
else:
    print("Cây nhị phân không là BST tuần tự.")
