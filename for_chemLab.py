temp_range=input()
max, min = map(int, temp_range.split())

temp = int(input())

while temp != -999:

    '''
    for n in b:
        if mintem <= n <= maxtem:
            print('Nothing to report')
        elif n == -999:
            break
        else:
            print('Alert!')
'''

'''
    one = input()  # 첫번째입력
    two = input()  # 두번째입력

    _min, _max = map(int, one.split())
    for n in map(int, two.split()):
        if n == -999:
            break
        elif _min <= n <= _max:
            print("Nothing to report")
        else:
            print("Alert!")
            break
            '''
#map 함수 map(적용할 함수, 반복가능한 객체)
#ex list(map(int,a))
#split 함수 (sep="",maxsplit="") sep 은 split 기준. 예를들어 "."일시 문장안에 있는 .를 기준으로 자른다.
#maxsplit은 몇번 쪼갤 것인가