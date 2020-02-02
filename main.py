from src.Character import Character
import random as rand

points = 6
state = [1, 1, 1]

print("\n{} restantes\n".format(points))

while points > 0:
    try:
        print("/******************************************************************************/")
        op = int(input("Escolha uma opção para colocar o ponto:\nHeal: 1\nAttack: 2\nArmor: 3\n"))
        state[op - 1] += 1
        points -= 1
    except Exception:
        print("\nValor incorreto")
        continue
    finally:
        print("\n{} restantes\n".format(points))

ch = Character(state[0], state[1], state[2])
# print("\nPlayer:\n{}".format(ch))

random_state = rand.choices([0, 1, 2], k = 6)
state = [1, 1, 1]
for i in random_state:
    state[i - 1] += 1
enemy = Character(state[0], state[1], state[2])
# print("\nEnemy:\n{}".format(enemy))

round = rand.randint(0, 1)

while enemy.heal > 0 and  ch.heal > 0:
    if round == 0:
        print("\nPlayer:\n{}\n".format(ch))
        print("\nEnemy:\n{}\n".format(enemy))
    if round == 0:
        try:
            op = int(input("Escolha uma opção para fazer uma ação:\nAttack: 1\nDefender: 2\n"))
        except Exception:
            print("Opção inválida")

        if op is 1:
            enemy.defend(ch)
            if ch.shield:
                ch.desactive_shield()

        if op is 2:
            ch.active_shield()
    if round is 1:
        op = rand.randint(1, 4)

        if op is 1 or op is 3:
            ch.defend(enemy)
            if enemy.shield:
                enemy.desactive_shield()

        if op is 2:
            enemy.active_shield()

    round = 1 if round == 0 else 0

print("\n/************************ End game ********************************/")

print("\nPlayer:\n{}\n".format(ch))
print("\nEnemy:\n{}\n".format(enemy))

if ch.heal < 1:
    print("\nEnemy win")

if enemy.heal < 1:
    print("\nPlayer win")