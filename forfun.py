import tkinter
from tkinter import *
import random as rd


def random():
    button.place(x=rd.randint(0, 500), y=rd.randint(0, 500))


def random2():
    button2.place(x=rd.randint(0, 500), y=rd.randint(0, 500))


def random3():
    button3.place(x=rd.randint(0, 500), y=rd.randint(0, 500))


main = tkinter.Tk()
button = Button(main, text="CLICK", command=random)
button2 = Button(main, text="CLICK", command=random2)
button3 = Button(main, text="CLICK", command=random3)
button.place(x=rd.randint(0, 200), y=rd.randint(0, 200))
button2.place(x=rd.randint(0, 200), y=rd.randint(0, 200))
button3.place(x=rd.randint(0, 200), y=rd.randint(0, 200))
main.mainloop()
