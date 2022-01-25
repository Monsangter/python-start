class Book:

    def setData(self, title, price, author):
        self.title = title
        self.price = price
        self.author = author

    def printData(self):
        print('제목 : ', self.title)
        print('가격 : ', self.price)
        print('저자 : ', self.author)

    def __init__(self, title, price, author):
        self.setData(title, price, author)
        print('책 객체를 새로 만들었어요~')

    def __repr__(self):
        return self.title


b=Book()
b.setData('누가 내 치즈를 먹었을까', '300원', '미키')
b.printData()

b2=Book()
b2.setData('내가 먹었지롱', '200원', '미니')

b3=Book('나두 좀 줘', '100원', '쥐벼룩')