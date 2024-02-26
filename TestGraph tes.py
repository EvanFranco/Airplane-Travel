from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """
        Create a graph with 5 cities and distances between them:
        
        A ----20---- B
        |          / |
        |       10   | 30
        |    /        |
        D ----40---- C
        """
        self.g = Graph()
        self.g.add_edge('A', 'B', 20)
        self.g.add_edge('A', 'D', 10)
        self.g.add_edge('B', 'C', 30)
        self.g.add_edge('C', 'D', 40)
        self.g.add_edge('B', 'D', 50)

    def test_add_edge(self):
        self.g.add_edge('E', 'F', 15)
        self.assertEqual(self.g.edges['E']['F'], 15)
        self.assertEqual(self.g.edges['F']['E'], 15)

    def test_remove_edge(self):
        self.g.remove_edge('B', 'D', 50)
        self.assertNotIn('D', self.g.edges['B'])
        self.assertNotIn('B', self.g.edges['D'])

    def test_nbrs(self):
        self.assertCountEqual(list(self.g.nbrs('A')), ['B', 'D'])
        self.assertCountEqual(list(self.g.nbrs('B')), ['A', 'C', 'D'])

    
class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """
        Seattle ------ 2040 mi ------ Chicago ------ 980 mi ------ Boston
        |                                                          |
        |                                                          |
        1140 mi                                                  1520 mi
        |                                                          |
        |                                                          |
        Los Angeles ---------- 1890 mi ------------ New Orleans
        """
        self.g = Graph()
        self.g.add_edge('Seattle', 'Chicago', 2040)
        self.g.add_edge('Seattle', 'Los Angeles', 1140)
        self.g.add_edge('Chicago', 'Boston', 980)
        self.g.add_edge('Chicago', 'Los Angeles', 1980)
        self.g.add_edge('Boston', 'New Orleans', 1520)
        self.g.add_edge('Los Angeles', 'New Orleans', 1890)
    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstra's algorithm
    """ Why: Dijkstra's algorithm is used because it can find the shortest path between 
    two nodes in a graph with non-negative edge weights. Since we are interested in finding 
    the path with the fewest number of flights, and each flight can be 
    considered a non-negative edge weight, Dijkstra's algorithm is a good fit for this problem.."""
    def test_fewest_flights(self):
        # Test Seattle to New Orleans
        tree, weights = self.g.fewest_flights('Seattle')
        self.assertEqual(tree['Seattle'], None)
        self.assertEqual(tree['Los Angeles'], 'Seattle')
        self.assertEqual(tree['Chicago'], 'Seattle')
        self.assertEqual(tree['Boston'], 'Chicago')
        self.assertEqual(tree['New Orleans'], 'Los Angeles')
        self.assertEqual(weights['Seattle'], 0)
        self.assertEqual(weights['Los Angeles'], 1)
        self.assertEqual(weights['Chicago'], 1)
        self.assertEqual(weights['Boston'], 2)
        self.assertEqual(weights['New Orleans'], 2)

    # TODO: Which alg do you use here, and why?
    # Alg: BFS
    """ Why: In the given example graph with unweighted edges, the Breadth-First Search with level 
    recording algorithm is the most efficient because it explores the graph in a breadth-first manner, 
    visiting all the neighbors of the starting node before moving to the next level of neighbors. 
    This guarantees that we find the shortest path to all nodes that are reachable from 
    the starting node, and it can do so without having to consider edge weights."""
    def test_shortest_path(self):
        # Test Seattle shortest path
        distances, weights = self.g.shortest_path('Seattle')
        self.assertEqual(distances, {'Seattle': None, 'Los Angeles': 'Seattle', 'Chicago': 'Seattle', 'New Orleans': 'Los Angeles', 'Boston': 'Chicago'})
        self.assertEqual(weights, {'Seattle': 0, 'Los Angeles': 1140, 'Chicago': 2040, 'New Orleans': 3030, 'Boston': 3020})

    # TODO: Which alg do you use here, and why?
    # Alg: Prim's Algorithm
    """Why: Prim's algorithm is a greedy algorithm used to find the minimum spanning tree of a weighted undirected graph. It starts from a single vertex and 
     iteratively adds the minimum weight edge to a new vertex until all vertices are included in the tree."""
    def test_minimum_salt(self):
        #I know I stole the map in the hw, but it was just easy bc I already have desired test results so it was faster, these match exactly the desired results
        path_tree, optimized_param = self.g.minimum_salt('Seattle')
        self.assertEqual(path_tree, {'Seattle': None, 'Chicago': 'Boston', 'Los Angeles': 'Seattle', 'New Orleans': 'Los Angeles', 'Boston': 'New Orleans'})
        self.assertEqual(optimized_param, {'Seattle': 0, 'Chicago': 980, 'Los Angeles': 1140, 'Boston': 1520, 'New Orleans': 1890})

unittest.main()