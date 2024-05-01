class DaThuc:
    def __init__(self):
        self.head = None
        
    def Chep(self):
        new_dathuc = DaThuc()
        current = self.head
        while current:
            new_dathuc.Them(current.heso, current.somu)
            current = current.next
            if current == self.head:  # Đảm bảo dừng khi duyệt hết một vòng
                break
        return new_dathuc
