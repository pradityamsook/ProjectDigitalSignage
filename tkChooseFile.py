from Tkinter import Tk
from tkFileDialog import askopenfilename
def chooseFile():
    Tk().withdraw()
    filename = askopenfilename()
    print(filename)
List = ['0']
while chooseFile:
    List.insert(0,str(chooseFile))
    x = List
    print(x)
