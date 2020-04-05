from __future__ import annotations
from enum import Enum
import random


class Type(Enum):
    Magic = 1
    Physical = 2

class Character(object):
    def __init__(self, life = 3, attack = 3, armor = 3, magic = 0):
        self.type = "Character"

        # Base
        self.life = float("{0:.2f}".format(life ** 2 + 50))
        self.attack = float("{0:.2f}".format(2.75 * attack + 18))
        self.critical_chance = float("{0:.2f}".format(10 * attack))
        self.armor = float("{0:.2f}".format(2.5 * armor + 10))
        self.magic = float("{0:.2f}".format(8 * magic))
        self.magic_resistence = float("{0:.2f}".format(4 * magic + 15))

        # Increments
        self.shield_increment = 1.4
        self.weaK_increment = 1.0
        self.strong_increment = 1.2
        self.magic_increment = 1.0
        self.critical_damage = 1.5

        # others
        self.shield = False
        self.wait = 0

    def update(self):
        self.life = float("{0:.2f}".format(self.life))
        self.attack = float("{0:.2f}".format(self.attack))
        self.critical_chance = float("{0:.2f}".format(self.critical_chance))
        self.armor = float("{0:.2f}".format(self.armor))
        self.magic = float("{0:.2f}".format(self.magic))
        self.magic_resistence = float("{0:.2f}".format(self.magic_resistence))

    def attack_generic(self, attack, enemy: Character, type: Type):
        damage = 0

        if type is Type.Magic:
            damage = attack - enemy.magic_resistence

        if type is Type.Physical:
            damage = attack - enemy.armor

            if random.choice(range(1, 100)) <= self.critical_chance:
                damage = (attack * self.critical_damage) - enemy.armor
                print("Critical Attack")

        if damage < 0:
            damage = 0

        enemy.life -= damage


    def magic_attack(self, enemy):
        self.attack_generic(self.magic * self.magic_increment, enemy, Type.Magic)

    def weak_attack(self, enemy):
        self.attack_generic(self.attack * self.weaK_increment, enemy, Type.Physical, )

    def strong_attack(self, enemy):
        self.attack_generic(self.attack * self.strong_increment, enemy, Type.Physical)
        self.wait += 1

    def active_shield(self, enemy: Character):
        if self.shield is False:
            self.armor *= self.shield_increment
            self.shield = True

    def desative_shield(self):
        if self.shield is True:
            self.armor /= self.shield_increment
            self.shield = False

    def __repr__(self):
        obj = "Type: {}\nLife: {}\tAttack: {}\tArmor: {}"
        obj += "\nMagic: {}\tMagic Resistence: {}"
        return obj.format(self.type, self.life, self.attack,
                          self.armor, self.magic, self.magic_resistence)