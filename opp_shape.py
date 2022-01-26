class Shape:

    area = 0

    def __add__(self, other):
        return self.area + other.area


class Shape1:
    def __cmp__(self, other):
        if self.area < other.area :
            return -1
        elif self.area == other.area :
            return 0
        else :
            return 1


a=Shape()
a.area = 20
b=Shape()
b.area = 10
print (a+b)
c=Shape1()
c.area = 1
d=Shape1()
d.area = 0

if c > d:
    print('C가 더 넓어요~')