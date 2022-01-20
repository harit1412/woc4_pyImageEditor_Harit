from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1000)
root = Tk()

img = ImageTk.PhotoImage(Image.open("F:\pyimage\woc4_pyImageEditor_Harit\default.jpg"))
lab_img = Label(image = img)
lab_img.place(x=1,y=25)




root.geometry("500x500")

root.title("Image Editor")
root.iconbitmap('F:\pyimage\woc4_pyImageEditor_Harit\pyimage.ico')

save = Button(root, text="Save",bg="lightgray",fg="black")    
open = Button(root, text="Open",bg="lightgray",fg="black")      
BW = Button(root, text="Conver to Black & White",bg="lightgray",fg="black")
crop = Button(root, text="Apply Crop",bg="lightgray",fg="black") 
select_crop = Button(root, text="Apply Crop",bg="lightgray",fg="black")
flip_hori = Button(root, text="Flip Horizantal",bg="lightgray",fg="black")
flip_vert = Button(root, text="Flip Vertically",bg="lightgray",fg="black")
satu = Button(root, text="Apply Saturation",bg="lightgray",fg="black")
satu_in = ttk.Scale(root, from_= 0 , to=100, orient = 'horizontal')


save.grid(row=0, column=0 , padx = 3 , pady= 3)
open.grid(row=0, column=1 , padx=3 , pady=3)
# BW.grid(row=0, column=2 , padx=3 , pady=3 )
BW.place(x=1300,y=100)
crop.place(x=1400,y=200)
select_crop.place(x=1270,y=200)
flip_hori.place(x=1270,y=300)
flip_vert.place(x=1400,y=300)
satu.place(x=1400,y=400)
satu_in.place(x=1270,y=400)
root.mainloop()