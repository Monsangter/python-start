a=10
b=20
temp = a
a= b
b = temp

print(a, b)
##파이썬에선 이런식으로 두수의 값 바꾸기 가능.
c= 10
d= 20
c,d = d,c
print(c, d)

def magu_print(x,y,*rest):#*m은 나머지 전부를 가리킨다.
    print(x,y,rest)

#튜플만드는법
t=('a', 'b', 'c')
empty = ()
print(empty)
print(t)
one = (5)
two = (2,)
print(one)
print(two)#원소 하나만 가진 튜플을 만드려면 원소뒤에 콤마를꼭 해줘야 한다.

p=(1,2,3)
q=p[:1] + (5,) + p[2:]
print(q)
#리스트와 달리 직접 원소값을 창몾할 수 없어 오려붙이는 방법을 사용해야한다.

p=(1,2,3)
q=list(p)
print(q)

r= tuple(q)
print(r)