from tkinter import *
from PIL import Image,ImageTk
from buttons import buttons
import ctypes
ctypes.windll.shcore.SetProcessDpiAwareness(1000)

root = Tk()

my_canvas = Canvas(root, width=00,height=900 ,bg="skyblue")
my_canvas.place(x=0,y=30)

save = Button(root, text="Save",bg="lightgray",fg="black")    
open = Button(root , text="Open",bg="lightgray",fg="black")  

buttons(my_canvas)




root.mainloop()