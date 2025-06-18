class Digraph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = {}

    def add_edge(self, u, v, weight):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u][v] = weight

    def vertices(self):
        return list(self.adj.keys())

    def incident_edges(self, v):
        if v not in self.adj:
            return []
        return list(self.adj[v].items())

    def dijkstra_shortest_path(self, start, goal):
        import heapq
        distances = {v: float('inf') for v in self.adj}
        distances[start] = 0

        parent = {start: None}
        heap = [(0, start)]

        while heap:
            current_dist, u = heapq.heappop(heap)

            if u == goal:
                path = []
                while u is not None:
                    path.append(u)
                    u = parent[u]
                return path[::-1], distances[goal]

            for neighbor, weight in self.adj[u].items():
                distance_through_u = current_dist + weight
                if distance_through_u < distances[neighbor]:
                    distances[neighbor] = distance_through_u
                    parent[neighbor] = u
                    heapq.heappush(heap, (distance_through_u, neighbor))

        return None, float('inf')


class Graph:
    def __init__(self):
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def vertices(self):
        return list(self.adj.keys())

    def incident_edges(self, v):
        if v not in self.adj:
            return []
        return self.adj[v]

    def bfs_shortest_path(self, start, goal):
        visited = []
        queue = []
        parent = {}

        visited.append(start)
        queue.append(start)
        parent[start] = None

        while queue:
            current = queue.pop(0)

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return path[::-1]

            for neighbor in self.adj[current]:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current

        return None
