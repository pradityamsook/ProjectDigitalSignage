import vlc
import sys

try:
    import Tkinter as Tk
    from Tkinter import ttk
    from Tkinter.filedialog import askopenfilename
except ImportError:
    import tkinter as Tk
    from tkinter import ttk
    from tkinter.filedialog import askopenfilename
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
from threading import Timer,Thread,Event
import time
import platform

instance = vlc.Instance('--mouse-hide-timeout=0', '--fullscreen', '--repeat')
player = instance.media_player_new()
media = instance.media_new('test.mp4')


def 

class Application(Frame):
    def PlayVlc(self):
        self.media.get_mrl()
        self.player.set_fullscreen(True)
        self.player.set_media(media)
        self.player.play()
        self.player.audio_set_volume(0)

    def playVlcNotFullscrn(self):
        self.media.get_mrl()
        self.player.set_media(media)
        self.player.play()
        self.player.audio_set_volume(0)
        
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


def openPlayFullScreen(self):
    """Part of open file video from ,FullScreen"""
    self.OnStop()

    bring = pathlib.Path(os.path.expanduser("~"))
    fullname = askopenfilename(initialdir = bring, title = "Choose your file", 
                fileytpes = (("all files", "*.*"),("mp4 files", "*.mp4")))
    if os.path.isfile(fullname):
        print(fullname)
        Split = os.path.split(fullname)
        dirname = os.path.dirname(fullname)
        filename = os.path.basename(fullname)

        self.Media = self.instance.media_new(str(os.path.join(dirname, filename)))
        self.player.set_media(self.Media)

        if platform.system() == 'Windows':
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle())
        self.PlayVlc()


def openPlayNotFullScreen():
    """Part of open file video from ,FullScreen"""
    self.OnStop()

    bring = pathlib.Path(os.path.expanduser("~"))
    fullname = askopenfilename(initialdir = bring, title = "Choose your file", 
                fileytpes = (("all files", "*.*"),("mp4 files", "*.mp4")))
    if os.path.isfile(fullname):
        print(fullname)
        Split = os.path.split(fullname)
        dirname = os.path.dirname(fullname)
        filename = os.path.basename(fullname)

        self.Media = self.instance.media_new(str(os.path.join(dirname, filename)))
        self.player.set_media(self.Media)

        if platform.system() == 'Windows':
            self.player.set_hwnd(self.GetHandle())
        else:
            self.player.set_xwindow(self.GetHandle())
        self.OnPlay()

def OnPlayNotFullScreen(self):
    """Play Video"""
    if not self.player.get_media():
        self.openPlayFullScreen()
    else:
        if self.player.play == -1:
            self.errorDialog("Unable to play.")

def OnPlayFullscreen(self):
    self.media.get_mrl()
    self.player.set_fullscreen(True)
    self.player.set_media(media)
    self.player.play()
    self.player.audio_set_volume(0)

def OnStop(self):
    """Stop Video"""
    self.player.stop()
    self.timeslider.set(0)



def GetHandel(self):
    return self.videopanel.winfo_id()

def errorDialog(self, errormessage):
    errordialog = Tk.tkMessageBox,showerror(self, 'Error', errormessage)

#main of play application
root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
