from collections import defaultdict, deque

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị
    
    def them_canh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Đồ thị vô hướng
    
    def BFS(self, start, visited):
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def SoThanhPhan(self):
        if not self.graph:
            return 0  # Đồ thị rỗng không có thành phần liên thông
        
        visited = set()
        num_components = 0
        
        for node in self.graph:
            if node not in visited:
                # Bắt đầu một lần duyệt mới từ đỉnh chưa được duyệt
                self.BFS(node, visited)
                num_components += 1
        
        return num_components

# Ví dụ sử dụng phương thức SoThanhPhan
g = DoThi()
g.them_canh(0, 1)
g.them_canh(0, 2)
g.them_canh(3, 4)
g.them_canh(5, 6)

print("Số thành phần liên thông của đồ thị g là:", g.SoThanhPhan())  # Kết quả: 3
