#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Character():
    
    def __init__(self, name, health, mana, power, xp):
        self.name = name
        self.health = health
        self.mana = mana
        self.power = power
        self.xp = xp
        self.inventory = []

    def move(arg):
        pass

    def attack(charater):
        pass

    def loot(item):
        pass

    def throw(item):
        pass

    def use(item):
        pass


class Warrior(Character):

    def __init__(self, name, armor):
        Character.__init__(self, name, 200, 0, 300, 0)
        self.armor = armor


class Wizard(Character):

    def __init__(self, name):
        Character.__init__(self, name, 100 , 100, 50, 0)
        self.spells = []

    def invoke(spell):
        pass
