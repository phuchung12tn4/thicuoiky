class BinaryTree:
    def __init__(self):
        self.root = None
class Node:
    def __init__(self, data):
        self.info = data
        self.left = None
        self.right = None

def tim_nut_trung_gian(root):
    nut_trung_gian = []
        # Hàm đệ quy để duyệt cây và tìm các nút trung gian
    def dfs(node):
        if node is None:
            return
        # Kiểm tra xem nút hiện tại có là nút trung gian hay không
        if node.left is not None or node.right is not None:
            if node != root:  # Kiểm tra nếu nút không phải là nút gốc
                nut_trung_gian.append(node.info)
        # Duyệt các cây con bên trái và bên phải của nút hiện tại
        dfs(node.left)
        dfs(node.right)
    # Gọi hàm đệ quy bắt đầu từ nút gốc của cây
    dfs(root)
    return nut_trung_gian
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

# Tính số nút trung gian của cây nhị phân
so_nut_trung_gian = tim_nut_trung_gian(root)
print("Số nút trung gian của cây nhị phân là:", so_nut_trung_gian)