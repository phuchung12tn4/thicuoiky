class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u in self.adj_list:
            self.adj_list[u].append(v)
        else:
            self.adj_list[u] = [v]

    def DuongDi(self, v1, v2):
        visited = set()  # Dùng set để lưu các đỉnh đã duyệt
        return self._dfs(v1, v2, visited)

    def _dfs(self, current, target, visited):
        # Kiểm tra đỉnh hiện tại
        if current == target:
            return True
        
        # Đánh dấu đỉnh hiện tại là đã duyệt
        visited.add(current)

        # Duyệt các đỉnh kề của đỉnh hiện tại
        if current in self.adj_list:
            for neighbor in self.adj_list[current]:
                if neighbor not in visited:
                    # Nếu tìm thấy đường đi từ neighbor đến target, trả về True
                    if self._dfs(neighbor, target, visited):
                        return True
        
        # Nếu không tìm thấy đường đi từ current đến target
        return False

# Ví dụ sử dụng
# Khởi tạo đồ thị
dt = Graph()
dt.add_edge('A', 'B')
dt.add_edge('A', 'C')
dt.add_edge('B', 'D')
dt.add_edge('C', 'D')

# Kiểm tra đường đi từ 'A' đến 'D'
print(dt.DuongDi('A', 'D'))  # Output: True
print(dt.DuongDi('A', 'E'))  # Output: False
