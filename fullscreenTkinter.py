from tkinter import *

window = Tk()
canvas = Canvas(window, width=1400, height=820, bg="SteelBlue2")
canvas.pack()

xposition = 0
yposition = 0

temperature = "46"
message = "The temperature right now is " + temperature
indepth = "Its a clear night"


def moveleft(event):
    global yposition, xposition
    if yposition == 0 and xposition > -2:
        x = 0
        for i in range(40):
            canvas.move('test', x, 0)
            canvas.after(10)
            canvas.update()
            x -= 1
        xposition -= 1


def moveright(event):
    global yposition, xposition
    if yposition == 0 and xposition < 2:
        xposition += 1
        x = 0
        for i in range(40):
            canvas.move('test', x, 0)
            canvas.after(10)
            canvas.update()
            x += 1


def moveup(event):
    global i
    global yposition, xposition
    if xposition == 0 and yposition == 0:
        yposition += 1
        x = 0
        for i in range(10):
            canvas.move('test', 0, x)
            canvas.after(10)
            canvas.update()
            x -= 1
        i = canvas.create_text(700, 400, text=indepth, font=('Helvetica Neue UltraLight', 50),
                               fill="white", anchor='c')


def movedown(event):
    global i
    global yposition, xposition
    if xposition == 0 and yposition == 1:
        yposition -= 1
        x = 0
        canvas.delete(i)
        for i in range(10):
            canvas.move('test', 0, x)
            canvas.after(10)
            canvas.update()
            x += 1


test = canvas.create_text(700, 400, text=message, font=('Helvetica Neue UltraLight', 50),
                          fill="white", anchor='c', tag='test')

window.bind("<Left>", moveright)
window.bind("<Right>", moveleft)
window.bind("<Up>", moveup)
window.bind("<Down>", movedown)

window.mainloop()
