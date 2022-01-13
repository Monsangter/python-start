score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]
#divmod(a,b) 매개 변수로 받은 a를 b로 나눕니다. 그리고 그 몫과 나머지를 튜플로 반환합니다
#(3,1)

print(score)

def stem_leaf():
    stem_leaf=[[],[],[]]
    for i in score:
        if i/10<1:
            stem_leaf[0].append(i)
        elif i/10<2:
            stem_leaf[1].append(i)
        elif i/10<3:
            stem_leaf[2].append(i)

    print('0:', stem_leaf[0])
    print('1:', stem_leaf[1])
    print('2:', stem_leaf[2])

stem_leaf()