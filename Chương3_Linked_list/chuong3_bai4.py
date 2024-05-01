class DaThuc:
    def __init__(self):
        self.head = None

    def Them(self, heso, somu):
        """
        Thêm một số hạng vào đa thức.
        
        Args:
            heso (float): Hệ số của số hạng cần thêm.
            somu (int): Số mũ của số hạng cần thêm.
        """
        if self.head is None:
            self.head = Node(heso, somu)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(heso, somu)

    def DoiDau(self):
        """
        Đổi ngược dấu đại số của mỗi số hạng trong đa thức.
        """
        current = self.head
        while current:
            current.heso = -current.heso  # Đổi dấu của hệ số
            current = current.next
