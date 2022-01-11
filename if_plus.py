#양수는 영어로 positive number임
print('정수를 입력하세요 누적해서 더해드림다')
S = 0

while True:

    A = int(input()) #인풋도 반복문으로 넣어줘야한다.

    S += A

    if A < 0:
        break
print('s: ', S)