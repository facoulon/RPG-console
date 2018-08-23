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

    def attack(self, enemy):
        self.xp += 1
        enemy.health -= 1

    def pick(self, item):
        self.inventory.append(item)

    def drop(self, item):
        self.inventory.remove(item)

    def use(self, item):
        if item in self.inventory:
            item.use(self)
            self.drop(item)
        else:
            raise


class Warrior(Character):

    def __init__(self, name, armor):
        Character.__init__(self, name, 200, 0, 300, 0)
        self.armor = armor


class Wizard(Character):

    def __init__(self, name):
        Character.__init__(self, name, 100 , 100, 50, 0)
        self.spells = []

    def invoke(self, spell, enemy):
        if spell in self.inventory:
            self.use(spell)
            enemy.health -= spell.damage
        else:
            raise
