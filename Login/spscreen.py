from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time
import runpy

w=Tk()

width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
w.overrideredirect(1) 

faketext = ['Launching Omni Files..','Connecting to Omni Database..','Loading assets..','Building app..']

#new window to open
def new_win():
    runpy.run_path(path_name = 'login.py')
c = 0
def fakeupd():
    global c
    label2["text"] = faketext[c]

image_a=ImageTk.PhotoImage(Image.open('c2.png'))
image_b=ImageTk.PhotoImage(Image.open('c1.png'))
   
def change(x = image_b, y = image_b, z = image_b, a = image_b):
    fakeupd()
    l1=Label(w, image=x, border=0, relief=SUNKEN).place(x=180, y=145)
    l2=Label(w, image=y, border=0, relief=SUNKEN).place(x=200, y=145)
    l3=Label(w, image=z, border=0, relief=SUNKEN).place(x=220, y=145)
    l4=Label(w, image=a, border=0, relief=SUNKEN).place(x=240, y=145)
    w.update()
    
    

Frame(w, width=427, height=250, bg='#1D2E37').place(x=0,y=0)
label1=Label(w, text='OMNI FILES',  bg='#1D2E37',fg = '#3AFDFC') 
label1.configure(font=("Game Of Squids", 24, "bold"))
label1.place(x=120,y=90)

label2=Label(w, text='Loading...', fg='#3AFDFC', bg='#1D2E37') #decorate it 
label2.configure(font=("Calibri", 11))
label2.place(x=10,y=215)







for i in range(4):
    change(x = image_a)
    time.sleep(0.6)

    change(y = image_a)
    time.sleep(0.6)

    change(z = image_a)
    time.sleep(0.6)

    change(a = image_a)
    time.sleep(0.6)
    c += 1



w.destroy()
new_win()
w.mainloop()