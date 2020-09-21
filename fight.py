from logic import *

def fight_setting(monster_number, monsters):
    print('Да начнется бой !')
    if type(monster_number) != type(0): return monsters[monster_number - 1]
    else:
        print('Удачи тебе путник, целая армия врагов ! а ты смельчак!') 
        return monsters
     



    