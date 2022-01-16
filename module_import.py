'''
import tkinter
tkinter.widget = tkinter.Label(None, text='I love Python!')
'''
'''
from tkinter import *
widget = Label(None, text='I love Python!')
widget.pack()
'''
Label = 'This is a Label'
from tkinterpractice import *
print(type(label))

del tkinter

from importlib import reload
reload(tkinter)