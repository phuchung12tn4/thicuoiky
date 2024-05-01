class Node:
    def __init__(self, heso, somu):
        self.heso = heso
        self.somu = somu
        self.next = None

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

    def print_dathuc(self):
        """
        In đa thức ra màn hình.
        """
        current = self.head
        while current:
            print(f"{current.heso}x^{current.somu}", end=" ")
            current = current.next
        print()

# Example usage:
dathuc = DaThuc()
dathuc.Them(2, 3)  # Thêm số hạng có hệ số 2 và số mũ 3 vào đa thức
dathuc.Them(3, 2)  # Thêm số hạng có hệ số 3 và số mũ 2 vào đa thức đã có
dathuc.print_dathuc()  # In đa thức ra màn hình
