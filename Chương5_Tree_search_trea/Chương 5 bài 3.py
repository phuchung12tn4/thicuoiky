class BinaryTree:
    def __init__(self):
        self.root = None

class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def so_nut_la(root):
    if root is None:
        return 0
    if root.left is None and root.right is None:
        return 1
    so_nut_trai = so_nut_la(root.left)
    so_nut_phai = so_nut_la(root.right)
    return so_nut_trai + so_nut_phai + 1

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

# Tính số nút lá của cây nhị phân
so_nut = so_nut_la(root)
print("Số nút lá của cây nhị phân là:", so_nut)