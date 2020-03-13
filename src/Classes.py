from __future__ import annotations
from classes.Warrior import Warrior
from classes.Paladin import Paladin

class Classes(object):
    @staticmethod
    def list():
        return [
            "Warrior",
            "Paladin"
        ]

    @staticmethod
    def dict():
        return {
            1: Warrior(),
            2: Paladin()
        }

    