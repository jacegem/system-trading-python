from tkinter import *


def hello():
    print('Hello there')

tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()

canvas = Canvas(tk, width=500, height=500)
canvas.pack()


