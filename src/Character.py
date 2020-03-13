class Character(object):
    def __init__(self, life = 3, attack = 3, armor = 3):
        self.type = "Character"

        # Base
        self.life = float("{0:.2f}".format(life ** 2 + 50))
        self.attack = float("{0:.2f}".format(2.75 * attack + 18))
        self.armor = float("{0:.2f}".format(2.5 * armor + 10))

        # Increments
        self.shield_increment = 1.2
        self.strong_increment = 1.2

        # others
        self.shield = False
        self.wait = 0

    def update(self):
        self.life = float("{0:.2f}".format(self.life))
        self.attack = float("{0:.2f}".format(self.attack))
        self.armor = float("{0:.2f}".format(self.armor))

    def weak_attack(self, enemy):
        damage = self.attack - enemy.armor

        if damage < 0:
             damage = 0

        enemy.life -= damage

    def strong_attack(self, enemy):
        damage = (self.attack * self.strong_increment) - enemy.armor

        if damage < 0:
            damage = 0

        enemy.life -= damage
        self.wait += 1

    def active_shield(self):
        if self.shield is False:
            self.armor *= self.shield_increment
            self.shield = True

    def desative_shield(self):
        if self.shield is True:
            self.armor /= self.shield_increment
            self.shield = False

    def __repr__(self):
        return "Type: {}\nLife: {}\nAttack: {}\nArmor: {}".format(self.type, self.life, self.attack, self.armor)