import random
import time

class Player():

    players_count = 0

    def __init__(self, name, palyer_class = 'Human'):
        
        self.name = name
        self.palyer_class = palyer_class
        self.helf = 10
        self.player_inventory = []
        self.max_player_inventory = 5
        self.player_power = 1
    
    def take_something(self, something):
        if len(self.player_inventory) == self.max_player_inventory: print('Инвентарь полон')
        else:
            chose = input(f'Вы хотите подобрать {something.name} (Yes/No)? ')
            if chose.lower() == 'yes':
                something.take_it()
                self.player_inventory.append(something)


    
class Item():

    def __init__(self, name, item_type, skill):

        self.name = name 
        self.item_type = item_type
        self.skill = skill
    
    def take_it(self): 
        print(f'вы подобрали {self.name}')



class World():

    def __init__(self, name, max_players = 5, max_monsters = 10):

        self.name = name
        self.max_players = max_players
        self.max_monsters = max_monsters
        self.players = []
        self.items = []
        global players

    def join_to_world(self): 
        
        if Player.players_count == self.max_players: print('world is full...')
        else:
            self.players = [Player(input('name: '), input('class: ')) for i in range(self.max_players)]

    def start_play(self):
        if self.max_players == 1:
            print(f'\n\n\nПриветствую {self.players[0].name}...\n\n')
    def drow_table(self):
        print(f'{"♥" * self.players[0].helf}   {self.players[0].palyer_class}')
            

    def generate_item(self, name = '', item_type = ''):

        if name == '':

            items_food = ['apple', 'cooke', 'cake']
            items_weapon = ['sword', 'stick', 'gun']

            type_of_item = 1
            
            if  type_of_item == 1:
                food = random.randint(0,len(items_food)-1)
                item = Item(items_food[food], 'food', '')
                print(f'в мире появился новый прдмет {item.name}')
                self.items.append(item)
    










# world_1.start_play()

# item_1 = Item('apple', 'food', '')

# world_1.players[0].take_something(item_1)

# world_1.generate_item()
