import vlc
import sys

import Tkinter as Tk
from Tkinter import *
'''
if sys.version_info[0] < 3:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter.filedialog import askopenfilename
else:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename'''

import os
import pathlib                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
import platform

instance = vlc.Instance('--mouse-hide-timeout=0', '--fullscreen', '--repeat')
player = instance.media_player_new()
media = instance.media_new('test.mp4')

class Application(Frame):
    def playVlc(self):
        media.get_mrl()
        player.set_fullscreen(True)
        player.set_media(media)
        player.play()
        player.audio_set_volume(0)

    def playVlcNotFullscrn(self):
        media.get_mrl()
        player.set_media(media)
        player.play()
        player.audio_set_volume(0)
        
    def createWidgets(self):
        '''part of button quit'''
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit

        self.QUIT.pack({"side": "right"})

        #part of full screen
        self.hi_there = Button(self)
        self.hi_there["text"] = "PLAY FULL SCREEN"
        self.hi_there["command"] = self.playVlc

        self.hi_there.pack({"side": "left"})

        #part of default
        self.getPlay = Button(self)
        self.getPlay["text"] = "PLAY DEFUALT WINDOW"
        self.getPlay["command"] = self.playVlcNotFullscrn

        self.getPlay.pack({"side": "left"})
        

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()


#main of play application
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
