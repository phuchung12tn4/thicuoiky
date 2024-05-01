from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị
    
    def them_canh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Đồ thị vô hướng
    
    def BacDinh(self, v):
        # Đếm số cạnh kề của đỉnh v
        return len(self.graph[v])

# Ví dụ sử dụng phương thức BacDinh
g = DoThi()
g.them_canh(0, 1)
g.them_canh(0, 2)
g.them_canh(1, 2)
g.them_canh(2, 3)

print("Bậc của đỉnh 0 trong đồ thị g là:", g.BacDinh(0))  # Kết quả: 2
print("Bậc của đỉnh 2 trong đồ thị g là:", g.BacDinh(2))  # Kết quả: 3
print("Bậc của đỉnh 3 trong đồ thị g là:", g.BacDinh(3))  # Kết quả: 1
print("Bậc của đỉnh 4 trong đồ thị g là:", g.BacDinh(4))  # Kết quả: 0 (vì đỉnh 4 không có cạnh nối)
