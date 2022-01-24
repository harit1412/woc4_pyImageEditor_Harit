from asyncio.windows_events import NULL
from tkinter import *
from PIL import Image,ImageTk
# from tkinter import Image
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from buttons import buttons
from tkinter.filedialog import askopenfile
import ctypes

ctypes.windll.shcore.SetProcessDpiAwareness(1000)

root = Tk()
root.geometry("1000x1000")


my_canvas1 = Canvas(root,width=1300,height=900, bg="lightgray")
my_canvas1.place(x=320,y=30)


# img =Label(image=img).place(x=400,y=150)
# my_canvas1.create_image(300,300,image = img)

# # img = NULL
# # im = NULL
# def open():
#     global img
#     global im
#     my_canvas1.img_name = filedialog.askopenfilename(title="Select Image",filetypes=(("png files","*.png"),("jpg files","*.jpg")))
#     im = Image.open(my_canvas1.img_name)

    
def open():
    global img
    global label
    global im_resize
    my_canvas1.img_name = filedialog.askopenfilename(title="Select Image",filetypes=(("png files","*.png"),("jpg files","*.jpg")))
    im = Image.open(my_canvas1.img_name)
    im_resize = im.resize((900,800))
    img = ImageTk.PhotoImage(im_resize) 
    label = Label(my_canvas1,image=img).place(x=200,y=70)
    label.resize(width=1600 , hieght = 800)



  



my_canvas = Canvas(root, width=00,height=900 ,bg="white")
my_canvas.place(x=0,y=30)

save = Button(root,text="Save" , bg = "white")
save.grid(row=0,column=0,padx=2,pady=2,ipadx=10)


open = Button(root,text="Open" , bg = "white",command=open)
open.grid(row=0,column=1,padx=2,pady=2,ipadx=10)
buttons(my_canvas)

#helllo hhhh


img = PhotoImage(file="abcd.png",width=1300,height=900)
my_image = my_canvas1.create_image(200,200 , anchor = NW , image = img)



root.mainloop()