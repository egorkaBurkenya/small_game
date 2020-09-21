from func import *
from world import World
from table import Table
import os

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
        print('\nНапишите цифру предмета, который хотите использовать')
        what_item = input('\n Выйти ENTER')
        if what_item == '': pass
        else: 
            World.players[0].backpack.use_item(what_item)

