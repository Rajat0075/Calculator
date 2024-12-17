from tkinter import *
from tkinter import ttk

window = Tk()
window.iconbitmap('')
frame = ttk.Frame(window, padding=10).grid()
ttk.Label(frame, text="Calculator").grid(column=0,row=0)
ttk.Button(frame, text="Solved", command=window.destroy).grid(column=1,row=0)
window.mainloop()
