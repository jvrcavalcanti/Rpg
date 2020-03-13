from Character import Character
from classes.Warrior import Warrior
from classes.Paladin import Paladin
import random as rand
import os


class Game(object):
    def __init__(self):
        self.player: Character = None
        self.enemy: Character = None
        self.classes = ["Warrior", "Paladin"]

    def get_classes(self, op):
        return {
            1: Warrior(),
            2: Paladin()
        }[op]

    def start(self):
        print("\nEscolha a classe")

        op = self.user_input(self.classes)
        
        while op not in range(1, len(self.classes) + 1):
            op = self.user_input(self.classes)

        self.player = self.get_classes(op)
        self.enemy = self.get_classes(rand.randint(1, len(self.classes)))


    def end(self):
        self.player.update()
        self.enemy.update()
        
        print("\n/************************ End game ********************************/")

        print("\nPlayer:\n{}\n".format(self.player))
        print("\nEnemy:\n{}\n".format(self.enemy))

        if self.player.life < 1:
            print("\nEnemy win")

        if self.enemy.life < 1:
            print("\nPlayer win")

        os.system("pause")

    def user_input(self, commands):
        try:
            template = "\nEscolha uma opção para fazer uma ação:"
            i = 1
            for command in commands:
                template += "\n" + command + ": " + str(i)
                i += 1

            op = int(input(template + "\n"))

            if op not in range(1, len(commands) + 1):
                print("\nOpção inválida")
                return None

            return op
        except Exception:
            print("\nOpção inválida")


    def run(self):
        round = rand.randint(0, 1)

        while self.enemy.life > 0 and  self.player.life > 0:
            self.player.update()
            self.enemy.update()

            round = 1 if round == 0 else 0

            if round == 0:
                print("\nPlayer:\n{}".format(self.player))
                print("\nEnemy:\n{}".format(self.enemy))

            if round == 0:
                if self.player.wait > 0:
                    self.player.wait -= 1
                    print("\nEm espera")
                    continue

                op = self.user_input(["Weak Attack", "Defender", "Strong Attack"])

                if op == 1:
                    self.player.weak_attack(self.enemy)

                if op == 3:
                    self.player.strong_attack(self.enemy)

                if op == 2:
                    self.player.active_shield()
                else:
                    self.player.desative_shield()

            if round == 1:
                op = rand.randint(1, 5)

                if self.enemy.wait > 0:
                    self.enemy.wait -= 1
                    continue

                if op == 1 or op == 3:
                    self.enemy.weak_attack(self.player)

                if op == 4:
                    self.enemy.strong_attack(self.player)

                if op == 2:
                    self.enemy.active_shield()
                else:
                    self.enemy.desative_shield()
        self.end()
        