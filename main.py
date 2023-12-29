import os
from class_def import bcolors, Hero, Monster, Healer, pick_a_monster

os.system('cls' if os.name == 'nt' else 'clear')
print(bcolors.pink + 'A new game start \n')

super_hero = Hero()

nb_monster = 10

level = 1

while super_hero.pv > 0 and nb_monster > 0:
    monster = pick_a_monster(level, super_hero.diademe)
    level +=1
    nb_monster-=1
    while super_hero.pv > 0 and monster.pv > 0:
        super_hero.play(monster)
        monster.play(super_hero)
        os.system('cls' if os.name == 'nt' else 'clear')
        

if super_hero.pv <= 0:
    print(bcolors.red +"GAME OVER YOU ARE DEAD \n")
    print(bcolors.green +f"Your score is {(9-nb_monster)} points \n")
else:
    print(bcolors.green + "YOU WIN \n")
    print(bcolors.green + f"Your score is 10 points \n")