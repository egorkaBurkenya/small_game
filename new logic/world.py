from player import Player
from monster import Monster

class World():

    players = []
    monsters = []
    items = []
    level = 1

    @staticmethod
    def regPlayer(name, player_class):
        World.players.append(Player(name, player_class))
    
    @staticmethod
    def spawnMonster(kind, power, helf):
        World.monsters.append(Monster(kind, power, helf))
    
    @staticmethod
    def killMonster(monster):
        for i in range(len(World.monsters)): 
            if World.monsters[i] == monster: 
                World.monsters.pop(i)
    
    @staticmethod
    def new_item(item):
        World.items.append(item)

    @staticmethod    
    def take_item(item):
        World.players[0].backpack.put(item)
        for i in range(len(World.items)):
            if World.items[i] == item: World.items.pop(i)