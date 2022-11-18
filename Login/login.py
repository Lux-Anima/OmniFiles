from tkinter import *
import mysql.connector as conn
import runpy
import os
import sys
from tkinter import messagebox
from passlib.hash import pbkdf2_sha256
mydb = conn.connect(host='localhost',user = 'root',password='Sample123')
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES LIKE 'OMNI'")
result = mycursor.fetchall()
dirname = os.getcwd()
filename = dirname + '/Register/register.py'
if not result:
    os.chdir(dirname + '/Register')
    runpy.run_path(path_name = filename)
    sys.exit()
    
    

x = 0

def btn_clicked():
    uname = entry0.get()
    passwd = entry1.get()
    

    mycursor.execute('use omni')
    query = 'select * from otable where username = %s'
    mycursor.execute(query, [(uname)])
    result = mycursor.fetchone()
    try:
        verifp = result[1]
        che = pbkdf2_sha256.verify(passwd,verifp)
    except:
        che = 0

    
    if che:
        global x
        x = 1
        de()
        os.chdir(dirname + '/Hub')
        runpy.run_path(path_name = dirname + '/Hub/hub.py' )
        sys.exit()
    else:
        messagebox.showinfo('','Incorrect username or password')



window = Tk()
top = Toplevel()
def de():
    top.destroy()
    window.destroy()
    if x == 0:
        sys.exit()

    
top.protocol('WM_DELETE_WINDOW',de)


top.geometry("1012x506")
#windowf.config(height = 506,width = 1012)
#windowf.wm_attributes('-transparentcolor', '#ab23ff')
top.configure(bg = "#1c2433")
canvas = Canvas(
    top,
    bg = "#1c2433",
    height = 506,
    width = 1012,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    689.0, 240.0,
    image = entry0_img)

entry0 = Entry(top,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry0.place(
    x = 526, y = 228,
    width = 326,
    height = 22)

entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    689.0, 343.0,
    image = entry1_img)

entry1 = Entry(top,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry1.place(
    x = 526, y = 331,
    width = 326,
    height = 22)

entry1.config(show = '*')

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    498.5, 270.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(top,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 591, y = 403,
    width = 190,
    height = 48)

window.resizable(False, False)
window.withdraw()
window.mainloop()
