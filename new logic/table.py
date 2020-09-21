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
        if item.kind == 'food':
            print('')
    
