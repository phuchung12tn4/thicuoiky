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

    def Tich(self, dathuc2):
        """
        Tính tích của hai đa thức và trả về một đa thức mới đã được rút gọn.
        
        Args:
            dathuc2 (DaThuc): Đa thức cần nhân vào đa thức hiện tại.
        
        Returns:
            DaThuc: Đa thức mới là kết quả của phép nhân.
        """
        result = DaThuc()  # Tạo một đa thức mới để lưu kết quả

        # Duyệt qua từng số hạng của đa thức 1
        current1 = self.head
        while current1:
            # Duyệt qua từng số hạng của đa thức 2
            current2 = dathuc2.head
            while current2:
                heso_moi = current1.heso * current2.heso
                somu_moi = current1.somu + current2.somu
                result.Them(heso_moi, somu_moi)  # Thêm số hạng mới vào đa thức kết quả
                current2 = current2.next
            current1 = current1.next

        result.RutGon()  # Rút gọn đa thức kết quả trước khi trả về
        return result
