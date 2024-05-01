from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị hướng
    
    def them_cung(self, u, v):
        self.graph[u].append(v)  # Thêm cung từ u tới v (cung đi ra từ đỉnh u)
    
    def SoCungRa(self, v):
        # Đếm số lượng đỉnh kề với đỉnh v (có cung ra từ đỉnh v)
        return len(self.graph[v])

# Ví dụ sử dụng phương thức SoCungRa
g = DoThi()
g.them_cung(0, 1)
g.them_cung(0, 2)
g.them_cung(1, 2)
g.them_cung(2, 3)
g.them_cung(3, 1)

print("Số cung đi ra từ đỉnh 0 trong đồ thị g là:", g.SoCungRa(0))  # Kết quả: 2
print("Số cung đi ra từ đỉnh 1 trong đồ thị g là:", g.SoCungRa(1))  # Kết quả: 1
print("Số cung đi ra từ đỉnh 2 trong đồ thị g là:", g.SoCungRa(2))  # Kết quả: 1
print("Số cung đi ra từ đỉnh 3 trong đồ thị g là:", g.SoCungRa(3))  # Kết quả: 1
