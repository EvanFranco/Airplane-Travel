class Graph:
    def __init__(self):
        #basic initialization
        self.vertices = set()
        self.edges = dict()

    def add_vertex(self, v):
        #adds vertexs to create graph
        self.vertices.add(v)

    def remove_vertex(self, v):
        #removes vertexs from graph
        self.vertices.remove(v)
        for u in self.edges.keys():
            if v in self.edges[u]:
                self.edges[u].remove(v)
        del self.edges[v]

    def add_edge(self, u, v, wt):
        #adds edges to create graph, checks if edge/vertex already exists
        if u not in self.edges:
            self.edges[u] = {}
        if v not in self.edges:
            self.edges[v] = {}
        self.edges[u][v] = wt
        self.edges[v][u] = wt
        
    def remove_edge(self, u, v, wt):
        #removes edges from graph
        if u in self.edges and v in self.edges[u]:
            if self.edges[u][v] == wt:
                del self.edges[u][v]
                del self.edges[v][u]
                if not self.edges[u]:
                    del self.edges[u]
                if not self.edges[v]:
                    del self.edges[v]
                    
    def nbrs(self, v):
        # Returns the set of neighbors of the given vertex v in the graph.
        neighbors = set()
        if v in self.edges:
            for neighbor in self.edges[v]:
                neighbors.add(neighbor)
        for key in self.edges.keys():
            if v in self.edges[key]:
                neighbors.add(key)
        neighbors.discard(v)
        return neighbors
    
    def fewest_flights(self, city):
        # Returns a dictionary with the shortest path tree and its optimized parameters, using breadth-first search with unit weights starting from the given city.
        visited = {city: None}
        weights = {city: 0}
        queue = [city]
        while queue:
            current_city = queue.pop(0)
            for neighbor in self.nbrs(current_city):
                if neighbor not in visited:
                    visited[neighbor] = current_city
                    weights[neighbor] = weights[current_city] + 1
                    queue.append(neighbor)
        return visited, weights
    
    def shortest_path(self, city):
        # Returns a dictionary with the shortest path tree and its optimized parameters, using Dijkstra's algorithm starting from the given city.
        visited = {city: None}
        weights = {city: 0}
        queue = [city]
        while queue:
            current_city = queue.pop(0)
            for neighbor in self.nbrs(current_city):
                distance = weights[current_city] + self.edges[current_city][neighbor]
                if neighbor not in weights or distance < weights[neighbor]:
                    visited[neighbor] = current_city
                    weights[neighbor] = distance
                    queue.append(neighbor)
        return visited, weights
    
    def minimum_salt(self, start_vertex):
        # Returns a dictionary with the minimum spanning tree and its optimized parameters, using Prim's algorithm starting from the given start_vertex.
        distances = {v: float('inf') for v in self.edges}
        distances[start_vertex] = 0

        visited = set()
        path_tree = {start_vertex: None}

        while len(visited) < len(self.edges):
            u = min((v for v in self.edges if v not in visited), key=distances.get)
            visited.add(u)

            for v in self.edges[u]:
                if v not in visited and self.edges[u][v] < distances[v]:
                    distances[v] = self.edges[u][v]
                    path_tree[v] = u

        optimized_param = {v: distances[v] for v in self.edges}

        return path_tree, optimized_param








