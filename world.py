# world class 
from player import Player
from items import *
from monster import Monster
import random

class World():
    
    def __init__(self, name, max_players = 5, max_monsters = 10):

        self.name = name
        self.max_players = max_players
        self.max_monsters = max_monsters
        self.players = []
        self.monsters = []
        self.items = []
        
    def join_to_world(self):     
        if len(self.players) == self.max_players: print('world is full...')
        else:
            name = input('Имя: ')
            player_class = input('Класс: ')
            if player_class.lower() in ['hero', 'human', 'Dark', 'Hunter']:
                self.players = [Player(name, player_class) for i in range(self.max_players)]
            else: print('такого класса не существует')
    
    def generate_item(self, name = '', skill = 0, item_type = ''):

        if name == '':
            items_food = ['apple', 'cooke', 'cake']
            items_weapon = ['sword', 'stick', 'gun']
            item_type = random.randint(1,2)
            if  item_type == 1:
                food = random.randint(0,len(items_food)-1)
                item = Item(items_food[food], random.randint(1,5))
                print(f'в мире появился новый прдмет {item.name}')
                self.items.append(item)  
                return item
            elif item_type == 2:
                weapon = random.randint(0,len(items_weapon)-1)
                item = Weapon(items_weapon[weapon] ,random.randint(1,10))
                print(f'в мире появилось новое оружие {item.name}')
                self.items.append(item)   
                return item
        else: 
            if item_type == 'food': self.items.append(Item(name, skill, item_type))
            elif item_type == 'weapon': self.items.append(Weapon(name, skill, item_type))

        
    def generate_monster(self): 

        monster_type = ['zombie', 'dark hero']

        self.monsters.append(Monster(monster_type[random.randint(0,len(monster_type) - 1)], random.randint(1,7), random.randint(1,40)))
        print(f'в мире появился монстр {self.monsters[-1].monster_type}')

    # def fight_with_monster(self, player, monster, world):
    #     os.system(['clear', 'cls'][os.name == os.sys.platform])
    #     print('Монстр в вашем поле зрении !')
    #     print('\n   Монстр: ' + self.monsters[-1].monster_type)
    #     print('   Сила: ' + str(self.monsters[-1].power))
    #     print('   Здоровье: ' + str(self.monsters[-1].helf))

    #     player_chose = input(f'\nРешишься ли ты зразиться с {self.monsters[-1].monster_type} путник ? (Y/N) ')
    #     if player_chose.lower() == 'n' or player_chose.lower() == 'no':
    #         print('Значит в следующий раз', end='\r')    
    #         time.sleep(0.5)  
    #         print('Значит в следующий раз.  ', end='\r')
    #         time.sleep(0.5)
    #         print('Значит в следующий раз..', end='\r')
    #         time.sleep(0.5)
    #         print('Значит в следующий раз...', end='\r')
    #         time.sleep(0.5)
    #     elif player_chose.lower() == 'yes' or player_chose.lower() == 'y':
    #         os.system(['clear', 'cls'][os.name == os.sys.platform])
    #         print('Да начнется битва!!!!!!!\n\n')
    #         time.sleep(2)
    #         while monster.helf != 0 or player.helf != 0:
    #             os.system(['clear', 'cls'][os.name == os.sys.platform])
    #             print(f'{player.name.upper()}')
    #             print(f'Здоровье: {"♥" * player.helf} ({player.helf})')
    #             print(f'Оружте: {player.weapon.name}')
    #             print(f'Сила: {player.player_power}')
    #             print(f'\n{monster.monster_type.upper()}')
    #             print(f'Здоровье: {"♥" * monster.helf} ({monster.helf})')
    #             print(f'Сила: {monster.power}')
    #             chanse = random.randint(1,2)
    #             print(f'\n\nВы разбегаетесь и хотите нанести удар... {monster.monster_type} тоже готовиться атаковать...\n')
    #             player_fight = input('У вас есть несколько секунд на раздумие.. \n 1. Нанести удар \n 2. Отскочить \n 3. Открыть Инвентарь \n 4. Убежать \n Что ты сделаешь ? ')
    #             what_will_be = random.randint(1,3)
    #             if player_fight == '2':
    #                 if what_will_be == 3:
    #                     print(f'Вы делаете резкий прыжек назад...\n {monster.monster_type} промахивается и снова заносит орудие!')
    #                 else:
    #                     print('\n')
    #                     player.damage_from_monster(monster.power//2)
    #                     input('\nENTER')
    #             elif player_fight == '1':
    #                 if what_will_be == 3: 
    #                     print('\n')
    #                     monster.damage_from_player(player.player_power)
    #                     input('\nENTER')
    #                 elif what_will_be == 1: 
    #                     print('Вы промахнулись...')
    #                 elif what_will_be == 2:
    #                     print('Монстр Увернулся ...')
    #                     c = random.randint(1,5)
    #                     if c == 5:
    #                         print('и не много задел вас')
    #                         player.damage_from_monster(monster.power//2)
    #                         input('\nENTER')
    #                     if c == 1 or c == 2:
    #                         print('Вам все же удалось задеть врага')
    #                         monster.damage_from_player(player.player_power//2)
    #                         input('\nENTER')
    #             elif player_fight == '3':
    #                 player.open_inventory()
    #             elif player_fight == '4':
    #                 print('Ты пытаешься скрыться от монстра..')
    #                 c = random.randint(1,4)
    #                 if c != 3:
    #                     print('Беги путник !!! Бегии !!!')
    #                     time.sleep(2)
    #                     break
    #             if monster.helf <= 0: 
    #                 print('Это ваша заслуженная победа !\n твоя награда')
    #                 player.take_something(world.generate_item())
    #                 time.sleep(2)
    #                 break
    #             elif player.helf <= 0:
    #                 print('Монстр убил вас ....... тут должна быть смерть, но я ее пока не сделал')
    #                 time.sleep(2)
    #                 break
    #             time.sleep(2)