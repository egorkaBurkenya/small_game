# main fail
from world import World
from player import Player
from logic import *
import time
import os 
import random

world = World('World', 1)
# story()
while True:
    world.join_to_world()
    if len(world.players) != 0: break
# loading()

while True:
    os.system(['clear', 'cls'][os.name == os.sys.platform])
    if random.randint(1, 10) == 2: 
        world.generate_monster()
        print('\n')
        time.sleep(2)
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
        useItem = input(': ') 
        if useItem != '': 
            try: 
                use_item(world.players[-1].player_inventory.backpack[int(useItem)-1], world.players[-1], int(useItem) - 1)
            except: pass
            time.sleep(2)
        else: pass
    elif player_chose == '3': 
        world.players[-1].take(world.generate_item())
    elif player_chose == '4' and table_type == 'monster':
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        for i in world.monsters: 
            drow_monster(i)
        print('\nС каким моснтром ты желаешь сразиться путник?')
        print('Что бы сразиться со всеми монстрами напиши "all" ')
        print('Выйти ENTER')
        fight(input('\nЦифра: '))
    elif player_chose == 'q':
        print('Возвращайся в другой раз путник ...')
        time.sleep(2)
        exit()
    