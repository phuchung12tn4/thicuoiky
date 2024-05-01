class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def CayCon(self, other):
        def is_subtree(node1, node2):
            if node1 is None:
                return False
            if node1.info == node2.info and is_same_tree(node1, node2):
                return True
            return is_subtree(node1.left, node2) or is_subtree(node1.right, node2)
        
        def is_same_tree(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is not None and node2 is not None:
                return (node1.info == node2.info and
                        is_same_tree(node1.left, node2.left) and
                        is_same_tree(node1.right, node2.right))
            return False
        
        # Gọi hàm đệ quy để kiểm tra xem cây other có là cây con của cây self không
        return is_subtree(self.root, other.root)

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

# Xây dựng cây nhị phân 2 là một cây con của cây 1
tree2 = BinaryTree()
tree2.root = tree2.Node(2)
tree2.root.left = tree2.Node(4)
tree2.root.left.left = tree2.Node(5)

# Kiểm tra xem cây 2 có là cây con của cây 1 không
is_subtree = tree1.CayCon(tree2)
if is_subtree:
    print("Cây nhị phân 2 là cây con của cây nhị phân 1.")
else:
    print("Cây nhị phân 2 không là cây con của cây nhị phân 1.")
