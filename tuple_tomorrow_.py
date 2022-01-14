today = input('년 월 일 을 공백으로 구분하여 입력하시오.\n')
y,m,d=today.split()

print(d+'/'+m+'/'+y)

year_toggle=0

if y % 400 == 0:
    a=1
elif y % 100 == 0:
    a=0
elif y % 4 == 0:
    a=1
else :
    a=0

month_toggle=0
if m == 1,3,5,7,9,11:
    if d== 32:
        m = m+1
        d = 1
elif m == 4,6,8,10:
    if d== 31:
        m = m+1
        d = 1
elif m == 12:
    if d== 31:
        m = 1
        y += 1

