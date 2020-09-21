# player class and logic
from items import Weapon
from inventory import Inventory

class Player():

    def __init__(self, player_name, player_class):

        self.player_name = player_name
        self.player_class = player_class
        self.player_helf = 10
        self.player_inventory = Inventory()
        self.player_power = 1
        self.player_weapon = Weapon()
    
    def take(self, item):
        want_take = input(f'Вы хотите подобрать {item.info()} (Y/N)?')
        if want_take.lower() == 'y':
            self.player_inventory.put(item)
        else: pass

    def info(self): 
        print(f'Мои характеристики: \n\nИмя: {self.player_name}\nКласс: {self.player_class}\nЗдоровье: {self.player_helf}\nРазмер рюкзака: {self.player_inventory.max_len}\nСила: {self.player_power}\nОружие: {self.player_weapon.name}\n')

    def eat(self, food):
        self.player_helf += food.skill
        print('♥' * food.skill)