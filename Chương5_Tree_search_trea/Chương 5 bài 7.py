class BinaryTree:
    def __init__(self):
        self.root = None
    
    class Node:
        def __init__(self, data):
            self.info = data
            self.left = None
            self.right = None

    def Chep(self):
        def copy_tree(node):
            if node is None:
                return None
            
            # Tạo một nút mới có giá trị info là giống với nút hiện tại
            new_node = self.Node(node.info)
            
            # Đệ quy sao chép cây con bên trái và bên phải của nút hiện tại
            new_node.left = copy_tree(node.left)
            new_node.right = copy_tree(node.right)
            
            return new_node
        
        # Gọi hàm đệ quy để sao chép cây bắt đầu từ nút gốc của cây hiện tại
        new_tree = BinaryTree()
        new_tree.root = copy_tree(self.root)
        
        return new_tree

# Ví dụ sử dụng
# Xây dựng cây nhị phân
#        1
#       / \
#      2   3
#     /
#    4
#   /
#  5
tree = BinaryTree()
tree.root = tree.Node(1)
tree.root.left = tree.Node(2)
tree.root.right = tree.Node(3)
tree.root.left.left = tree.Node(4)
tree.root.left.left.left = tree.Node(5)

# Sao chép cây nhị phân
copied_tree = tree.Chep()

# In ra các nút của cây nhị phân sao chép để kiểm tra
def traverse(node):
    if node is None:
        return
    traverse(node.left)
    print(node.info, end=' ')
    traverse(node.right)

print("Cây nhị phân gốc:")
traverse(tree.root)
print("\nCây nhị phân sao chép:")
traverse(copied_tree.root)
