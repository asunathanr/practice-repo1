from coord import Coord
class MapGrid:

    def __init__(self, xsize: int, ysize: int, coords: list):
        self.xsize = xsize
        self.ysize = ysize
        self.gridArea = []
        for i in range(0, xsize):
            new = []
            for j in range(0, ysize):
                new.append(0)
            self.gridArea.append(new)


    def neighbors(self, coord: (int, int)) -> list:
        pass

    def is_adjacent(self,coord1,coord2):
        if self.is_valid_coord(coord1) and self.is_valid_coord(coord2):
            if self.is_adjacent_position(coord1,coord2):
                return True
        return False

    def is_valid_coord(self,coord):
        if coord.x < 0:
            return False
        if coord.y < 0:
            return False
        if coord.x >= self.xsize:
            return False
        if coord.y >= self.ysize:
            return False
        return True

    def is_adjacent_position(self, coord1, coord2):
        md = abs(coord1.x-coord2.x)+abs(coord1.y-coord2.y)
        if md == 1:
            return True
        return False

    def adjacent(self, coord) -> list:
        raw_neighbors = [
            Coord(coord.x, coord.y + 1),
            Coord(coord.x, coord.y - 1),
            Coord(coord.x - 1, coord.y),
            Coord(coord.x + 1, coord.y)
        ]
        neighbors = []
        for i in raw_neighbors:
            if self.is_adjacent(coord, i):
                neighbors.append(i)
        return neighbors
