class Fridge:
    def __init__(self):
        self.isOpened = False
        self.foods = []

    def open(self):
        self.isOpened = True
        print('냉장고 문을 열었어요...')

    def put(self, thing):
        if self.isOpened:
            self.foods.append(thing)
            print('냉장고 속에 음식이 들어갔네...')
        else:
            print('냉장고 문이 닫혀있어서 못 넣겠어요...')

    def close(self):
        self.isOpened = False
        print('냉장고 문을 닫았어요...')

class Food:
    pass

f = Fridge()
apple = Food()
elephant = Food()

print(f.open())
print(f.put(apple))
print(f.put(elephant))
print(f.foods)