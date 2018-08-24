#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# class Board():

class Board():

    def __init__(self, nb_row, nb_col):
        self.grid = []
        for lig in range(nb_row):
            self.grid.append([])
            for col in range(nb_col):
                self.grid[lig].append([])
