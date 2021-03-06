import unittest
from MapGrid import *
from coord import Coord


# File: map_grid_test.py
# Authors: Jason Cassimus, Eric Day, Nathan Robertson
# Purpose: Test the MapGrid class.


class GridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [])

    def test_is_adjacent(self):
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(0, 0)))
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(1, 2)))
        self.assertFalse(self.grid.is_adjacent(Coord(-1, 0), Coord(-1, 2)))

        self.assertTrue(self.grid.is_adjacent(Coord(0, 0), Coord(0, 1)))
        self.assertTrue(self.grid.is_adjacent(Coord(1, 1), Coord(0, 1)))

    def test_neighbors(self):
        neighbors = self.grid.neighbors(Coord(1, 1))
        expected = {Coord(1, 2), Coord(0, 1), Coord(2, 1), Coord(1, 0)}
        self.assertEqual(expected, set(neighbors))

    def test_out_of_bound_neighbors(self):
        neighbors = self.grid.neighbors(Coord(0, -1))
        self.assertEqual(set(), set(neighbors), "Expected coords not equivalent to actual coords.")


class ObstacleGridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [])

    def test_add_obstacle(self):
        self.grid.insert_obstacle(Coord(1, 1))
        self.assertEqual([Coord(1, 1)], self.grid.obstacles())
