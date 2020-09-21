class Inventory():

    def __init__(self):

        self.backpack = []
        self.max_len = 5
    
    def open_backpack(self):
        if len(self.backpack) == 0: print('Рюкзак пуст')
        else: 
            for i in range(len(self.backpack)):
                print(f'{i+1}. {self.backpack[i].name}')
            if len(self.backpack) == self.max_len: print('Рюкзак заполен')

    def put(self, item):
        if len(self.backpack) == self.max_len: print('В вашем рюкзаке нет места...')
        else:
            print(f'Вы подобрали {item.name}')
            self.backpack.append(item)
    
