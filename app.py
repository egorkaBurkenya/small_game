import random
import time
import os

class Player():

    players_count = 0

    def __init__(self, name, player_class = 'Human'):
        
        self.name = name
        self.player_class = player_class
        self.helf = 10
        self.player_inventory = []
        self.max_player_inventory = 5
        self.player_power = 1
    
    def take_something(self, something):
        if len(self.player_inventory) == self.max_player_inventory: print('Инвентарь полон')
        else:
            chose = input(f'Вы хотите подобрать {something.name} (Yes/No)? ')
            if chose.lower() == 'yes' or chose.lower() == 'y':
                something.take_it()
                self.player_inventory.append(something)
    def stats(self):
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        print('Характеристики персонажа')
        print(f'\nИмя: {self.name}')
        print(f'Класс: {self.player_class}')
        print(f'Запас здоровье: {self.helf}')
        print(f'Размер рюкзака: {self.max_player_inventory}')
        print(f'Сила: {self.player_power}')
        input('\nСкрыть характеристики ENTER')

    def open_inventory(self):
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        print('Инвентарь')
        for i in range(len(self.player_inventory)):
            print(f'{i+1}. {self.player_inventory[i].name}')
        use_item = input('\nЕсли хотите выбросить/использовать предмет, напишите его номер \n выйти ENTER ')
        if use_item == '':
            pass
        elif 'helf+' in self.player_inventory[int(use_item) - 1].skill:
            use_or_drop =input(f'\n\nвы хотите:\n1. Cъесть {self.player_inventory[int(use_item) - 1].name} и востановить {self.player_inventory[int(use_item) - 1].skill[-1]} жизний ?\n2. выбросить ?\n выйти ENTER ')
            if use_or_drop == "1":
                self.helf += int(self.player_inventory[int(use_item) - 1].skill[-1])
                print(f'+ {"♥" * int(self.player_inventory[int(use_item)-1].skill[-1])}')
                time.sleep(2)
            elif use_or_drop == '2':
                self.player_inventory.pop(int(use_item) - 1)
                print('предмет был выброшен')
                time.sleep(2)
            else: pass
        
        
        

        # except: 
        #     print('\nинвентарь пуст')
        #     input('\nСкрыть инвентарь ENTER')
        


    
class Item():

    def __init__(self, name, skill):

        self.name = name 
        self.skill = skill
    
    def take_it(self): 
        print(f'вы подобрали {self.name}')
        time.sleep(2)


class Weapon(Item):

    def __init__(self, name,  skill, ):

        super().__init__(name, skill)


class World():

    def __init__(self, name, max_players = 5, max_monsters = 10):

        self.name = name
        self.max_players = max_players
        self.max_monsters = max_monsters
        self.players = []
        self.items = []
        

    def join_to_world(self): 
        
        if Player.players_count == self.max_players: print('world is full...')
        else:
            self.players = [Player(input('name: '), input('class: ')) for i in range(self.max_players)]

    def drow_table(self, table_css = 'base'):
        if table_css == 'base':
            os.system(['clear', 'cls'][os.name == os.sys.platform])
            print(f'{"♥" * self.players[0].helf}   {self.players[0].player_class}')
            print('\n 1. Мои характеристики\n 2. Инвентарь\n 3. Выйти \n\nВыберите действие')
            return input('\n Цифра: ')

    def start_play(self):
        if self.max_players == 1:
            os.system(['clear', 'cls'][os.name == os.sys.platform])
            print(f'Приветствую {self.players[0].name}...\n')
        start_chose = input('Желаешь начать игру ?(Yes/No) ')
        if start_chose.lower() == "yes" or start_chose.lower() == "y":
            os.system(['clear', 'cls'][os.name == os.sys.platform])
            print("Начнем же веселье !!!!!!!!!!!!!!!")
            time.sleep(2)
        elif start_chose.lower() == "no" or start_chose.lower() == "n":
            print('Возвращайся в другой раз путник')
            time.sleep(5)
            exit()       

    def generate_item(self, name = ''):

        if name == '':

            items_food = ['apple', 'cooke', 'cake']
            items_weapon = ['sword', 'stick', 'gun']

            type_of_item = 1
            
            if  type_of_item == 1:
                food = random.randint(0,len(items_food)-1)
                item = Item(items_food[food], f'helf+{random.randint(1,5)}')
                print(f'в мире появился новый прдмет {item.name}')
                self.items.append(item)
    










# world_1.start_play()

# item_1 = Item('apple', 'food', '')

# world_1.players[0].take_something(item_1)

# world_1.generate_item()
