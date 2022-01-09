print("정수를 입력해주세요. 제곱표를 만들어드립니당")

A=int(input())
B=1

while B <= A: #콜론 붙이는 거 잊지 말 것.
    #c는 지역변수로서 선언해주자.
    C = B ** 2
    print (B, C)
    B+=1