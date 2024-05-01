from collections import defaultdict, deque

class DoThi:
    def __init__(self):
        self.graph = defaultdict(list)  # Danh sách kề của đồ thị
    
    def them_canh(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)  # Đồ thị vô hướng
    
    def BFS(self, start):
        visited = set()  # Tập hợp các đỉnh đã được duyệt
        queue = deque([start])
        visited.add(start)
        
        while queue:
            node = queue.popleft()
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return visited
    
    def LienThong(self):
        if not self.graph:
            return False  # Đồ thị rỗng không phải là đồ thị liên thông
        
        start_vertex = next(iter(self.graph))  # Chọn một đỉnh bất kỳ làm đỉnh xuất phát
        visited = self.BFS(start_vertex)  # Duyệt đồ thị từ đỉnh xuất phát
        
        # Kiểm tra xem tất cả các đỉnh của đồ thị đã được duyệt hay chưa
        return len(visited) == len(self.graph)

# Ví dụ sử dụng phương thức LienThong
g = DoThi()
g.them_canh(0, 1)
g.them_canh(0, 2)
g.them_canh(1, 2)
g.them_canh(3, 4)

print("Đồ thị g là đồ thị liên thông?", g.LienThong())  # False
