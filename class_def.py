from random import randint, random
import os

class bcolors:
    pink = '\033[95m'
    blue = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'

class Monster:

    def __init__(self,level,diademe):
        self.level = level
        if diademe:
            self.pv = (5 * level) /2
        else:
            self.pv = 5 * level
        print(bcolors.yellow + f"The monster has {self.pv} pv \n")

    def attack(self, hero):
        print(bcolors.yellow +"The monster attack")
        attack_amount = int(((9 + self.level)/10) * randint(1, 10))
        hero.pv -= attack_amount
        print(bcolors.yellow +f"You lost {attack_amount} pv, your life is now:{max(0,hero.pv)} \n")
        input("(press enter)")


    def die(self,hero):  
        print(bcolors.green +f"The monster is dead")
        if random() < 0.2:
            print(bcolors.green +f"Oh my god, this is a perigourdin diademe, all the monster are now weaker \n")
            hero.diademe = True
        input("(press enter)")


    def play(self,hero):
        if self.pv > 0:
            self.attack(hero)
        else:
            self.die(hero)

class Healer(Monster):
    def heal(self):
        print(bcolors.yellow +"The monster heals itself")
        self.pv+=10

    def play(self,hero):
        if self.pv > 0:
            if random() < 0.2:
                self.heal()
            else:
                self.attack(hero)
        else:
            self.die(hero)



class Hero:
    def __init__(self):
        self.pv = 100
        self.nb_potion = 3
        self.diademe = False

    def attack(self,monster):
        print(bcolors.blue +"You attack")
        attack_amount = randint(1, 10)
        monster.pv -= attack_amount
        print(bcolors.blue + f"The monster lost {attack_amount} pv, his life is now:{max(0,monster.pv)} \n")

    def take_potion(self):
        if self.nb_potion != 0:
            potion_amount = randint(30,60)
            self.pv += potion_amount
            self.nb_potion -= 1
            print(bcolors.blue +f"You get back {potion_amount} pv, your life is now {self.pv}, you have {self.nb_potion} potions left \n")
        else:
            print(bcolors.red +"malheur plus de potion, un tour de gaché \n")
    
    def play(self,monster):
        decision = input(bcolors.blue +"Press 'Enter' to attack or 'P' to take a potion \n")
        while True:
            if decision == '':
                self.attack(monster)
                break
            elif decision.upper() == 'P':
                self.take_potion()
                break
            else:
                print(bcolors.red +"Wrong Answer \n")
                decision = input(bcolors.blue +"Press 'Enter'to attack or 'P' to take a potion \n")

def pick_a_monster(level, diademe):
    if random() < 0.2:
        print(bcolors.yellow + f"A new monster comes, be careful, it is a healer")
        return Healer(level , diademe)
    else:
        print(bcolors.yellow + f"A new monster comes, it's a classic monster")
        return Monster(level , diademe)
