class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def SoSanh(self, other):
        def is_same_tree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is not None and node2 is not None:
                return (node1.info == node2.info and
                        is_same_tree(node1.left, node2.left) and
                        is_same_tree(node1.right, node2.right))
            return False
        
        # Gọi hàm đệ quy để kiểm tra hai cây bắt đầu từ nút gốc của mỗi cây
        return is_same_tree(self.root, other.root)

# Ví dụ sử dụng
# Xây dựng cây nhị phân 1
#        1
#       / \
#      2   3
#     /
#    4
#   /
#  5
tree1 = BinaryTree()
tree1.root = tree1.Node(1)
tree1.root.left = tree1.Node(2)
tree1.root.right = tree1.Node(3)
tree1.root.left.left = tree1.Node(4)
tree1.root.left.left.left = tree1.Node(5)

# Xây dựng cây nhị phân 2 giống với cây 1
tree2 = BinaryTree()
tree2.root = tree2.Node(1)
tree2.root.left = tree2.Node(2)
tree2.root.right = tree2.Node(3)
tree2.root.left.left = tree2.Node(4)
tree2.root.left.left.left = tree2.Node(5)

# So sánh hai cây nhị phân
is_same = tree1.SoSanh(tree2)
if is_same:
    print("Hai cây nhị phân giống hệt nhau.")
else:
    print("Hai cây nhị phân khác nhau.")
