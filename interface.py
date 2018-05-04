from tkinter import *
import time
import random

WIDTH = 500
HEIGHT = 500

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
window.title("#TweetTwins")
canvas.pack()

canvas.create_text(10, 10, text="#TweetTwins", anchor=W)

textBox = Entry(canvas, width=20, bg="white", text="twitter username #1")
textBox.grid(row=1, column=0, sticky=W)
textBox2 = Entry(canvas, width=20, bg="white", text="twitter username #2")
textBox2.grid(row=2, column=0, sticky=W)

# add a submit button
#Button(bottomframe, text="Find", width=6, command=lambda: array.onClick(clickFind)).grid(row=0, column=2, sticky=W)
outputText = StringVar()
outputText.set('')
output = Label(canvas, textvariable=outputText, font="none 12 bold")
output.grid(row=0, column=3, sticky=E)

def close_window():
    window.destroy()
    exit()

# exit button
Button(canvas, text="EXIT", width=4, command=close_window).grid(row=3, column=0, sticky=W)
Button(canvas, text="ARE WE A MATCH?", width=15).grid(row=3, column=1, sticky=E)

window.mainloop()

