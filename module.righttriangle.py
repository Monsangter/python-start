import math


a=3
b=4
d=a**2 +b**2
c=math.sqrt(d)
print(c)


def hypotenuse(a, b):
    c=a**2+b**2
    return math.sqrt(c)

print(hypotenuse(3,4))
print(hypotenuse(10,20))