from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị hướng
    
    def them_cung(self, u, v):
        self.graph[u].append(v)  # Thêm cung từ u tới v (cung đi vào đỉnh v)
    
    def SoCungVao(self, v):
        count = 0
        
        # Đếm số lượng đỉnh u sao cho có cung từ u tới v (cung đi vào đỉnh v)
        for u in self.graph:
            if v in self.graph[u]:  # Kiểm tra xem có cung từ u tới v không
                count += 1
        
        return count

# Ví dụ sử dụng phương thức SoCungVao
g = DoThi()
g.them_cung(0, 1)
g.them_cung(0, 2)
g.them_cung(1, 2)
g.them_cung(2, 3)
g.them_cung(3, 1)

print("Số cung đi vào đỉnh 1 trong đồ thị g là:", g.SoCungVao(1))  # Kết quả: 2
print("Số cung đi vào đỉnh 2 trong đồ thị g là:", g.SoCungVao(2))  # Kết quả: 1
print("Số cung đi vào đỉnh 3 trong đồ thị g là:", g.SoCungVao(3))  # Kết quả: 1
print("Số cung đi vào đỉnh 0 trong đồ thị g là:", g.SoCungVao(0))  # Kết quả: 0
