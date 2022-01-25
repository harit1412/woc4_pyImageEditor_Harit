from asyncio.windows_events import NULL
from tkinter import *
from tkinter.messagebox import askyesno
from PIL import Image,ImageTk,ImageEnhance
# from tkinter import Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from buttons import buttons

import ctypes
import colorsys
import cv2




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
    global new
    global im ,im_g,i
    global label 
    im_g= im.resize((1200,780))
    i = im_g.crop([200,500,600,300])
    new = ImageTk.PhotoImage(i)
    label.config(image=new)

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

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


def Sat_in(self):
  global im,new,label,im_g,img
  global a
  filter = ImageEnhance.Color(im)
  a = satu_scale.get()
  img = filter.enhance(a)
  im_g = img.resize((1200,780))
  new = ImageTk.PhotoImage(im_g)
  label.configure(image=new)

def Saturation():
    global ans
    ans = askyesno(title = "Confirmation",message = "Do you want to change?")  
    if ans : 
        pass
       
    else :
        # satu_scale.set("0")
        global im,new,label,im_g,img
        im_resize = im.resize((1200,780))
        img = ImageTk.PhotoImage(im_resize) 
        label.configure(image=img)
        
    
satu_scale = Scale(my_canvas, from_= -100 , to=100, orient = 'horizontal',bg="yellow",fg="black",command = Sat_in)
satu_scale.grid(row=4,column=1,padx=2,pady=5)

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


def sharp_in(self):  
    global im,new,label,im_g,img,b
    b = sharp_scale.get()
    filter = ImageEnhance.Sharpness(im)
    img = filter.enhance(b)
    im_g = img.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)
    label.configure(image=new)
    


def sharp():
    global ans
    ans = askyesno(title = "Confirmation",message = "Do you want to change?")  
    if ans : 
        pass
       
    else :
        global im,new,label,im_g,img
        im_resize = im.resize((1200,780))
        img = ImageTk.PhotoImage(im_resize) 
        label.configure(image=img)    
        sharp_scale.set("0")




sharp_scale = Scale(my_canvas, from_= 0 , to=100, orient = 'horizontal',bg="yellow",fg="black",command =sharp_in)
sharp_scale.grid(row=5,column=1,padx=2,pady=5)

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


def cont():
    global ans
    ans = askyesno(title = "Confirmation",message = "Do you want to change?")  
    if ans : 
        pass
        
    else :
        global im,new,label,im_g,img
        im_resize = im.resize((1200,780))
        img = ImageTk.PhotoImage(im_resize) 
        label.configure(image=img)
        cont_scale.set("0")


def cont_scale(self):
    global cont_scale,b,img,im_g,new,label
    b = cont_scale.get()
    filter = ImageEnhance.Contrast(im)
    img = filter.enhance(b)
    im_g = img.resize((1200,780))
    new = ImageTk.PhotoImage(im_g)
    label.configure(image=new)


cont_scale = Scale(my_canvas, from_= -100 , to=100, orient = 'horizontal',bg="yellow",fg="black",command=cont_scale)
cont_scale.grid(row=6,column=1,padx=2,pady=5)


# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------


def Expo_in(event):
  global im,new,label,im_g,img
  global a
  a = satu_scale.get()
  filter = ImageEnhance.Brightness(im)
  img = filter.enhance(a)
  im_g = img.resize((1200,780))
  new = ImageTk.PhotoImage(im_g)
  label.configure(image=new)

def expo():
    global ans
    ans = askyesno(title = "Confirmation",message = "Do you want to change?")  
    
    if ans : 
        pass
       
    else :
        # satu_scale.set("0")
        global im,new,label,im_g,img
        im_resize = im.resize((1200,780))
        img = ImageTk.PhotoImage(im_resize) 
        label.configure(image=img)
        
    
expo_scale = Scale(my_canvas, from_= 2 , to= 100, orient = 'horizontal',bg="yellow",fg="black",command = Expo_in)
expo_scale.set("2")
expo_scale.grid(row=7,column=1,padx=2,pady=5)

# -----------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------



save = Button(root,text="Save" , bg = "white")
save.grid(row=0,column=0,padx=2,pady=2,ipadx=10)


open = Button(root,text="Open" , bg = "white",command=open)
open.grid(row=0,column=1,padx=2,pady=2,ipadx=10)

#helllo hhhh

buttons(my_canvas,crop,select_crop,flip_hori,flip_vert,BnW,Saturation,sharp,cont,expo)



img = PhotoImage(file="abcd.png",width=1300,height=900)
my_image = my_canvas1.create_image(200,200 , anchor = NW , image = img)




root.mainloop()