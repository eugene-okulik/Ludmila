class Flower:
    def __init__(self, name, color, stem_length, cost, lifespan):
        self.name = name
        self.color = color
        self.stem_length = stem_length
        self.cost = cost
        self.lifespan = lifespan

    def __repr__(self):
        return f'{self.name}({self.color}, {self.stem_length}cm, ${self.cost}, {self.lifespan} days)'


class Rose(Flower):
    def __init__(self, color, stem_length, cost, lifespan):
        super().__init__('Rose', color, stem_length, cost, lifespan)

class Tulip(Flower):
    def __init__(self, color, stem_length, cost, lifespan):
        super().__init__('Tulip', color, stem_length, cost, lifespan)


class Lily(Flower):
    def __init__(self, color, stem_length, cost, lifespan):
        super().__init__('Lily', color, stem_length, cost, lifespan)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_cost(self):
        return sum(flower.cost for flower in self.flowers)

    def average_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers(self, key, value):
        return [flower for flower in self.flowers if getattr(flower, key) == value]

    def __repr__(self):
        return f'Bouquet({self.flowers})'


rose1 = Rose('red', 40, 5, 7)
rose2 = Rose('white', 35, 4.5, 7)
tulip1 = Tulip('yellow', 30, 3, 5)
lily1 = Lily('pink', 50, 6, 10)
