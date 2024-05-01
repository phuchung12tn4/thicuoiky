from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị
    
    def them_canh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Đồ thị vô hướng
    
    def ChuaDinh(self, v):
        # Kiểm tra xem đỉnh v có trong danh sách các đỉnh của đồ thị không
        return v in self.graph

# Ví dụ sử dụng phương thức ChuaDinh
g = DoThi()
g.them_canh(0, 1)
g.them_canh(0, 2)
g.them_canh(1, 2)
g.them_canh(2, 3)

print("Đỉnh 0 có trong đồ thị g?", g.ChuaDinh(0))  # Kết quả: True
print("Đỉnh 5 có trong đồ thị g?", g.ChuaDinh(5))  # Kết quả: False
