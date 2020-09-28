from func import *
from world import World
from table import Table
from item import Item, ready_items

import os
import random

# time_print("Здраствуй путник, эта история поведает тебе о молодом мальчике", 4)
# time_print("...", 1)
# time_print("Жизнь которого наполнилась ужасом и кровью....", 2)
# time_print("после того как омерзительный правитель земли Ариган на его глазах...", 4)
# time_print("убил его отца...", 2)
# print('\n___________________________________________________________________')
# print("Введи свое имя и выбери свой класс путник ... Hero/Human/Dark/Hunter")
# print('___________________________________________________________________')

World.regPlayer(input('name: '), input('class: '))

# print('Загрузка мира', end='\r')
# i = 0
# while i < 3:
#     print('Загрузка мира.  ', end='\r')
#     time.sleep(0.5)
#     print('Загрузка мира..', end='\r')
#     time.sleep(0.5)
#     print('Загрузка мира...', end='\r')
#     time.sleep(0.5)
#     i += 1
Table.addPlayer(World.players[-1])
while True:
    os.system(['clear', 'cls'][os.name == os.sys.platform])
    chose = Table.drow()
    if chose == '1':
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        Table.player_info()
        what_item = input('\n Выйти ENTER')
    elif chose == '2':
        os.system(['clear', 'cls'][os.name == os.sys.platform])
        Table.inventory()
        print('\nНапишите цифру предмета, который хотите использовать')    
        what_item = input('Выйти ENTER')
        if what_item == '': pass
        else:
            
            item = World.players[0].backpack.use_item(what_item)
            if item.kind == 'food': 
                what_do = input(f'Вы хотите \n1. скушать{item.name} и востановить {item.treat} сердец\n 2. выбросить {item.name} \n\n Выйти ENTER ')
                if what_do == '1': 
                    World.players[0].to_treat(item)
                    print(f'+ {"♥" * item.treat}')
                elif what_do == '2': 
                    World.players[0].backpack.drop(item)
                    print(f'Вы выбросили {item.name}')

    elif chose == '3':
        World.new_item(ready_items["good_food"][random.randint(0, len(ready_items) - 1)])
        if Table.what_take(World.items[-1]).lower() == 'y':
            World.take_item(World.items[-1])
            

        
                

