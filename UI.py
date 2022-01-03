import tkinter
from tkinter import *
import random as rd


def random():
    button.place(x=rd.randint(0, 500), y=rd.randint(0, 500))


main = tkinter.Tk()
button = Button(main, text="aimlab lowbudget", command=random)
button.place(x=rd.randint(0, 500), y=rd.randint(0, 500))
main.mainloop()

main2 = tkinter.Tk()
main2.mainloop()
