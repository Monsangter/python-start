import tkinter as tk

s = "Life is short\n Use Python"

window = tk.Tk()
t= tk.Text(window, height= 4, width = 8)
t.insert(tk.END, s)
t.pack()
tk.mainloop()
