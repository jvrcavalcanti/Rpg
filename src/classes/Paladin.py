from Character import Character


class Paladin(Character):
    def __init__(self):
        super().__init__(4, 1, 4, 1)
        self.type = "Paladin"
        self.shield_increment += 0.3