from MapGrid import *


class AStar(MapGrid):
    def __init__(self, xsize, ysize, obstacles: list):
        super().__init__(xsize, ysize, obstacles)

    def a_star(self, start: Coord, end: Coord) -> []:
        if not self.is_valid_coord(start) or not self.is_valid_coord(end):
            return None
        processing, visited = self.initialize(start)
        current, neighbors = self.next_cell(processing, visited)
        while len(processing) > 0 and end not in neighbors:
            processing.remove(current)
            for neighbor in neighbors:
                tentative_g = current.weight + self.cost(neighbor)
                processing = self.try_add_cell(tentative_g, neighbor, processing, current, end)
            visited.add(current)
            current, neighbors = self.next_cell(processing, visited)
        path = self.make_path(current, end) if end in neighbors else []
        return path

    def initialize(self, start):
        return {WeightedCoord(0, start.x, start.y)}, set()

    def next_cell(self, open_set, closed_set) -> ():
        current = self.pick_current(open_set)
        neighbors = list(filter(lambda n: n not in closed_set, self.neighbors(current)))
        return current, neighbors

    def pick_current(self, open_set):
        if len(open_set) > 0:
            current = min(open_set)
        else:
            current = None
        return current

    def manhattan(self, coord1, coord2):
        return abs(coord1.x - coord2.x) + abs(coord1.y - coord2.y)

    def try_add_cell(self, new_g, cell, open_set, parent, end):
        if self.should_replace_cell(new_g, cell, open_set):
            new_cell = self.make_new_cell(new_g, cell, parent, end)
            if new_cell in open_set:
                open_set.remove(new_cell)
            open_set.add(new_cell)
        return open_set

    def should_replace_cell(self, new_g, cell, open_set):
        if cell not in open_set:
            return True
        for i in open_set:
            if cell == i and new_g < i.weight:
                return True
        return False

    def make_new_cell(self, weight, location, parent, end) -> WeightedCoord:
        new_cell = WeightedCoord(weight, location.x, location.y)
        new_cell.h = self.manhattan(new_cell, end)
        new_cell.parent = parent
        return new_cell

    def make_path(self, parent, end):
        weighted_end = WeightedCoord(0, end.x, end.y)
        weighted_end.parent = parent
        return self.find_path(weighted_end)

    def find_path(self, weighted_end):
        if weighted_end is None:
            return []
        return self.find_path(weighted_end.parent) + [weighted_end]
