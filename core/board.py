#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Board():

    def __init__(self, nb_row, nb_col):
        self.grid = []
        for lig in range(nb_row):
            self.grid.append([])
            for col in range(nb_col):
                self.grid[lig].append([])


    def move(self, character, x, y):
        if character.x != None or character.y != None:
            self.grid[character.x][character.y].remove(character)
        character.x = x
        character.y = y
        self.grid[x][y].append(character)

    def display(self):
        map = ""
        for table in self.grid:
        # for index, value_table in enumerate(self.grid):
            for cell in table:
            # for cell in value_table:
                if cell == []:
                    map += "-"
                else:
                    map += "X"
            map += "\n"
        return map
