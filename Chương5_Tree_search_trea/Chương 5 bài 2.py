class BinaryTree:
    def __init__(self):
        self.root = None
    
class Node:
    def __init__(self, data):
        self.infor = data
        self.left = None
        self.right = None

def height_of_binary_tree(root):
    if root is None:
        return 0
    left_height = height_of_binary_tree(root.left)
    right_height = height_of_binary_tree(root.right)
    return max(left_height, right_height) + 1

# Ví dụ sử dụng
# Xây dựng cây nhị phân
#       1
#      / \
#     2   3
#    /
#   4
#  /
# 5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)

# Tính chiều cao của cây nhị phân
tree_height = height_of_binary_tree(root)
print("Chiều cao của cây nhị phân là:", tree_height)
        