from random import randint
import time



class Player():
    def __init__(self, name, hp, mental_hp, xp, dmg, mental_dmg, lvl):
        self.name = name
        self.hp = hp - Enemy.dmg
        self.mental_hp = mental_hp
        self.xp = xp
        self.is_alive = True
        self.dmg = dmg
        self.mental_dmg = mental_dmg
        self.lvl = lvl

    def set_hp(self, hp):
        
        self.hp = hp

        if(self.hp < 1):
            self.is_alive = False
            print("You have died and your body was paraded through town square on a pole.")

    def fight(self, enemy):
        enemy.set_hp(enemy.hp - self.dmg)
    
class Enemy():

    def __init__(self, name, hp, emotional_hp, xp, dmg, emotional_dmg):
        self.name = name
        self.hp = hp
        emotional_hp = emotional_hp
        self.xp = xp
        dmg = dmg
        self.emotional_dmg = emotional_dmg
        self.is_alive = True

    def set_hp(self, hp):
        self.hp = hp

        if(self.hp < 1):
            self.is_alive = False
            print(f"{self.name} was brutally destroyed")




player1 = Player("Riley", 200, 400, 0, 10, 0)

enemy1 = Enemy("Mom maked you food. It tasted bad", 100, 20, 100, 10, 5)
enemy2 = Enemy("Dad slaps you on the face. You did not enjoy it.", 125, 25, 10, 5, 5)
enemy3 = Enemy("You break a finger while beating up a Lamp Post.", 200, 10, 10, 10, 0)
enemy4 = Enemy("A Dog urinates on you.", 100, 20, 100, 10, 10)
enemy5 = Enemy("You hit a Tree. It is not like MineCraft.", 200, 10, 20, 10, 10)
enemy6 = Enemy("You get hit by a baby.", 25, 20, 100, 10, 5)
enemy7 = Enemy("Jeff is weird.", 50, 10, 50, 0, 10)
enemy8 = Enemy("A Police Car runs over you", 200, 20, 10, 25, 0)
enemy9 = Enemy("Kill this Pregnant Woman for double xp!", 50, 40, 10, 10, 5)
enemy10 = Enemy("you get ran over by a Car", 250, 50, 0,25, 25)
enemy11 = Enemy("A Police officer nearly arrests you.", 150, 10,2, 0, 10)
enemy12 = Enemy("Your Boss fires you", 50, 40, 1, 0, 10)
enemy13 = Enemy("Arsonist sets your house on fire", 250, 10, 0, 10)
enemy14 = Enemy("Merritt makes a joke about linzie.", 500, 100, 0, 0)
enemy15 = Enemy("A News car runs you over", 200, 100, 0, 10, 5)
enemy16 = Enemy("Walking Washington walks up toyou and comments first before you can.", 26, 26, 0.5)
enemy17 = Enemy("Fungal Sal appeared and dealt emotional damage.", 26, 26, 0.01)
enemy18 = Enemy("Funguy Ty appeared and sprayed spores in your face!", 26, 26, 1)
enemy19 = Enemy("Your hp went a holiday.", 26, 26, 50)
enemy20 = Enemy("Fungus grow on your face!", 26, 26, 10)



enemies = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6, enemy7, enemy8, enemy9, enemy10, enemy11, enemy12, enemy13, enemy14, enemy15, enemy16, enemy17, enemy18, enemy19, enemy20]

while(player1.is_alive):
    current_enemy =  enemies[randint(0,len(enemies)-1)]

    while current_enemy.is_alive:

        print(current_enemy.name)
        print(f"{player1.name} hp: {player1.hp} | {current_enemy.name} hp: {current_enemy.hp}")

        action = int(input("What would you like to do?\n1) fight\n2) run\n"))
        if action == 1:
            player1.fight(current_enemy)
        elif action ==2:
            player1.run()



    

    # if(enemy19 == True):
    #     time.sleep(10)
    # print(current_enemy.name)
    # print(player1.hp)
    # current_enemy.hp = (current_enemy.hp - player1.dmg)
    # player1.xp = (current_enemy.xp + player1.xp)
    # print(player1.xp)
    # player1.set_hp(current_enemy.dmg)
    # if player1.xp > 100:
    #     player1.lvl += 1
    #     player1.xp = 0
    #     player1.hp += 10
    # print("lvl" + str(player1.lvl))
    # time.sleep (1.5)