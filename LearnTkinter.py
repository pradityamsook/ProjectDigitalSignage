from tkinter import *
import tkinter.messagebox as Tk

def doNothing(self):
	self.str make = "Show text"
	return print(make)
def showSomething(self):
	self.str show = "Show message hahaha"
	return print(show)

root = Tk()

menu = Menu(root)
root.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New Project", command = doNothing)
subMenu.add_command(label = "New", command = doNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = showSomething)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", command = editMenu)
editMenu.add_command(label = "Redo", command = doNothing)


# **** The Toolbar ****
toolbar = Frame(root, bg = "blue")

insert = Button(toolbar, text = "insert Image", command = doNothing)
insertButton.pack(side = LEFT, padx = 2, pady = 2)
printButt = Button(toolbar, text = "Print", command = doNothing)
printButt.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

#***** Status bar *****
status = Label(root, text = "Praparing to do nothing...", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)


#***Messge Box***
Tk.messagebox.showinfo('Window Title', 'Mokneys can like up to 300 years.')
anwer = Tk.messagebox.askquestion('Question 1', 'Do you like Icecream?')

if anwer == 'yes':
	Tk.messagebox.showinfo('Oh man!')


root.mainloop()
