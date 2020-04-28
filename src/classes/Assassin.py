from Character import Character

class Assassin(Character):
    def __init__(self, life=3, attack=3, armor=3, magic=0):
        super().__init__(3, 5, 2)
        self.type = "Assassin"
        self.strong_increment -= 0.45
        self.weaK_increment -= 0.3