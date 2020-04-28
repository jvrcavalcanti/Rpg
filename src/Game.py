from Character import Character
from Classes import Classes
import random as rand
import os
from colorama import Fore, Style


class Game(object):
    def __init__(self):
        self.player: Character = None
        self.enemy: Character = None

    def get_classes(self, op):
        return Classes.dict()[op]()

    def run_command(self, op, cha: Character, cha2: Character):
        cha.desative_shield()
        return {
            1: cha.weak_attack,
            2: cha.strong_attack,
            3: cha.magic_attack,
            4: cha.active_shield
        }[op](cha2)

    def start(self):
        print("\nEscolha a classe")

        classes = Classes.list()

        op = self.user_input(classes)
        
        while op not in range(1, len(classes) + 1):
            op = self.user_input(classes)

        self.player = self.get_classes(op)
        self.enemy = self.get_classes(rand.randint(1, len(classes)))


    def end(self):
        self.player.update()
        self.enemy.update()
        
        print(Fore.RED)
        print("\n/************************ End game ********************************/")
        print(Style.RESET_ALL)

        print("\nPlayer:\n{}\n".format(self.player))
        print("\nEnemy:\n{}\n".format(self.enemy))

        if self.player.life < 1:
            print("\nEnemy win")

        if self.enemy.life < 1:
            print("\nPlayer win")

        os.system("pause")

    def user_input(self, commands):
        try:
            print(Fore.CYAN)
            template = "\nEscolha uma opção para fazer uma ação:"
            i = 1
            for command in commands:
                template += "\n" + command + ": " + str(i)
                i += 1

            op = int(input(template + "\n"))

            if op not in range(1, len(commands) + 1):
                print("\nOpção inválida")
                return None
            print(Style.RESET_ALL)

            return op
        except Exception:
            print(Fore.RED)
            print("Opção inválida")
            print(Style.RESET_ALL)


    def run(self):
        round = 1

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

                op = self.user_input(["Weak Attack", "Strong Attack", "Magic Attack", "Defender"])

                if op is None:
                    round = 1
                    continue

                self.run_command(op, self.player, self.enemy)
                
            if round == 1:
                op = rand.randint(1, 5)

                if self.enemy.wait > 0:
                    self.enemy.wait -= 1
                    continue

                if op == 5:
                    op = 1

                self.run_command(op, self.enemy, self.player)
        self.end()
        