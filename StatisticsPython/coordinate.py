#!/usr/bin/python3.9


class Coordinate:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, delta_x, delta_y):
        return Coordinate(self.x + delta_x, self.y + delta_y)

    def distance(selfm other_coordinate):
        delta_x = self.x - other_coordinate.x
        delta_y = self.y - other_coordinate.y

        return (delta_x**2 + delta_y**2)**0.5
