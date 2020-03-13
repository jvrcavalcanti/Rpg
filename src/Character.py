from __future__ import annotations
from enum import Enum


class Type(Enum):
    Magic = 1
    Physical = 2

class Character(object):
    def __init__(self, life = 3, attack = 3, armor = 3, magic = 0):
        self.type = "Character"

        # Base
        self.life = float("{0:.2f}".format(life ** 2 + 50))
        self.attack = float("{0:.2f}".format(2.75 * attack + 18))
        self.armor = float("{0:.2f}".format(2.5 * armor + 10))
        self.magic = float("{0:.2f}".format(12 * magic))
        self.magic_resistence = float("{0:.2f}".format(3 * magic + 8))

        # Increments
        self.shield_increment = 1.4
        self.strong_increment = 1.2

        # others
        self.shield = False
        self.wait = 0

    def update(self):
        self.life = float("{0:.2f}".format(self.life))
        self.attack = float("{0:.2f}".format(self.attack))
        self.armor = float("{0:.2f}".format(self.armor))
        self.magic = float("{0:.2f}".format(self.magic))
        self.magic_resistence = float("{0:.2f}".format(self.magic_resistence))

    def attack_generic(self, attack, enemy: Character, type: Type):
        damage = 0

        if type is Type.Magic:
            damage = attack - enemy.magic_resistence

        if type is Type.Physical:
            damage = attack - enemy.armor

        if damage < 0:
            damage = 0

        enemy.life -= damage


    def magic_attack(self, enemy):
        self.attack_generic(self.magic, enemy, Type.Magic)

    def weak_attack(self, enemy):
        self.attack_generic(self.attack, enemy, Type.Physical)

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