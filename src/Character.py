class Character(object):
    def __init__(self, heal = 3, attack = 3, armor = 3):
        self.heal = float("{0:.2f}".format(2 ** heal + 50))
        self.attack = float("{0:.2f}".format(2.75 * attack + 18))
        self.armor = float("{0:.2f}".format(2.5 * armor + 10))
        self.shield = False
        self.wait = 0

    def weak_attack(self, enemy):
        damage = self.attack - enemy.armor

        if damage < 0:
             damage =0

        enemy.heal -= damage

    def strong_attack(self, enemy):
        damage = (self.attack * 1.5) - enemy.armor

        if damage < 0:
            damage = 0

        enemy.heal -= damage
        self.wait += 1

    def active_shield(self):
        if self.shield is False:
            self.armor *= 1.2
            self.shield = True

    def desative_shield(self):
        if self.shield is True:
            self.armor /= 1.2
            self.shield = False

    def __repr__(self):
        return "Heal: {}\nAttack: {}\nArmor: {}".format(self.heal, self.attack, self.armor)