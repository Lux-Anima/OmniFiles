import runpy
import os
import shutil
from sys import exit
import pickle
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import docx2txt
import textract
from cryptography.fernet import Fernet
import concurrent.futures
from send2trash import send2trash
import threading
import mysql.connector as conn

    
delf =[]
def UniSearch(entry2,entry0):
    #text_box.delete("1.0","end")
    pos = []
    global delf
    delf=[]
    #searc = input("Enter search term")
    for (root,dirs, files) in os.walk(path):
        check = entry0.get()
        for f in files:
            if '.txt' in f:
                with open(os.path.join(root, f),errors ='ignore') as fil:
                    s = fil.read()
                if check in s:
                    pos.append(f)
                    delf.append(os.path.join(root, f))
            elif '.docx' in f:
                try:
                    
                    s = textract.process(os.path.join(root, f))
                    s = s.decode("utf-8")

                    if check in s:
                        pos.append(f)
                        delf.append(os.path.join(root, f))
                        
                        
                except:
                    continue
    
    entry2.configure(state= NORMAL)
    entry2.insert(1.0,str(pos))
    entry2.configure(state= DISABLED)
    
def searchh(entrym0):
    global delf
    delf=[]
    path = entrym0.get().lstrip('Directory: ')
    #searc = input("Enter search term")
    for (root,dirs, files) in os.walk(path):
        for f in files:
            delf.append(os.path.join(root, f))
    
def Delete(entrym0):
    searchh(entrym0)
    for i in delf:
        if os.path.isfile(i):            
           deleteme()
        else:    ## Show an error ##
             pass
def deleteme():
    result = messagebox.askquestion("Delete", "Are You Sure?", icon='warning')
    if result == 'yes':
        for i in delf:
           i = i.replace('/','\\')
           send2trash(i)
        print ("Deleted")
    else:
        print ("I'm Not Deleted Yet")
    
   
def encr(entrym0):
    delf = []
    result = messagebox.askquestion('Choice','Use already existing key?')
    if result == 'yes':
        messagebox.showinfo('Info','Choose the location of the key')
        x = filedialog.askopenfile()
        pat = entrym0.get()
        path = pat.lstrip('Directory: ')
        kname = path.split('/')[-2]
        keyloc = os.path.abspath(x.name)
        with open(keyloc ,'rb') as l:
            key = pickle.load(l)
        for (root,dirs, files) in os.walk(path):
            for f in files:
                delf.append(os.path.join(root, f))
        for i in delf:
            with open(i,'rb+') as f:
                    x = f.read()
                    e = Fernet(key)
                    edat = e.encrypt(x)
                    f.seek(0)
                    f.write(edat)
            
    else:
          delf  = []
          key = Fernet.generate_key()
          messagebox.showinfo('Info','Choose location to store new key')
          keyloc = filedialog.askdirectory()
          pat = entrym0.get()
          path = pat.lstrip('Directory: ')
          kname = path.split('/')[-1]
          with open(keyloc +'/' + kname + '.dat','wb') as l:
              pickle.dump(key,l)
          
          for (root,dirs, files) in os.walk(path):
              for f in files:
                  delf.append(os.path.join(root, f))
          for i in delf:
              with open(i,'rb+') as f:
                      x = f.read()
                      e = Fernet(key)
                      edat = e.encrypt(x)
                      f.seek(0)
                      f.write(edat)
            
def decr(entrym0):
    delf  = []
    messagebox.showinfo('Info','Choose the location of the key')
    x = filedialog.askopenfile()
    keyloc = os.path.abspath(x.name)
    pat = entrym0.get()
    path = pat.lstrip('Directory: ')
    with open(keyloc ,'rb') as l:
        key = pickle.load(l)
    
    for (root,dirs, files) in os.walk(path):
        for f in files:
            delf.append(os.path.join(root, f))
    for i in delf:
        with open(i,'rb+') as f:
                x = f.read()
                e = Fernet(key)
                edat = e.decrypt(x)
                f.seek(0)
                f.truncate()
                f.write(edat)
                
def checking():
    try:
        file = open(r'F:\testing.txt')
        print("Found")
    except FileNotFoundError:
        print("Not Found!!")

def browseFiles(entry1):
    global path
    path = filedialog.askdirectory()
      
    # Change label contents
    entry1.configure(state= NORMAL)
    entry1.insert(0,"Directory: " +path)
    entry1.configure(state= DISABLED)
    
def browseFiles2():
       global path2
       path2 = filedialog.askdirectory()
         
       # Change label contents
       label_file_explorer2.configure(text="Directory: "+path2)  

def group(entry3):
    name = entry3.get()
    x = os.getlogin()
    dest = 'C:\\Users\\' + x + '\\OmniGroups' + '\\'+name
    os.makedirs(dest)
    for i in delf:
        shutil.copy2(i, dest)


def addusr(top,window):
    x = os.getcwd()
    path = x.rstrip('Hub')
    rpath = path + r'Register\register.py'
    top.destroy()
    window.destroy()
    os.chdir(path + r'Register')
    runpy.run_path(path_name = rpath)
    sys.exit()
    
    
def delusr(top,window):
    x = os.getcwd()
    path = x.rstrip('Hub')
    rpath = path + r'DeleteUser\deluser.py'
    top.destroy()
    window.destroy()
    os.chdir(path + r'DeleteUser')
    runpy.run_path(path_name = rpath)
    sys.exit()
    
def logout(top,window):
    dirname = os.getcwd()
    filen = dirname.rstrip('/Hub')
    filename = filen + '/login.py'
    top.destroy()
    window.destroy()
    os.chdir(filen)
    runpy.run_path(path_name = filename)
    sys.exit()





    


    
    




