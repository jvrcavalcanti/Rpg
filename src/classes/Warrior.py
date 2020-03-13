from Character import Character


class Warrior(Character):
    def __init__(self):
        super().__init__(5, 4, 3)
        self.type = "Warrior"
        self.strong_increment += 0.1