d = int(input())
m = 0
b = []

while True:

    d, m = divmod(d,2)#divmod는 튜플로 몫과 나머지 반환
    b.insert(0, m)#어펜드는 리스트의 마지막에 삽입하는 함수. insert(a,b)는 위치 a에 b삽입
    #insert(0을 쓰니까 앞부분부터 채워짐.
    if d == 0:
        break

print(b)