import vlc
import sys

import Tkinter as Tk
from Tkinter import *

class ClassName(Object):
	"""docstring for ClassName"""
	def createWigets(self):
		self.entry = StringVar()
		self.setEntry = Entry(textvariable = entry)
		self.setEntry.pack()

	def __init__(self, master = None):
		Object.__init__(self, master)
		self.pack()
		self.createWidgets()
		
root = Tk()
app  = ClassName(master=root)
app.mainloop()
root.destroy()
	