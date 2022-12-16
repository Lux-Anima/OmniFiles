from tkinter import *
import mysql.connector as conn
import sys
from tkinter import messagebox
from passlib.hash import pbkdf2_sha256
import os
import runpy

mydb = conn.connect(host='localhost',user = 'Omni',password='Omni123')
mycursor = mydb.cursor(buffered = True)

    
def deluser():
    result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
    if result == 'yes':
        user = entry0.get()
        passwd = entry1.get()
        mycursor.execute('use omni')
        query = 'select * from otable where username = %s'
        mycursor.execute(query, [(user)])
        result = mycursor.fetchone()
        if result:
            query = 'select * from otable where username = %s'
            mycursor.execute(query, [(user)])
            result = mycursor.fetchone()
            verifp = result[1]
            che = pbkdf2_sha256.verify(passwd,verifp)

            
            if che:
                print('sucess')
                mycursor.execute('delete from otable where username = %s',[(user)])
                mydb.commit()
                mydb.close()
                messagebox.showinfo('','Successfully deleted')
                dirname = os.getcwd()
                filen = dirname.rstrip('/DeleteUser')
                filename = filen + '/login.py'
                top.destroy()
                window.destroy()
                os.chdir(filen)
                runpy.run_path(path_name = filename)
                sys.exit()
            else:
                messagebox.showinfo('','Incorrect password')
        else:
            messagebox.showinfo('','There is no such username')
                
            
            
        
        
    
    


window = Tk()
top= Toplevel()
top.iconbitmap("realomnilogo.ico")
top.resizable(False,False)
top.title('Omni Files')
def de():
    top.destroy()
    window.destroy()
    sys.exit()

    
top.protocol('WM_DELETE_WINDOW',de)

top.geometry("1012x506")
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

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    498.5, 270.5,
    image=background_img)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(top,
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = deluser,
    relief = "flat")

b0.place(
    x = 591, y = 403,
    width = 190,
    height = 48)

window.withdraw()
window.resizable(False, False)
window.mainloop()
