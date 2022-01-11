def korean_number(a):
    if a == 1:
        print('일')
    elif a == 2:
        print('이')
    elif a == 3:
        print('삼')
    elif a == 4:
        print('사')
    elif a == 5:
        print('오')
    elif a == 6:
        print('육')
    elif a == 7:
        print('칠')
    elif a == 8:
        print('팔')
    elif a == 9:
        print('구')
    elif a == 10:
        print('십')


a=int(input('한국어로 읽는 법을 알고 싶은 숫자를 입력하세요'))
#파이썬은 대소문자를 구별한다.
korean_number(a)