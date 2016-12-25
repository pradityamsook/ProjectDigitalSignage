# ImageTk may need a separate install on Linux
from PIL import ImageTk
import time
try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk


# create the root window
root = tk.Tk()
# set ULC (x, y) position of root window
root.geometry("+{}+{}".format(70, 100))
root.title("a simple Tkinter slide show")

# delay in seconds (time each slide shows)
delay = 3

# create a list of image file names
# (you can add more files as needed)
# pick image files you have in your working directory or use full path
# PIL's ImageTk allows .gif  .jpg  .png  .bmp formats
imageFiles = [
"001.jpg",
"002.jpg"]#,
#"../image/A_Dog03.jpg",
#"../image/A_Dog04.jpg",
#"../image/Flowers.jpg"


# create a list of image objects
# PIL's ImageTk converts to an image object that Tkinter can handle
photos = [ImageTk.PhotoImage(file=fname) for fname in imageFiles]

# use a button to display the slides
# this way a simple mouse click on the picture-button stops the show
button = tk.Button(root, command=root.destroy)
button.pack(padx=5, pady=5)

for photo in photos:
    button["image"] = photo
    root.update()
    time.sleep(delay)

# execute the event loop
root.mainloop()
