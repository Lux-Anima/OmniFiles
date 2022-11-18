from tkinter import *
import runpy
import os
from excutord import *
import sys

def btn_clicked():
    print("Button Clicked")

def switchgroup():
    canvas.coords(r1,0, 183, 0+7, 183+47)
    fmanage.place_forget()
    fsetting.place_forget()
    fframe.place_forget()
    fgroup.place(x=215, y = 38,width=797,height=432)
    
def switchmanage():
    canvas.coords(r1,0, 233, 0+7, 233+47)
    fgroup.place_forget()
    fsetting.place_forget()
    fframe.place_forget()
    fmanage.place(x=215, y = 38,width=797,height=432)
    
def switchsetting():
    canvas.coords(r1,0, 283, 0+7, 283+47)
    fmanage.place_forget()
    fgroup.place_forget()
    fframe.place_forget()
    fsetting.place(x=215, y = 38,width=797,height=432)
    
def switchabout():
    fmanage.place_forget()
    fsetting.place_forget()
    fgroup.place_forget()
    canvas.coords(r1,0, 333, 0+7, 333+47)
    fframe.place(x=215, y = 38,width=797,height=432)
    
    
    
    

    
window = Tk()
top = Toplevel()
def de():
    top.destroy()
    window.destroy()
    sys.exit()

    
top.protocol('WM_DELETE_WINDOW',de)

top.geometry("1012x506")
top.configure(bg = "#000000")
#----------------------------------HUB START------------------------------------
canvas = Canvas(
    top,
    bg = "#000000",
    height = 506,
    width = 1012,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)


canvas.create_rectangle(
    215, 0, 215+797, 0+506,
    fill = "#ffffff",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(top,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 7, y = 133,
    width = 208,
    height = 47)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(top,
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = switchgroup,
    relief = "flat")

b1.place(
    x = 7, y = 183,
    width = 208,
    height = 47)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(top,
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = switchsetting,
    relief = "flat")

b2.place(
    x = 7, y = 283,
    width = 208,
    height = 47)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(top,
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = switchabout,
    relief = "flat")

b3.place(
    x = 7, y = 333,
    width = 208,
    height = 47)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(top,
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: logout(top,window),
    relief = "flat")

b4.place(
    x = 0, y = 441,
    width = 215,
    height = 47)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(top,
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = switchmanage,
    relief = "flat")

b5.place(
    x = 7, y = 233,
    width = 208,
    height = 47)


r1 = canvas.create_rectangle(
    0, 133, 0+7, 133+47,
    fill = "#3afdfc",
    outline = "")

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    479.5, 49.0,
    image=background_img)

#---------------------------------------------HUB END-----------------------------

#fdashboard = Frame(window)
fgroup = Frame(top,bg = "#ffffff")
fmanage = Frame(top,bg = "#ffffff")
fsetting = Frame(top,bg ='#ffffff')
fframe = Frame(top,bg ='#ffffff')


# GROUP FRAME -------------------------------------------------
canvasg = Canvas(
    fgroup,
    bg = "#ffffff",
    height = 432,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvasg.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvasg.create_image(
    141.5, 276.0,
    image = entry0_img)

entry0 = Entry(fgroup,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry0.place(
    x = 52, y = 264,
    width = 179,
    height = 22)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvasg.create_image(
    154.5, 171.5,
    image = entry1_img)

entry1 = Entry(fgroup,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry1.place(
    x = 43, y = 163,
    width = 223,
    height = 15)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvasg.create_image(
    549.5, 152.0,
    image = entry2_img)

entry2 = Text(fgroup,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry2.place(
    x = 323, y = 104,
    width = 453,
    height = 94)

entry3_img = PhotoImage(file = f"img_textBox3.png")
entry3_bg = canvasg.create_image(
    493.0, 276.0,
    image = entry3_img)

entry3 = Entry(fgroup,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry3.place(
    x = 352, y = 264,
    width = 282,
    height = 22)

imgg0 = PhotoImage(file = f"simg.png")
bg0 = Button(fgroup,
    image = imgg0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: UniSearch(entry2,entry0),
    relief = "flat")

bg0.place(
    x = 32, y = 325,
    width = 190,
    height = 48)

imgg1 = PhotoImage(file = f"sfimg.png")
bg1 = Button(fgroup,
    image = imgg1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: browseFiles(entry1),
    relief = "flat")

bg1.place(
    x = 41, y = 68,
    width = 190,
    height = 48)
 
imgg2 = PhotoImage(file = f"cimg.png")
bg2 = Button(fgroup,
    image = imgg2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: group(entry3),
    relief = "flat")

bg2.place(
    x = 366, y = 325,
    width = 190,
    height = 48)

background_imgg = PhotoImage(file = f"backgroundg.png")
background = canvasg.create_image(
    403.5, 199.5,
    image=background_imgg)
    

#-----------------------------FRAME GROUP END ---------------------------

#---------------------------------FRAME MANAGE-----------------------------
canvasm = Canvas(
    fmanage,
    bg = "#ffffff",
    height = 432,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvasm.place(x = 0, y = 0)

background_imgm = PhotoImage(file = f"backgroundm.png")
backgroundm = canvasm.create_image(
    288, 165.5,
    image=background_imgm)

entrym0_img = PhotoImage(file = f"textboxm.png")
entrym0_bg = canvasm.create_image(
    211.5, 290.0,
    image = entrym0_img)

entrym0 = Entry(fmanage,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entrym0.place(
    x = 122, y = 278,
    width = 179,
    height = 22)

imgm0 = PhotoImage(file = f"sgimg.png")
bm0 = Button(fmanage,
    image = imgm0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: browseFiles(entrym0),
    relief = "flat")

bm0.place(
    x = 112, y = 128,
    width = 190,
    height = 48)


canvasm.create_rectangle(
    417, 59, 417+2, 59+311,
    fill = "#efefef",
    outline = "")

imgm1 = PhotoImage(file = f"encrypt.png")
bm1 = Button(fmanage,
    image = imgm1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: encr(entrym0),
    relief = "flat")

bm1.place(
    x = 482, y = 98,
    width = 209,
    height = 74)

imgm2 = PhotoImage(file = f"decrypt.png")
bm2 = Button(fmanage,
    image = imgm2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: decr(entrym0),
    relief = "flat")

bm2.place(
    x = 482, y = 193,
    width = 209,
    height = 74)

imgm3 = PhotoImage(file = f"delete.png")
bm3 = Button(fmanage,
    image = imgm3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: Delete(entrym0),
    relief = "flat")

bm3.place(
    x = 482, y = 296,
    width = 209,
    height = 74)

#----------------------------------FRAME MANAGE END-----------------------------

#-----------------------------------FRAME SETTING START--------------------------

canvass = Canvas(
    fsetting,
    bg = "#ffffff",
    height = 432,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvass.place(x = 0, y = 0)

imgs0 = PhotoImage(file = f"update.png")
bs0 = Button(fsetting,
    image = imgs0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bs0.place(
    x = 325, y = 353,
    width = 144,
    height = 48)

background_imgs = PhotoImage(file = f"sbackground.png")
background = canvass.create_image(
    413.5, 222.5,
    image=background_imgs)

imgs1 = PhotoImage(file = f"logout.png")
bs1 = Button(fsetting,
    image = imgs1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: logout(top,window),
    relief = "flat")

bs1.place(
    x = 303, y = 285,
    width = 190,
    height = 48)

imgs2 = PhotoImage(file = f"adduser.png")
bs2 = Button(fsetting,
    image = imgs2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: addusr(top,window),
    relief = "flat")

bs2.place(
    x = 303, y = 216,
    width = 190,
    height = 48)

imgs3 = PhotoImage(file = f"deleteu.png")
bs3 = Button(fsetting,
    image = imgs3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: delusr(top,window),
    relief = "flat")

bs3.place(
    x = 303, y = 148,
    width = 190,
    height = 48)

imgs4 = PhotoImage(file = f"cp.png")
bs4 = Button(fsetting,
    image = imgs4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bs4.place(
    x = 283, y = 80,
    width = 242,
    height = 48)

#----------------------------FRAME SETTING END------------------------------------

#----------------------------FRAME ABOUT------------------------------------------
canvasf = Canvas(
    fframe,
    bg = "#ffffff",
    height = 432,
    width = 797,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvasf.place(x = 0, y = 0)

background_imgf = PhotoImage(file = f"backgroundf.png")
backgroundf = canvasf.create_image(
    398.0, 207.5,
    image=background_imgf)

#-------------------------------FRAME ABOUT END-----------------------------------

fgroup.place(x=215, y = 38,width=797,height=432)

window.resizable(False, False)
window.withdraw()
window.mainloop()
