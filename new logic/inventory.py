class Inventory():

    def __init__(self):

        self.backpack = []
        self.size = 5
    
    def put(self, item):
        self.backpack.append(item)
    
    def drop(self, item):
        if type(item) != type(1):
            for i in range(len(self.backpack)): 
                if self.backpack[i] == item: 
                    self.backpack.popi) 
        else: self.backpack.pop(item - 1)
    
    def _open(self):
        return self.backpack
    
    def use_item(self, item_number):
            a = self.backpack[int(item_number) - 1]
            return a
        

            