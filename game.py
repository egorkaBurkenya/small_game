from app import *
import time








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



