class DaThuc:
    def __init__(self):
        self.head = None

    def RutGon(self):
        current = self.head
        while current:
            prev = current
            check = current.next
            while check != self.head:  # Duyệt đến khi gặp đầu danh sách
                if check.somu == current.somu:
                    current.heso += check.heso
                    prev.next = check.next
                    check = prev
                prev = check
                check = check.next
            current = current.next
        current = self.head
        while current and current.heso == 0:
            if current.next == self.head:  # Trường hợp chỉ có một số hạng
                self.head = None
                return
            self.head = current.next
            current = self.head
        while current and current.next != self.head:
            if current.next.heso == 0:
                current.next = current.next.next
            else:
                current = current.next
