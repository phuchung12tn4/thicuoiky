from collections import defaultdict

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị
    
    def them_canh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Đồ thị vô hướng
    
    def DFS(self, v, visited, parent):
        visited[v] = True  # Đánh dấu đỉnh v đã được duyệt
        
        for neighbor in self.graph[v]:
            if not visited[neighbor]:  # Nếu đỉnh láng giềng chưa được duyệt
                if self.DFS(neighbor, visited, v):  # Tiến hành duyệt đệ quy
                    return True
            elif parent != neighbor:  # Nếu đỉnh láng giềng đã được duyệt và không phải là đỉnh cha
                return True
        
        return False
    
    def ChuTrinh(self):
        if not self.graph:
            return False  # Đồ thị rỗng không có chu trình
        
        visited = {v: False for v in self.graph}  # Tạo tập visited để đánh dấu các đỉnh đã duyệt
        
        # Duyệt qua tất cả các đỉnh của đồ thị và kiểm tra xem có chu trình từ đỉnh đó hay không
        for v in self.graph:
            if not visited[v]:  # Nếu đỉnh chưa được duyệt
                if self.DFS(v, visited, -1):  # Duyệt DFS từ đỉnh v
                    return True
        
        return False

# Ví dụ sử dụng phương thức ChuTrinh
g = DoThi()
g.them_canh(0, 1)
g.them_canh(0, 2)
g.them_canh(1, 2)
g.them_canh(2, 3)

print("Đồ thị g có chu trình:", g.ChuTrinh())  # Kết quả: True

h = DoThi()
h.them_canh(0, 1)
h.them_canh(1, 2)
h.them_canh(2, 0)

print("Đồ thị h có chu trình:", h.ChuTrinh())  # Kết quả: True

k = DoThi()
k.them_canh(0, 1)
k.them_canh(1, 2)

print("Đồ thị k có chu trình:", k.ChuTrinh())  # Kết quả: False
