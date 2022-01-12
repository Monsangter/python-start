'''모듈을 불러오는 방법으로는 import 모듈
from 모듈 import 이름 두가지가 있다.
첫뻔쨰는 모듈 전체를 두번째는 필요한 것만 콕 찝어서 들고온다.
import tkinter
tkinter.widget = tkinter.Label(None, text='I love Python!')
tkinter.widget.pack()
import 는 모듈, 변수 이름을 계속 유지해줘야하지만 from은
from tkinter import *
widget = Label(None, text='I love Python!')
widget.pack()
'''
'''
from datetime import datetime
today = datetime.today()
today
datetime.datetime(2021, 3, 21, 15, 46, 1, 94942)

today.year
2021

'''
def korean_age(birth_year):
    from datetime import datetime
    today = datetime.today()
    return today.year - birth_year + 1

print(korean_age(2000))