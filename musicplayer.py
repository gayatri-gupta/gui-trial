import tkinter as tk
from tkinter import *
from mutagen.id3 import ID3
import pygame
import os
from tkinter.filedialog import askdirectory

root = tk.Tk()
root.title("Music Player")
root.minsize(300,300)
root.configure(background= "burlywood1")
v = StringVar()

lsngs = []
rnme = []
sngnme = StringVar()
idx = 0

songlabel = Label(root, textvariable=v,background = "burlywood1", relief = GROOVE)
songlabel.pack( fill =X)
def nxtsng():
    global idx
    idx-=1    
    pygame.mixer.music.load(lsngs[idx])
    pygame.mixer.music.play()
    updtlbl() 
def prevsng():
    global idx
    idx+=1 #idx-=1
    pygame.mixer.music.load(lsngs[idx])
    pygame.mixer.music.play()
    updtlbl()  

def stpsng():
    pygame.mixer.music.stop()
    v.set("")
    return sngnme
def updtlbl():
    global idx
    global sngnme
    v.set(rnme[idx])
    return sngnme

def chodir():
    dr = askdirectory()
    os.chdir(dr)

    for files in os.listdir(dr):
        if files.endswith(".mp3"):
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            rnme.append(audio["TIT2"].text[0])
            lsngs.append(files)
    pygame.mixer.init()
    pygame.mixer.music.load(lsngs[0])
    pygame.mixer.music.play()

chodir()    


listbox=Listbox(root, bg = "Brown4",fg = "snow")
listbox.pack( fill=BOTH)

for items in rnme:
    listbox.insert(0,items)
    
    nb = Button(root,text="Previous", width = 10, bg = "dark slate grey", fg = "white", command = prevsng)
nb.place(x = 10,y=200)

pb = Button(root,text="Stop", width = 10, bg = "dark slate grey", fg = "white", command = stpsng)
pb.place(x = 110,y=200)

sb = Button(root,text="Next", width = 10, bg = "dark slate grey" , fg = "white", command = nxtsng)
sb.place(x = 210,y=200)

sht = Button(root,text = "Quit",width = 10, bg = "dark slate grey" , fg = "white", command = lambda:root.quit())
sht.place(x = 10 , y = 240)

root.mainloop()
