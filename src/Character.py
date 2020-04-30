from __future__ import annotations
from enum import Enum
from colorama import Fore, Style
import random


class TypeAttack(Enum):
    Magic = 1
    Physical = 2

class Character(object):
    def __init__(self, life = 3, attack = 3, armor = 3, magic = 0):
        self.type = "Character"

        # Increments no base
        self.shield_increment = 1.4
        self.weaK_increment = 1.0
        self.strong_increment = 1.2
        self.critical_damage = 1.5
        self.magic_increment = 1.0

        # Others no base
        self.cost_mp = 25
        self.shield = False
        self.wait = 0
        self.moviments = []

        self.increments = {
            "attack": {
                "increment": 2.75,
                "base": 18
            },
            "critical": {
                "increment": 10
            },
            "magic": {
                "increment": 6.5
            },
            "life": {
                "increment": 3,
                "base": 150
            },
            "armor": {
                "increment": 2.5,
                "base": 10
            },
            "magic_resistance": {
                "increment": 4.5,
                "base": 19
            },
            "mp": {
                "increment": 35
            }
        }

        ## Attack
        self.attack = float("{0:.2f}".format(
            self.increments["attack"]["increment"] * attack + self.increments["attack"]["base"])
        )
        self.critical_chance = float("{0:.2f}".format(
            self.increments["critical"]["increment"] * attack)
        )
        self.magic = float("{0:.2f}".format(
            self.increments["magic"]["increment"] * magic)
        )

        ## Tank
        self.life = float("{0:.2f}".format(
            self.increments["life"]["increment"] ** 3 + self.increments["life"]["base"])
        )
        self.armor = float("{0:.2f}".format(
            self.increments["armor"]["increment"] * armor + self.increments["armor"]["base"])
        )
        self.magic_resistence = float("{0:.2f}".format(
            self.increments["magic_resistance"]["increment"] * magic + self.increments["magic_resistance"]["base"])
        )

        ## Others
        self.mp = float("{0:.2f}".format(
            self.increments["mp"]["increment"] * magic)
        )

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
        cost_mp = 0

        if type is TypeAttack.Magic:
            damage = attack - enemy.magic_resistence

            cost_mp = self.cost_mp

            if self.mp - self.cost_mp < 0:
                damage = 0
                cost_mp = 0
                print(Fore.RED + "Mp Onvoldoende" + Style.RESET_ALL)

        if type is TypeAttack.Physical:
            damage = attack - enemy.armor

            if random.choice(range(1, 100)) <= self.critical_chance:
                damage = (attack * self.critical_damage) - enemy.armor
                print(Fore.RED + "Critical Attack" + Style.RESET_ALL)

        if damage < 0:
            damage = 0

        self.mp -= cost_mp
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
        result += "| Magic: {}\tMagic Resistence: {}\tMp: {}\n"
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
            Fore.WHITE + str(self.mp) + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.critical_chance) + "%" + Style.RESET_ALL + Fore.GREEN,
            Fore.WHITE + str(self.critical_damage * 100) + "%" + Style.RESET_ALL + Fore.GREEN
        )