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
    
    def DaoNguoc(self):
        if not self.head or not self.head.next:
            return
        
        # Khởi tạo stack rỗng
        stack = []
        current = self.head
        
        # Đưa từng node vào stack
        while current:
            stack.append(current)
            current = current.next
        
        # Pop từng node ra khỏi stack và chỉnh next để đảo ngược danh sách
        self.head = stack.pop()
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next

# Khởi tạo danh sách liên kết
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print("Danh sách liên kết ban đầu:")
llist.display()

llist.DaoNguoc()
print("\nDanh sách liên kết sau khi đảo ngược:")
llist.display()
