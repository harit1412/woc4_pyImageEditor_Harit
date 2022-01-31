from tkinter import *
class buttons :
    def __init__(self,my_canvas,crop,select_crop,flip_hori,flip_vert,BnW,Saturation,sharp,cont,expo,highlight):
      self.BW = Button(my_canvas, text="Conver to Black & White", bg = "yellow", fg = "black",command = BnW)
      self.BW.grid(row=0, column=0,padx=2,pady=5)
      ##
      
      self.crop = Button(my_canvas, text="Apply Crop",bg="yellow",fg="black",command = crop) 
      self.select_crop = Button(my_canvas, text="Selct Area",bg="yellow",fg="black",command = select_crop)
      
      self.crop.grid(row=1,column=0,padx=2,pady=5)
      self.select_crop.grid(row=1,column=1,padx=2,pady=5)
      ##
      self.flip_hori = Button(my_canvas, text="Flip Horizantal",bg="yellow",fg="black",command = flip_hori)
      self.flip_vert = Button(my_canvas, text="Flip Vertically",bg="yellow",fg="black",command = flip_vert)
      
      self.flip_hori.grid(row=2,column=0,padx=2,pady=5)
      self.flip_vert.grid(row=3,column=0,padx=2,pady=5)
      ##
      
      # global a
      self.satu = Button(my_canvas, text="Apply Saturation",bg="yellow",fg="black",command =Saturation )
      # self.satu_in = Scale(my_canvas, from_= -100 , to=100, orient = 'horizontal',bg="yellow",fg="black",command = Saturation)
      # self.a = self.satu_in.get() 

      self.satu.grid(row=4,column=0,padx=2,pady=5)
      # self.satu_in.grid(row=4,column=1,padx=2,pady=5)
      ##
      
      self.sharp = Button(my_canvas, text="Apply Sharpness",bg="yellow",fg="black",command=sharp)
      # self.sharp_in = Scale(my_canvas, from_= 0 , to=100, orient = 'horizontal',bg="yellow",fg="black")
      
      
      self.sharp.grid(row=5,column=0,padx=2,pady=5)
      # self.sharp_in.grid(row=5,column=1,padx=2,pady=5)
      ##
      
      self.cont = Button(my_canvas, text="Apply Contrast",bg="yellow",fg="black",command= cont)
      # self.cont_in = Scale(my_canvas, from_= 0 , to=100, orient = 'horizontal',bg="yellow",fg="black")
      # self.cont_in.get()
      
      
      self.cont.grid(row=6,column=0,padx=2,pady=5)
      # self.cont_in.grid(row=6,column=1,padx=2,pady=5)
      ##
      
      self.expo = Button(my_canvas, text="Apply Exposure",bg="yellow",fg="black",command= expo)
      # self.expo_in = Scale(my_canvas, from_= 0 , to=100, orient = 'horizontal',bg="yellow",fg="black")
      
      
      self.expo.grid(row=7,column=0,padx=2,pady=5)
      # self.expo_in.grid(row=7,column=1,padx=2,pady=5)
      
      self.highlight = Button(my_canvas, text="Highlight Border",bg="yellow",fg="black",command= highlight)
      self.highlight.grid(row=8,column=0,padx=2,pady=5)
      
      
      self.text = Entry(my_canvas,width=35)
      self.text.grid(row=9,column=0)
      
      ##
      self.insert_text = Button(my_canvas, text="Insert Text",bg="yellow",fg="black")
      self.insert_text.grid(row=10,column=0)
      ##
      
      self.fix_text = Button(my_canvas, text="Fix Poaition",bg="yellow",fg="black")
      self.fix_text.place(x= 144 , y= 407) 

     
      
