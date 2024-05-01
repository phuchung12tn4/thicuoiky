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
        Cộng hai đa thức và trả về một đa thức mới đã được rút gọn.
        
        Args:
            dathuc2 (DaThuc): Đa thức cần cộng vào đa thức hiện tại.
        
        Returns:
            DaThuc: Đa thức mới là kết quả của phép cộng.
        """
        result = DaThuc()  # Tạo một đa thức mới để lưu kết quả
        current1 = self.head
        current2 = dathuc2.head

        while current1 is not None and current2 is not None:
            # Tính tổng hệ số của hai số hạng cùng mũ
            if current1.somu == current2.somu:
                heso_moi = current1.heso + current2.heso
                result.Them(heso_moi, current1.somu)
                current1 = current1.next
                current2 = current2.next
            # Nếu số mũ của số hạng trong đa thức 1 lớn hơn số mũ trong đa thức 2
            elif current1.somu > current2.somu:
                result.Them(current1.heso, current1.somu)
                current1 = current1.next
            # Nếu số mũ của số hạng trong đa thức 2 lớn hơn số mũ trong đa thức 1
            else:
                result.Them(current2.heso, current2.somu)
                current2 = current2.next

        # Duyệt qua phần còn lại của đa thức 1 (nếu có)
        while current1 is not None:
            result.Them(current1.heso, current1.somu)
            current1 = current1.next

        # Duyệt qua phần còn lại của đa thức 2 (nếu có)
        while current2 is not None:
            result.Them(current2.heso, current2.somu)
            current2 = current2.next

        result.RutGon()  # Rút gọn đa thức kết quả trước khi trả về
        return result
