from Graph import Graph
import unittest

class test_Graph(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
     def setUp(self):
        """ 
        15    10    20
        A ---- E ----- B
        |           /  |
        |         /    |
        10       /    20 
        |     /       |
        |   /         |
        D /   F ------ C
        10    15     5
        """
        self.g = Graph()
        self.g.add_edge('A', 'B', 10)
        self.g.add_edge('A', 'E', 15)
        self.g.add_edge('B', 'C', 20)
        self.g.add_edge('B', 'F', 20)
        self.g.add_edge('C', 'D', 5)
        self.g.add_edge('C', 'F', 10)
        self.g.add_edge('D', 'F', 15)
        self.g.add_edge('E', 'F', 10)

    # TODO: Add unittests for public interface of Graph class (except traversal algs)
     def test_add_edge(self):
        self.g.add_edge('A', 'B', 20)
        self.assertEqual(self.g.edges['A']['B'], 10)
        self.assertEqual(self.g.edges['B']['A'], 10)

     def test_removeEdge(self):
        self.g.remove_edge('C', 'f', 15)
        self.assertNotIn('C', self.g.edges['F'])
        self.assertNotIn('F', self.g.edges['C'])

class test_GraphTraversal(unittest.TestCase):
    # Create a graph `self.g` that you can use in your other unittests. Include ASCII art.
    def setUp(self):
        """ADD DOCSTRING"""
        self.g = Graph()
        self.g.add_edge('New York', 'Portland', 2894)
        self.g.add_edge('New York', 'San Francisco', 2905)
        self.g.add_edge('Portland', 'San Francisco', 635)
        self.g.add_edge('Portland', 'San Diego', 1729)
        self.g.add_edge('San Francisco', 'Las Vegas', 568)
        self.g.add_edge('San Diego', 'Las Vegas', 331)

    """New York---2894---Portland
     /                 |
  807                  |
    /                  |
    San Francisco      |
   568               1729 
    |                  |
    |                  |
    |                  |
   Las Vegas-331---San Diego"""


    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstras algorithm
    # Why: I used this alg becasue it can find the shortest distances between the two locations(nodes)
    def test_fewest_flights(self):
        """Test that the fewest number of flights between two cities is computed correctly."""
        expected_path = ['San Francisco', 'Los Angeles', 'San Diego']
        shortest_path = (self.g, 'San Francisco', 'San Diego')
        self.assertEqual(shortest_path, expected_path)

        expected_path = ['New York', 'Portland', 'San Francisco', 'Las Vegas']
        shortest_path = (self.g, 'New York', 'Las Vegas')
        self.assertEqual(shortest_path, expected_path)
    # TODO: Which alg do you use here, and why?
    # Alg: Dijkstras algorithm
    # Why: I used this alg becasue it can find the shortest distances between the two locations(nodes)

    def test_shortest_path(self):
        """Test shortest path using Prim's algorithm"""
        expected_path1 = ['New York', 'San Francisco', 'Las Vegas']
        expected_distance1 = 2473

        expected_path2 = ['Portland', 'San Francisco', 'Las Vegas']
        expected_distance2 = 1203

        self.assertEqual(self.g.shortest_path('New York', 'Las Vegas'), (expected_path1, expected_distance1))
        self.assertEqual(self.g.shortest_path('Portland', 'Las Vegas'), (expected_path2, expected_distance2))
    # TODO: Which alg do you use here, and why?
    # Alg: Prim's algorithm 
    # Why: To find the minimun spanning tree and it then traverses using the shortest path

    def test_minimum_salt(self):
        """Test minimum salt between Seattle and San Diego"""
        expected_path = ['Seattle', 'San Francisco', 'Los Angeles', 'San Diego']
        self.assertEqual(self.g.minimum_salt('Seattle', 'San Diego'), expected_path)

unittest.main()