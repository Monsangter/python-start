from functools import reduce
reduce(lambda x, y: x + y, [0, 1, 2, 3, 4])

print(reduce(lambda x, y: x + y, [0, 1, 2, 3, 4]))

#reduce 는 (함수, 시퀀스의 순서를 띈다. 시퀀스를 전부다 더함.

reduce(lambda x, y: y + x, 'abcde')

print(reduce(lambda x, y: y + x, 'abcde'))
#역순 배열