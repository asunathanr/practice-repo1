import unittest

from MapGrid import *
from coord import Coord

class GridTest(unittest.TestCase):
    def setUp(self):
        self.grid = MapGrid(3, 3, [])
    
    def test_is_adjacent(self):
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(0, 0))
        self.assertFalse(self.grid.is_adjacent(Coord(0, 0), Coord(1, 2))
        self.assertTrue(self.grid.is_adjacent(Coord(0, 0), Coord(0, 1))
