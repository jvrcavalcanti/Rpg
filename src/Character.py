from __future__ import annotations
from enum import Enum
import random
from colorama import Fore, Style


class TypeAttack(Enum):
    Magic = 1
    Physical = 2

class Character(object):
    def __init__(self, life = 3, attack = 3, armor = 3, magic = 0):
        self.type = "Character"

        # Base
        self.life = float("{0:.2f}".format(life ** 3 + 150))
        self.attack = float("{0:.2f}".format(2.75 * attack + 18))
        self.critical_chance = float("{0:.2f}".format(10 * attack))
        self.armor = float("{0:.2f}".format(2.5 * armor + 10))
        self.magic = float("{0:.2f}".format(8 * magic))
        self.magic_resistence = float("{0:.2f}".format(4 * magic + 15))

        # Increments
        self.shield_increment = 1.4
        self.weaK_increment = 1.0
        self.strong_increment = 1.2
        self.magic_increment = 0.8
        self.critical_damage = 1.5

        # others
        self.shield = False
        self.wait = 0
        self.moviments = []

    def add_moviments(self, moviment):
        self.moviments.append(moviment)

    def update(self):
        self.life = float("{0:.2f}".format(self.life))
        self.attack = float("{0:.2f}".format(self.attack))
        self.critical_chance = float("{0:.2f}".format(self.critical_chance))
        self.armor = float("{0:.2f}".format(self.armor))
        self.magic = float("{0:.2f}".format(self.magic))
        self.magic_resistence = float("{0:.2f}".format(self.magic_resistence))

    def attack_generic(self, attack, enemy: Character, type: TypeAttack):
        damage = 0

        if type is TypeAttack.Magic:
            damage = attack - enemy.magic_resistence

        if type is TypeAttack.Physical:
            damage = attack - enemy.armor

            if random.choice(range(1, 100)) <= self.critical_chance:
                damage = (attack * self.critical_damage) - enemy.armor
                print(Fore.RED + "Critical Attack" + Style.RESET_ALL)

        if damage < 0:
            damage = 0

        enemy.life -= damage


    def magic_attack(self, enemy):
        self.attack_generic(self.magic * self.magic_increment, enemy, TypeAttack.Magic)

    def weak_attack(self, enemy):
        self.attack_generic(self.attack * self.weaK_increment, enemy, TypeAttack.Physical, )

    def strong_attack(self, enemy):
        self.attack_generic(self.attack * self.strong_increment, enemy, TypeAttack.Physical)
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
        result = ""

        result += Fore.GREEN
        result += "------------------------------------------------------\n"
        result += "| Type: {}\n"
        result += "| Life: {}\tAttack: {}\tArmor: {}\n"
        result += "| Magic: {}\tMagic Resistence: {}\n"
        result += "| Critical Chance: {}  Critical Damage: {}\n"
        result += "------------------------------------------------------"
        result += Style.RESET_ALL

        return result.format(
            Fore.WHITE + str(self.type) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.life) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.attack) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.armor) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.magic) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.magic_resistence) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.critical_chance) + "%" + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.critical_damage * 100) + "%" + Style.RESET_ALL + Fore.GREEN
        )