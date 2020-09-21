from item import Item

class Weapon(Item):
    
    def __init__(self, name, kind, power):
        
        super().__init__(name, kind, treat = '')
        self.power = power