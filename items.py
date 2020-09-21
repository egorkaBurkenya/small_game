# class items and logick

class Item():
    
    def __init__(self, name, skill = 1, item_type = 'food'):

        self.name = name 
        self.skill = skill
    
    def info(self):
        info = f'{self.name} востановит вам {self.skill} едениц здоровья'
        return info
    
class Weapon(Item):

    def __init__(self, name = 'heand',  skill = 0, item_type = 'weapon'):

        super().__init__(name, skill, item_type)
    
    def info(self):
        info = f'{self.name} атака {self.skill} едениц'
        return info