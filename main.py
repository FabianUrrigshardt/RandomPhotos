from tkinter import Tk
from tkinter import Image 
from tkinter import Canvas 
from PIL import ImageTk,Image 
import os



def smallerImg(img):
    x= int(img.size[0]/5)
    y= int(img.size[1]/5)

    ret = img.resize((x,y))
#Todo: Je nach Größe Parameter anpassen
    return ret


window = Tk()
window.title("Random Photo App")
window.geometry('800x800')


im = Image.open("a.jpg")

out = smallerImg(im)
img = ImageTk.PhotoImage(out)
#img = img.resize(100,100)

canvas = Canvas(window, width=600, height=600)
canvas.pack()
canvas.create_image(300,300, image=img)

window.mainloop()
