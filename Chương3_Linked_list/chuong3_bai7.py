class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        if self.head is None:
            self.head = Node(heso, somu)
            self.head.next = self.head  # Tạo vòng
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = Node(heso, somu)
            current.next.next = self.head
