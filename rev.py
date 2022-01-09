number = 358

rem = rev = 0
while number >= 1:
    rem = number % 10
    rev = rev * 10 + rem
    number = number // 10 #//나누기 연산 후 소수점 이하의 수를 버리고 정수 부분의 수만 구함.
'''1회 실행 이후. rem 8 rev 8 num 35
2회실행 이후 rem 5 rev 85 num 3
3회 실행 이후 rem 8 rev 853 num 0 '''
print(rev)