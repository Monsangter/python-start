dic = {}
dic['dictionary'] = '1. A reference book contating an...'
dic['python'] = 'Any of various nonvenomous snakes of the...'
print(dic['dictionary'])

smalldic = {'dictionary': 'reference','python': 'snake'}
print(smalldic['python'])

#딕셔너리 자료형은 키와 값의 쌍으로 이루어 진다.

del smalldic['dictionary']

family= {'boy':'choi', 'girl': 'kim', 'baby':'choi'}
print(family)
family.keys()
print(family.keys())
family.values()
print(family.values())
print('boy' in family)
print('sister' in family)#key 값 확인임.
print('choi' in family)