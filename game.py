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
    world_1.players[0].take_something(world_1.items[0])
except: pass


while True:
    player_chose = world_1.drow_table()
    if player_chose == '1':
        world_1.players[0].stats()
    if player_chose == '2':
        world_1.players[0].open_inventory()
    if player_chose == '3':
        try: world_1.players[0].take_something(world_1.generate_item())
        except: pass



