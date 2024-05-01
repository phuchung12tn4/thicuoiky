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

    def Chep(self):
        """
        Sao chép đa thức và trả về một đa thức mới giống hệt đa thức ban đầu.
        
        Returns:
            DaThuc: Đa thức mới là bản sao của đa thức ban đầu.
        """
        new_dathuc = DaThuc()  # Tạo một đa thức mới để lưu bản sao
        current = self.head
        while current:
            new_dathuc.Them(current.heso, current.somu)  # Thêm số hạng vào đa thức mới
            current = current.next
        return new_dathuc
