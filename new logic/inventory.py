class Inventory():

    def __init__(self):

        self.backpack = []
        self.max_len = 5
    
    def put(self, item):
        self.backpack.append(item)
    
    def drop(self, item):
        if type(item) != type(1):
            for i in range(len(self.backpack)): if self.backpack[i] == item: self.backpack.pop[i] 
        else: self.backpack.pop(item - 1)
            