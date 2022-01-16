import tkinter
window=tkinter.Tk()
window.title("Bae Sang Do")
window.geometry("640x400+100+100")
window.resizable(False,False)

label=tkinter.Label(window, text="파이썬", height=5, bg="white", relief="solid")
label.pack()

window.mainloop()