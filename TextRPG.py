import random
import time

userName = input("What is your name?:\n")
userName = userName.title()


print(f'Welcome to the kingdom {userName}, choose your class young warrior!')

counter = 0
while counter == 0:
    userClass = int(input("1. Swordsman \n2. Mage \n3. Archer\n"))
    if userClass == 1 or userClass == 2 or userClass == 3:
        counter = 1

if userClass == 1:
    userClassName = "Swordsman"
elif userClass == 2:
    userClassName = "Mage"
elif userClass == 3:
    userClassName = "Archer"
time.sleep(1)
print("As the sun dipped below the horizon, long and ancient shadows cast themselves across the winding forest path. \nYoung " +userName
      + " had set out on a journey to visit his beloved grandmother, deep in the heart of Eldoria. \nHowever, with each step, the woods grew darker and much more dangerous." +
      "\nBut young " + userName + " was not a stranger to danger, of course he was an extremely talented " + userClassName + " renowned around the kingdom."
      + "\nDespite his skills, he still felt nervous when he saw a giant green orc appear in the distance and felt that the coming battle would be extremely ferocious.")


class Swordsman:
    def __init__(self, damage=13, health=100, weapon = "sword"):
        self._damage = damage
        self._health = health
        self._weapon = weapon

    def get_damage(self):
        return self._damage

    def set_damage(self, x):
        self._damage = x

    def get_health(self,):
        return self._health

    def set_health(self, x):
        self._health = x

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, x):
        self._weapon = x

class Mage:
    def __init__(self, damage=20, health=75, weapon = "staff"):
        self._damage = damage
        self._health = health
        self._weapon = weapon

    def get_damage(self):
        return self._damage

    def set_damage(self, x):
        self._damage = x

    def get_health(self, ):
        return self._health

    def set_health(self, x):
        self._health = x

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, x):
        self._weapon = x

class Archer:
    def __init__(self, damage=27, health=55, weapon = "bow"):
        self._damage = damage
        self._health = health
        self._weapon = weapon
    def get_damage(self):
        return self._damage

    def set_damage(self, x):
        self._damage = x

    def get_health(self):
        return self._health

    def set_health(self, x):
        self._health = x

    def get_weapon(self):
        return self._weapon

    def set_weapon(self, x):
        self._weapon = x

class Orc:
    def __init__(self, damage=10, health=67):
        self._damage = damage
        self._health = health

    def get_damage(self):
        return self._damage

    def set_damage(self, x):
        self._damage = x

    def get_health(self, ):
        return self._health

    def set_health(self, x):
        self._health = x


orc = Orc()

def berserk():
    ranNum = random.randint(0,6)
    if ranNum > 3:
        orc.set_damage(orc.get_damage() * 2)
        time.sleep(1)
        print("The Orc has went berserk, his damaged has increased twofold and his aura is nearing unbearable.")


if userClass == 1:
    trueClass = Swordsman()
elif userClass == 2:
    trueClass = Mage()
elif userClass == 3:
    trueClass = Archer()


def playerAttack():
    if orc.get_health() < 43:
        berserk()
    orc.set_health(orc.get_health() - trueClass.get_damage())
    time.sleep(1)
    print(f"With masterful talent, you wield your {trueClass.get_weapon()} and strike the orc down.")
    if orc.get_health() > 0:
        print("The orc's health has fallen to " + str(orc.get_health()) + ".\n")
    else:
        print("You have slain the great orc that once seemed invincible.")

def enemyAttack():
    trueClass.set_health(trueClass.get_health() - orc.get_damage())
    time.sleep(1)
    randNum = random.randint(0, 3)
    if randNum == 1:
        print("The great orc swings down his mace on your chest with great force.\n")
    elif randNum == 2:
        print("The great orc thrusts his mace towards your shoulder with great force.\n")
    elif randNum == 3:
        print("The great orc wielding his mighty mace, forgoes it momentarily to strike you with his fists.\n")
    if trueClass.get_health() > 0:
        print(f"The {userClassName}'s health has fallen to " + str(trueClass.get_health()) + ".\n")
    else:
        print("\nYou have died as a result of the orc's great strength and ferocious tenacity.\n")

#playerAttack()

#print(str(trueClass.get_health()) + " trueclass get health")
#print(str(orc.get_health()) + " orc get health")


def run():
    ranNum = random.randint(0, 6)
    if ranNum > 3:
        trueClass.set_health(-333)

        time.sleep(1)
        print("\nYou have managed to escape the vicious orc successfully ")
    else:
        time.sleep(1)
        print("\nYou failed to run successfully")
        enemyAttack()

while trueClass.get_health() > 0 and orc.get_health() > 0:
    battleChoice = input("\nYou have entered combat:\n1.Fight\n2.Run\n")
    if battleChoice.lower() == "fight" or battleChoice == "1":
        enemyAttack()
        playerAttack()

    else:
        run()
time.sleep(.5)
if trueClass.get_health() > 0 or trueClass.get_health() == -333:
    print("\nDespite a vicious and unexpected foe appearing, you managed to free yourself from his grasp \n heading towards your grandmother's house, you feel a sense of relief.")
    print("\nHopefully, next time you visit your grandmother you won't run into such a fierce creature.")
else:
    print("Succumbing to the power of the great orc like the warriors of the past, \nyou feel a sense of regret that you won't be able to visit your grandmother one more time.")



#print(str(trueClass.get_health()) + " trueclass get health")
#print(str(orc.get_health()) + " orc get health")

