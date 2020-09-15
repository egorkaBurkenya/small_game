from app import *
import time


# print("Здраствуй путник, эта история поведает тебе о молодом мальчике")
# time.sleep(4)
# print("...")
# time.sleep(1)
# print("Жизнь которого наполнилась ужасом и кровью....")
# time.sleep(2)
# print("после того как омерзительный правитель земли Ариган на его глазах...")
# time.sleep(4)
# print("убил его отца...")
# time.sleep(2)
# print('\n___________________________________________________________________')
# print("Введи свое имя и выбери свой класс путник ... Hero/Human/Dark/Hunter")
# print('___________________________________________________________________')

world_1 = World('World', 1)

world_1.join_to_world()

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

world_1.start_play()

world_1.generate_item()
try:
    world_1.players[0].take_something(world_1.items[-1])
except: pass

world_1.generate_monster()

while True:
    if len(world_1.monsters) == 0:
        player_chose = world_1.drow_table()
    else:
        table_type = 'monster_spaun'
        player_chose = world_1.drow_table(table_type)
    if player_chose == '1':
        world_1.players[0].stats()
    elif player_chose == '2':
        world_1.players[0].open_inventory()
    elif player_chose == '3':
        try: world_1.players[0].take_something(world_1.generate_item())
        except: pass
    elif player_chose == '4' and table_type == 'monster_spaun':
        world_1.fight_with_monster(world_1.players[-1], world_1.monsters[-1], world_1)
    elif player_chose == '4': 
        print('Возвращайся в другой раз путник ...')
        time.sleep(2)
        exit()



