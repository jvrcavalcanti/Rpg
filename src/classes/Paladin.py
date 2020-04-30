from Character import Character


class Paladin(Character):
    def __init__(self):
        super().__init__(4, 2, 2, 2)
        self.type = "Paladin"
        self.shield_increment += 0.1
        self.armor *= 1.3

    def active_shield(self, enemy):
        if self.shield is False:
            self.armor *= self.shield_increment
            self.magic_resistence *= self.shield_increment
            self.shield = True

    def desative_shield(self):
        if self.shield is True:
            self.armor /= self.shield_increment
            self.magic_resistence /= self.shield_increment
            self.shield = False