class Cell:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.visited = False
        self.walls = {"up": True, "down": True, "right": True, "left": True}

    def breackWalls(self, neighbour_x, neighbour_y):
        if self.x - neighbour_x == -1:
            self.walls["down"] = False
        elif self.x - neighbour_x == 1:
            self.walls["up"] = False
        elif self.y - neighbour_y == -1:
            self.walls["right"] = False
        elif self.y - neighbour_y == 1:
            self.walls["left"] = False
