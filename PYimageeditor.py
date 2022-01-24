from asyncio.windows_events import NULL
from tkinter import *
from PIL import Image,ImageTk,ImageEnhance
# from tkinter import Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from buttons import buttons
from tkinter.filedialog import askopenfile
import ctypes
import colorsys


ctypes.windll.shcore.SetProcessDpiAwareness(1000)

root = Tk()
root.geometry("1000x1000")


my_canvas1 = Canvas(root,width=1220,height=780, bg="lightgray")
my_canvas1.place(x=320,y=30)


    
def open():

    global img
    global label
    global im_resize
    global im
    my_canvas1.img_name = filedialog.askopenfilename(title="Select Image",filetypes=(("png files","*.png"),("jpg files","*.jpg")))
    im = Image.open(my_canvas1.img_name)
    im_resize = im.resize((1200,780))
    img = ImageTk.PhotoImage(im_resize) 
    label = Label(my_canvas1,image=img)
    label.place(x=1,y=0)
    
    

def select_crop():
    pass


def crop():
    pass
  
  
def flip_vert():
    global new
    global im ,im_g
    global label
    im = im.transpose(Image.FLIP_TOP_BOTTOM)
    im_g= im.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)

    label.configure(image=new)

def flip_hori():
    global im,im_g,new,label
    im = im.transpose(Image.FLIP_LEFT_RIGHT)
    im_g = im.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)
    label.configure(image=new)


def BnW():
    global im,im_g,new,label
    im = im.convert("L")
    
    im_g = im.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)
    label.configure(image=new)


my_canvas = Canvas(root, width=00,height=900 ,bg="white")
my_canvas.place(x=0,y=30)


def Saturation():
    global im,new,label,im_g
    filter = ImageEnhance.Color(im)
    img = im.filter(3)
    im_g = img.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)
    label.configure(image=new)
    






save = Button(root,text="Save" , bg = "white")
save.grid(row=0,column=0,padx=2,pady=2,ipadx=10)


open = Button(root,text="Open" , bg = "white",command=open)
open.grid(row=0,column=1,padx=2,pady=2,ipadx=10)

#helllo hhhh

buttons(my_canvas,crop,select_crop,flip_hori,flip_vert,BnW,Saturation)

img = PhotoImage(file="abcd.png",width=1300,height=900)
my_image = my_canvas1.create_image(200,200 , anchor = NW , image = img)




root.mainloop()