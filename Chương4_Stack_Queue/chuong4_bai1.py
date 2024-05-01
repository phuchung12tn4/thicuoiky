class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def InNguoc(self):
        # Khởi tạo một stack rỗng
        stack = []
        current = self.head
        
        # Đưa từng node vào stack
        while current:
            stack.append(current.data)
            current = current.next
        
        # Pop các phần tử khỏi stack để in ngược
        while stack:
            print(stack.pop(), end=" ")

    def InNguocRecursive(self, node):
        if node is None:
            return
        self.InNguocRecursive(node.next)
        print(node.data, end=" ")

# Khởi tạo danh sách liên kết
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("In ngược không đệ qui:")
llist.InNguoc()
print("\nIn ngược đệ qui:")
llist.InNguocRecursive(llist.head)
