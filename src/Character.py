class Character(object):
    def __init__(self, heal = 3, attack = 3, armor = 3):
        self.heal = 7 * heal + 50
        self.attack = 3 * attack + 13
        self.armor = 2 * armor + 4
        self.shield = False

    def defend(self, enemy):
        damage = enemy.attack - self.armor

        if damage < 0:
            damage = 0

        self.heal -= damage

    def active_shield(self):
        if self.shield is False:
            self.armor *= 1.5
            self.shield = True

    def desactive_shield(self):
        if self.shield is True:
            self.armor /= 1.5
            self.shield = False

    def __repr__(self):
        return "Heal: {}\nAttack: {}\nArmor: {}".format(self.heal, self.attack, self.armor)