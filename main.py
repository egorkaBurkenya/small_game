# main fail
from world import World
from player import Player
from text import *
import time
import os 

world = World('World', 1)
# story()
while True:
    world.join_to_world()
    if len(world.players) != 0: break
# loading()

while True:
    os.system(['clear', 'cls'][os.name == os.sys.platform])
    if len(world.monsters) != 0: 
        table_type = 'monster'
    else: table_type = 'base'
    player_chose = drow_table(world.players[-1], table_type)
    if player_chose == '1':
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        world.players[-1].info()
        input('Выход ENTER')
    elif player_chose == '2':
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        world.players[-1].player_inventory.open_backpack()
        print('\nВыберите предмет')
        print('Выйти ENTER')
        use_item = input('\nЦифра: ')
        
    elif player_chose == '3':
        pass
    elif player_chose == '4' and table_type == 'monster_spaun':
        pass
    elif player_chose == 'q': 
        print('Возвращайся в другой раз путник ...')
        time.sleep(2)
        exit()
    