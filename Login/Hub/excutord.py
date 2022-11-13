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
    
    print(str(pos))
    entry2.configure(state= NORMAL)
    entry2.insert(1.0,str(pos))
    entry2.configure(state= DISABLED)
    
def searchh(entrym0):
    global delf
    delf=[]
    path = entrym0.get().lstrip('Directory: ')
    print(path)
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
           print(i)
           send2trash(i)
        print ("Deleted")
    else:
        print ("I'm Not Deleted Yet")
    
   
def encr():
    key = Fernet.generate_key()
    print(key)
    print(delf)
    for i in delf:
        if '.txt' in i:

         with open(path2 + 'TheOneKey.dat','wb') as l:
             pickle.dump(key,l)
         with open(i,'rb+') as f:
            x = f.read()            
            e = Fernet(key)
            edat = e.encrypt(x)
            f.seek(0)
            f.write(edat)
            
        elif '.doc' or '.docx' in i:
            pass
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
def decr():
    with open(path2 + 'TheOneKey.dat','rb') as l:
           key = pickle.load(l)
           print(key)
    for i in delf:
        if '.txt' in i:
         with open(i,'r+') as f:
            x = f.read()
            print(x)
            
            e = Fernet(key)
            edat = e.decrypt(x)
            f.seek(0)
            f.truncate()
            f.write(edat)
        elif '.doc' or '.docx' in i:
            pass
def group(entry3):
    name = entry3.get()
    x = os.getlogin()
    dest = 'C:\\Users\\' + x + '\\OmniGroups' + '\\'+name
    os.makedirs(dest)
    for i in delf:
        shutil.copy2(i, dest)
      




    


    
    




