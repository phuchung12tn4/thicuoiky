class DaThuc:
    def __init__(self):
        self.head = None
        
    def DoiDau(self):
        current = self.head
        while current:
            current.heso = -current.heso
            current = current.next
