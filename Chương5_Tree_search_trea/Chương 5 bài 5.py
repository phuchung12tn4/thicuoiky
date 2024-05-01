class Tree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def KiemTraBST(self):
        def is_bst(node, min_val, max_val):
            if node is None:
                return True
            
            # Kiểm tra giá trị của nút hiện tại nằm trong khoảng (min_val, max_val)
            if min_val < node.info < max_val:
                # Kiểm tra BST cho cây con bên trái và cây con bên phải
                return (is_bst(node.left, min_val, node.info) and
                        is_bst(node.right, node.info, max_val))
            else:
                return False
        
        # Gọi hàm đệ quy để kiểm tra BST bắt đầu từ nút gốc
        return is_bst(self.root, float('-inf'), float('inf'))

# Ví dụ sử dụng
# Xây dựng cây nhị phân BST
#        10
#       /  \
#      5   15
#     / \    \
#    3   7   20
tree = Tree()
tree.root = tree.Node(10)
tree.root.left = tree.Node(5)
tree.root.right = tree.Node(15)
tree.root.left.left = tree.Node(3)
tree.root.left.right = tree.Node(7)
tree.root.right.right = tree.Node(20)

# Kiểm tra xem cây nhị phân có phải là BST hay không
is_bst = tree.KiemTraBST()
if is_bst:
    print("Cây là 1 cây nhị phân!")
else:
    print("Cây không phải là 1 cây nhị phân")
