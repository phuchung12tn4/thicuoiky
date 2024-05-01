# Định nghĩa lớp Node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Định nghĩa lớp BinaryTree và phương thức count_nodes
class BinaryTree:
    def __init__(self):
        self.root = None

    def count_nodes(self, root):
        if root is None:
            return 0
        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)

# Tạo một cây nhị phân
tree = BinaryTree()
tree.root = Node(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Đếm số nút của cây
num_nodes = tree.count_nodes(tree.root)
print("Số nút của cây là:", num_nodes)  # Output: Số nút của cây là: 5
