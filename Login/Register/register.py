from tkinter import *
from tkinter import messagebox
import mysql.connector as conn
import runpy
import os
import sys
from passlib.hash import pbkdf2_sha256
mydb = conn.connect(host='localhost',user = 'root',password='Sample123')
mycursor = mydb.cursor(buffered = True)
mycursor.execute("CREATE DATABASE IF NOT EXISTS omni")

def btn_clicked():

    usrname = entry0.get()
    passwd = entry1.get()
    passwor = pbkdf2_sha256.hash(passwd)
    mycursor.execute('USE omni')
    mycursor.execute('CREATE TABLE IF NOT EXISTS otable(Username VARCHAR(40),Password VARCHAR(500))')
    mydb.commit()
    query = 'select * from otable where username = %s'
    mycursor.execute(query, [(usrname)])
    result = mycursor.fetchone()
    if result:
        messagebox.showinfo('','Username already taken!')
    else:
        if entry1.get() == entry2.get():
            mycursor.execute("INSERT INTO otable (Username,Password) VALUES (%s, %s)",(usrname,passwor))
            mydb.commit()
            mydb.close()
            dirname = os.getcwd()
            filen = dirname.rstrip('/Register')
            filename = filen + '/login.py'
            topr.destroy()
            windowr.destroy()
            os.chdir(filen)
            runpy.run_path(path_name = filename)
            sys.exit()
        else:
            messagebox.showinfo(
            title='Information',
            message='Passwords do not match!')
        
    
    


windowr = Tk()
topr = Toplevel()
def de():
    topr.destroy()
    windowr.destroy()
    sys.exit()

    
topr.protocol('WM_DELETE_WINDOW',de)

topr.geometry("1012x506")
topr.configure(bg = "#1c2433")
canvasr = Canvas(
    topr,
    bg = "#1c2433",
    height = 506,
    width = 1012,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvasr.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvasr.create_image(
    689.0, 184.0,
    image = entry0_img)

entry0 = Entry(topr,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry0.place(
    x = 526, y = 172,
    width = 326,
    height = 22)


entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvasr.create_image(
    689.0, 274.0,
    image = entry1_img)

entry1 = Entry(topr,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry1.place(
    x = 526, y = 262,
    width = 326,
    height = 22)

entry2_img = PhotoImage(file = f"img_textBox2.png")
entry2_bg = canvasr.create_image(
    689.0, 363.0,
    image = entry2_img)

entry2 = Entry(topr,
    bd = 0,
    bg = "#efefef",
    highlightthickness = 0)

entry2.place(
    x = 526, y = 351,
    width = 326,
    height = 22)

background_img = PhotoImage(file = f"background.png")
background = canvasr.create_image(
    498.5, 270.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(topr,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 591, y = 403,
    width = 190,
    height = 48)

windowr.resizable(False, False)
windowr.withdraw()
windowr.mainloop()
