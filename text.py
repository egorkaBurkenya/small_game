# start story about world
import time

def story(): 
    print("Здраствуй путник, эта история поведает тебе о молодом мальчике")
    time.sleep(4)
    print("...")
    time.sleep(1)
    print("Жизнь которого наполнилась ужасом и кровью....")
    time.sleep(2)
    print("после того как омерзительный правитель земли Ариган на его глазах...")
    time.sleep(4)
    print("убил его отца...")
    time.sleep(2)
    print('\n___________________________________________________________________')
    print("Введи свое имя и выбери свой класс путник ... Hero/Human/Dark/Hunter")
    print('___________________________________________________________________')

def loading():
    print('Загрузка мира', end='\r')
    i = 0
    while i < 3:
        print('Загрузка мира.  ', end='\r')
        time.sleep(0.5)
        print('Загрузка мира..', end='\r')
        time.sleep(0.5)
        print('Загрузка мира...', end='\r')
        time.sleep(0.5)
        i += 1

def drow_table(player, table_style = 'base'):
    if table_style == 'base':
        print(f'{"♥" * player.player_helf}   {player.player_class}')
        print('\n 1. Мои характеристики\n 2. Инвентарь\n 3. Сгенерировать предмет \n q. Выйти \n\nВыберите действие')
        return input('\n Цифра: ')
    
    if table_style == 'monster':
        print(f'{"♥" * player.player_helf}   {player.player_class}')
        print('\n 1. Мои характеристики\n 2. Инвентарь\n 3. Сгенерировать предмет \n 4. Сразиться с монстром \n q. Выйти \n\nВыберите действие')
        return input('\n Цифра: ')

def use_item(item, player):
    print(f'Хотите скушать {item.name} и востановить {item.skill}?')
    use = input('\nY/N ')
    if use.lower() == 'y':
        player.eat(item)
    if use.lower() == 'n': print('')