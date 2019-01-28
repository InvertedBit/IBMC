import tkinter
from tkinter import Tk, Label

root = Tk()
root.attributes('-fullscreen', True)


lblWelcome = Label(root, text='Welcome!')
lblWelcome.pack()


# Start Tk main loop
root.mainloop()
