class Item():

    def __init__(self, name, kind, treat):

        self.name = name
        self.kind = kind
        self.treat = treat     
    
    def eat(self, player):
        player.helf += self.treat

ready_items = {
    "good_food": [Item('Яблоко', 'food', 2), Item('Печенька','food', 1), Item('Куриная ножка','food', 4), Item('Дошик','food', 7)]
}
