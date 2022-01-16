import random
random.random()
#0~1의 무작위 숫자 하나 뽑아 돌려줌

#randrange는 1~6

random.randrange(1,7)#1이상 7미만

abc=['a', 'b', 'c', 'd', 'e']
random.shuffle(abc)
print(abc)
random.shuffle(abc)
print(abc)

print(random.choice(abc))

menu = '졸면', '육계장', '비빔밥'
print(random.choice(menu))

print(random.choice([True,False]))