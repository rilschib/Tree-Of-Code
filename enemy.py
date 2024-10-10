class Enemy():
    def __init__(self, name, Class, enemyhp, enemyxp, enemydmg, enemylevel, enemyspeed, u, v, w):
        self.name = name
        self.Class = Class
        self.hp = enemyhp
        self.xp = enemyxp
        self.dmg = enemydmg
        self.lvl = enemylevel
        self.speed = enemyspeed
        self.statrewardU = u
        self.statrewardV = v
        self.statrewardW = w
        self.is_alive = True

