#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Item():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def use(Character):
        pass

class Spell(Item):

    def __init__(self, name, weight, cost, damage):
        Item.__init__(self, name, weight)
        self.cost = cost
        self.damage = damage

class Apple(Item):

    def __init__(self, weight, gain):
        Item.__init__(self, "Apple", weight)
        self.gain = gain
