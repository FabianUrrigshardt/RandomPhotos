from tkinter import Tk
from tkinter import Image 
from tkinter import Canvas 
from tkinter import Button
from PIL import ImageTk,Image 
import os
import collections
import random

def smallerImg(img):
    x=img.size[0]
    y=img.size[1]
    z=1 #Faktor der Vergrößerung
    
    if x>3400:
        z=4
    elif x>2000:
        z=3
    elif x>1200:
        z=2
    
    x=int(img.size[0]/z)
    y=int(img.size[1]/z)

    return img.resize((x,y))

def testComand():
    return

def getImgList():
    ret = collections.deque()
    for sfld in os.listdir('images'):
        for im in os.listdir(os.path.join('images',sfld)):
            print(im)
            ret.append(im)         
    return ret    

def getRandomImg(imgList):
    #rand = random.randint(1,imgList.maxlen())
    rand = 1
    while rand > 0:
        ret=imgList.pop()
        rand = rand -1
    return ret

imgList = getImgList()

window = Tk()
window.title("Random Photo App")
window.geometry('800x800')

im = Image.open(getRandomImg(imgList))
out = smallerImg(im)
img = ImageTk.PhotoImage(out)


canvas = Canvas(window, width=600, height=600)
canvas.pack()
canvas.create_image(300,300, image=img)

btNext = Button(window, text="nächstes Bild", command=testComand())
btNext.pack()


window.mainloop()
