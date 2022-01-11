def cal_tri():
    a = input('밑변과 높이 순으로 공백으로 구분해 입력하세요\n')
    legs, height=map(int, a.split())
    #split하면 자료형 str로 바뀜

    result = legs * height / 2
    return result

a=cal_tri()

print(a)