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
        for i in range(len(self.grid)):
            if character in i:
                self.grid.remove(character)
        character.x = x
        character.y = y
        self.grid[x][y].append(character)
