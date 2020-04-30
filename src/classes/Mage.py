from Character import Character

class Mage(Character):
    def __init__(self, life=3, attack=3, armor=3, magic=0):
        super().__init__(2, 1, 1, 6)
        self.type = "Mage"
        self.magic *= 1.2
        self.mp *= 3.5