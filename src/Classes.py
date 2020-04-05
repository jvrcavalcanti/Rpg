from __future__ import annotations
from classes.Warrior import Warrior
from classes.Paladin import Paladin
from classes.Mage import Mage
from classes.Assassin import Assassin

class Classes(object):
    @staticmethod
    def list():
        return [
            "Warrior",
            "Paladin",
            "Mage",
            "Assassin"
        ]

    @staticmethod
    def dict():
        return {
            1: Warrior,
            2: Paladin,
            3: Mage,
            4: Assassin
        }

    