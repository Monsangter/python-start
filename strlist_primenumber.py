inp = int(input('구하고 싶은 자연수 범위를 입력하세오\n'))
b = list(range(2,inp+1))
d = []
print(b)

'''
for i in b:


    if i/2!=1 or i/2== 0:
        b.remove(i/2)
    elif i/3!=1 or i/3 == 0:
        b.remove(i/3)
    elif i/5!=1 or i/5 == 0:
        b.remove(i/5)
    else:
      d.append()

print(b)
'''

for i in b:
    if i!=2 or i%2 == 0:
        b.remove(i)
    elif i%3 == 0:
        b.remove(i)
    elif i%5 == 0:
        b.remove(i)
    elif i%7 == 0:
        b.remove(i)
    elif i%11 == 0:
        b.remove(i)
    elif i%13 == 0:
        b.remove(i)

print(b)