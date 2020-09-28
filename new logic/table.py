class Table():

    players = []
    monsters = []

    @staticmethod
    def addPlayer(player):
        Table.players.append(player)
    
    @staticmethod
    def addMonster(monster):
        Table.monsters.append(monster)

    @staticmethod
    def removePlayer(player):
        for i in range(len(Table.players)):
            if Table.players[i] == player: Table.players.pop(i)

    @staticmethod
    def removeMonster(monster):
        for i in range(len(Table.monsters)):
            if Table.monsters[i] == monster: Table.monsters.pop(i)

    @staticmethod
    def drow():
        print(f'{"♥" * Table.players[0].helf}        {Table.players[0].player_class}')
        print('\n1. Мои характеристики')
        print('2. Инвентарь')
        print('3. Сгенерировать предмет')
        if len(Table.monsters) != 0: print('4. Поход в подземелье')
        print('q. Выйти')
        print('\n\nВыберите действие')
        return input('Выйти ENTER: ')
    
    @staticmethod
    def player_info():
        print('Мои Характеристики:\n')
        print(f'Имя: {Table.players[0].name}')
        print(f'Класс: {Table.players[0].player_class}')
        print(f'Здоровье: {Table.players[0].helf}')
        print(f'Сила: {Table.players[0].power}')
        print(f'Оружие: {Table.players[0].weapon.name}')
        print(f'Места в рюкзаке: {Table.players[0].backpack.size-len(Table.players[0].backpack._open())}')
    
    @staticmethod
    def use_item(item):
        item = Table.players[0].backpack[int(item) - 1]
        if item.kind == 'food':
            chose = input(f'Вы хотите скушать {item.name} и востановить {item.treat} сердец ?(y/n)')
            if chose.lower() == 'y':
                Table.players[0].backpack[int(item) - 1].eat(Table.players[0])
                print(f'+ {"♥" * Table.players[0].backpack[int(item) - 1].treat}')
                Table.players[0].backpack.pop(int(item) - 1)
            else: pass

    
    @staticmethod
    def inventory():
        for i in range(len(Table.players[0].backpack._open())):
            print(f'{i+1}. {Table.players[0].backpack._open()[i].name}')

    @staticmethod 
    def new_item(item):
        print(f'В мире появился новый предмет {item.name} Востанавливает {item.treat}')
        return item
    
    @staticmethod
    def what_take(item):
        return input(f'Вы хотите подобрать {item.name} который востанавливает {item.treat} сердец ? (y/n) \n Выйти ENTER')