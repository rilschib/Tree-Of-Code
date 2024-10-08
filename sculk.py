
class player1():
    def __init__(self, name, hp, xp, dmg, lvl, speed):
        self.name = name

        self.hp = a - self.dmg
        self.xp = 1
        self.dmg = b
        self.lvl = 1
        self.speed = c
        self.is_alive = True

class Enemy():

    def __init__(self, name, Class, enemyhp, enemyxp, enemydmg, enemylevel, enemyspeed):
        self.name = name
        self.Class = Class
        self.hp = enemyhp
        self.xp = enemyxp
        self.dmg = enemydmg
        self.lvl = enemylevel
        self.speed = enemyspeed
        self.is_alive = True

    def set_hp(self, hp):
        
        self.hp = hp

        if(self.hp < 1):
            print("You have died your body turned into sculk... You may start again from your save or quit now.")
            self.is_alive = False
    def fight(self, hp, enemy, enemydmg, dmg, speed, enemyhp, enemyspeed):
        if speed > enemyspeed:
            self.hp(self.enemyhp - self.dmg)
            self.hp(self.hp - self.enemydmg)
        elif speed < enemyspeed:
    

            def set_hp(self, hp):
                self.hp = hp

        if(self.hp < 1):
            self.is_alive = False
            return(f"{self.name} was brutally destroyed")

        if(self.enemyhp < 1):
            self.is_alive=false
        else:
            self.enemyis_alive = True
            player1 = Player(name, Class, a, xp, b, lvl, c)

enemy1 = Enemy("Steve accidentaly activates a sculk shrieker", 2, 1, 1, 5, 0.5, 5)
enemy2 = Enemy("Alex sets spawn in the deep dark, and doing so forgot to sneak and activates a shrieker", 2, 1, 1, 5, 0.5, 5)



enemies = [enemy1, enemy2]
def fight(self, hp):
    while(self.hp > 0):
        current_enemy =  enemies[randint(0,len(enemies)-1)]

    while current_enemy.is_alive:

        print(current_enemy.name)
        print(f"{player1.name} hp: {player1.hp} | {current_enemy.name} hp: {current_enemy.hp}")

        action = int(input("What would you like to do?\n1) fight\n2) run\n3) save\n4)"))
        if action == 1:
            player1.fight(current_enemy)
        elif action ==2:
            player1.run()
def load_game_progress():
    try:  # Try loading the local save game file ("game_progress.txt").
        with open('game_progress.txt') as f:
            if input("Load your existing game? (Y/N) ").lower() == "y":
                return int(f.readlines()[0])  # If player chose to load game, load last index from save file.
            else:
                print("Starting a new game...")
                return 1  # If player chose to start a new game, set index to 1.
    except:  # If save game file wasn't found, start a new game instead.
        print("Starting a new game...")
        return 1