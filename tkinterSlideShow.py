from Tkinter import *
from PIL import Image, ImageTk
import random

class MyApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        fr = Frame(self)
        fr.pack()
        self.canvas  = Canvas(fr, height = 400, width = 600)
        self.canvas.pack()

        self.old_label_image = None
        self.position = 0
        self.getcommand()
        self.slideshow()

    def slideshow (self):

        file = str(self.position) + '001.jpg' + '002.jpg'
        image1 = Image.open(file)
        self.tkpi = ImageTk.PhotoImage(image1)
        label_image = Label(self, image=self.tkpi)
        label_image.place(x=0,y=0,width=image1.size[0],height=image1.size[1])
        self.title("Title: " + file + " - " + str(self.lastCommand))

        if self.old_label_image is not None:
            self.old_label_image.destroy()
        self.old_label_image = label_image

        if self.position is not 1:
            self.position = self.position + 1
        else:
            self.position = 0

          #currently switches title between 0 and 1 ok
        int = random.randint(2000, 5000)
        huh = self.after(int, self.slideshow)
          #self.after_cancel(huh) - works ! so maybe can do from below Fn?

    def getcommand (self):
        self.lastCommand = 8
        self.after(2000, self.getcommand)
          # if changes then pause slide show after x seconds randint
          # and display commanded for ... set time
          # then start slideshow again

if __name__ == "__main__":
    root = MyApp()
    root.mainloop()
