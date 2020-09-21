from inventory import Inventory
from item import Weapon

class Player():
    
    def __init__(self, name, player_class):

        self.name = name
        self.player_class = player_class
        self.helf = 10
        self.backpack = Inventory()
        self.power = 1
        self.weapon = Weapon('heand', '0', '')

    def to_treat(self, food):
        self.helf += food.treat
        self.backpack.drop(food)
    
    