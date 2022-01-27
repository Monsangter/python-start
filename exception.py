def f(a,  b):
    try:
        if a and b:
            return (a * b) + (a / b)
        elif a:
            return '불능'
        else:
            return '부정'
    except:
        return '똑바로 살아라'


print(f(4,2))
print(f(3,0))
print(f(0,0))
print(f(30000000,5000000))