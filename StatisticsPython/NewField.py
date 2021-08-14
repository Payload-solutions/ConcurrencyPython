#!/usr/bin/python3.9


class Field:

    def __init__(self):
        self.coordinate_drunks = {}

    def add_drunk(self, drunk, coordinate):
        self.coordinate_drunks[drunk] = coordinate

    def move_drunk(self, drunk):
        delta_x, delta_y = drunk.walk()
        coordinate_actual = self.coordinate_drunks[drunk]
        new_coordinate = coordinate
