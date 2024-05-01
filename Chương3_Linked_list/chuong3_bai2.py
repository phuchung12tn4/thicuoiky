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

    def Cong(self, dathuc2):
        """
        Cộng đa thức hiện tại với một đa thức khác và trả về đa thức kết quả.
        
        Args:
            dathuc2 (DaThuc): Đa thức cần cộng vào đa thức hiện tại.
        
        Returns:
            DaThuc: Đa thức kết quả sau khi cộng.
        """
        result = DaThuc()  # Tạo một đa thức mới để lưu kết quả
        current1 = self.head
        current2 = dathuc2.head

        while current1 is not None and current2 is not None:
            # Tính tổng của các số hạng có cùng số mũ và thêm vào kết quả
            if current1.somu == current2.somu:
                result.Them(current1.heso + current2.heso, current1.somu)
                current1 = current1.next
                current2 = current2.next
            # Nếu số mũ của số hạng trong đa thức 1 nhỏ hơn số mũ trong đa thức 2
            elif current1.somu < current2.somu:
                result.Them(current1.heso, current1.somu)
                current1 = current1.next
            # Nếu số mũ của số hạng trong đa thức 1 lớn hơn số mũ trong đa thức 2
            else:
                result.Them(current2.heso, current2.somu)
                current2 = current2.next

        # Nếu có số hạng còn lại trong đa thức 1, thêm chúng vào kết quả
        while current1 is not None:
            result.Them(current1.heso, current1.somu)
            current1 = current1.next

        # Nếu có số hạng còn lại trong đa thức 2, thêm chúng vào kết quả
        while current2 is not None:
            result.Them(current2.heso, current2.somu)
            current2 = current2.next

        result.RutGon()  # Rút gọn đa thức kết quả trước khi trả về
        return result
