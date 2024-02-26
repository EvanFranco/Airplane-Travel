class Graph:
    def __init__(self):

        """This initialization of the graph"""

        self.vertices = set()
        self.edges = dict()

    def add_vertex(self, v):

        """This adds the vertex(s) to the graph"""

        self.vertices.add(v)

    def remove_vertex(self, v):

        """This removes the vertexs from graph"""

        self.vertices.remove(v)
        for u in self.edges.keys():
            if v in self.edges[u]:
                self.edges[u].remove(v)

        del self.edges[v]

    def add_edge(self, u, v, wt):

        """Adds an edge to the graph or updates its weight if it exists"""
        
        if u not in self.edges:
            self.edges[u] = {}
        
        if v not in self.edges:
            self.edges[v] = {}
        
        self.edges[u][v] = wt
        self.edges[v][u] = wt if v in self.edges[u] else self.edges[v][u]

            
    def remove_edge(self, u, v, wt):

        """Removes the edges from the graph"""

        if u in self.edges and v in self.edges[u]:

            if self.edges[u][v] == wt:
                del self.edges[u][v]
                del self.edges[v][u]

                if not self.edges[u]:
                    del self.edges[u]
                if not self.edges[v]:
                    del self.edges[v]
                    
    def nbrs(self, v):

        """Returns the set of the neighbors of the given vertex v in the graph"""
        neighbors = set()
        if v in self.edges:
            for nbrs in self.edges[v]:
                neighbors.add(nbrs)

        for key in self.edges.keys():
            if v in self.edges[key]:
                neighbors.add(key)

        neighbors.discard(v)
        return neighbors
    
    def fewest_flights(self, city):

        """Returns the shortest path by using breadth first search from the given city."""

        visited = {city: None}
        weights = {city: 0}
        queue = [city]
        while queue:

            current_city = queue.pop(0)
            for nbrs in self.nbrs(current_city):
                if nbrs not in visited:
                    visited[nbrs] = current_city
                    weights[nbrs] = weights[current_city] + 1
                    queue.append(nbrs)
        return visited, weights
    
    def shortest_path(self, start_city, end_city):
        """Returns the shortest path using breadth first search"""
        visited = {start_city: None}
        queue = [start_city]
        while queue:
            current_city = queue.pop(0)
            if current_city == end_city:
                break
            for nbrs in self.nbrs(current_city):
                if nbrs not in visited:
                    visited[nbrs] = current_city

                    queue.append(nbrs)
        if end_city not in visited:
            return None
        path = []
        while end_city is not None:
            path.append(end_city)
            end_city = visited[end_city]
        path.reverse()
        return path
        
    def minimum_salt(self, start_vertex):

        """Returns the minimum spanning tree using Prims algorithm """
        
        pathtree = {start_vertex: None}
        dis = {v: float('inf') for v in self.edges}
        visited = set()
        dis[start_vertex] = 0

        while len(visited) < len(self.edges):
            u = min((v for v in self.edges if v not in visited), key=dis.get)
            visited.add(u)
            for v in self.edges[u]:
                if v not in visited and self.edges[u][v] < dis[v]:
                    dis[v] = self.edges[u][v]
                    pathtree[v] = u
        Opti_P = {v: dis[v] for v in self.edges}
        return pathtree, Opti_P
