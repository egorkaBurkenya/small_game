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
        print(f'{'♥' * Table.players[0].helf}        {Table.players[0].player_class}')
        print('\n 1. Мои характеристики')
        print('2. Инвентарь')
        print('3. Сгенерировать предмет')
        if len(Table.monsters) != 0: print('4. Поход в подземелье')
        print('q. Выйти')
        print('\n\nВыберите действие')
        return input('Выйти ENTER: ')
    
