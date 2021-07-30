# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 13:35:29 2019

@author: fahim
"""

from tkinter import filedialog
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
#from tkinter import messagebox
def huadi():
    print("Hudai")

def create_window():
    window = tk.Toplevel(root)

def client_exit():
        root.destroy()
        
def importImages2():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        print(root.filename)
        image=Image.open(root.filename)
        try:
            image.verify()
            #image = image.resize((250, 250), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(image)
            panel = tk.Label(root, image = img)
            panel.image = img
            #panel.pack(side = "bottom", fill = "both", expand = "yes")
            panel.pack()
            button2 = tk.Button(root,text="Convert")
            #button2.bind("<Button-2>",convertImg)
            button2.pack()
        except Exception:
            messagebox.showinfo("Error", "Not an image")
        
        
def importImages(event):
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("JEPG files","*.jpg"),("all files","*.*")))
        print(root.filename)
        image=Image.open(root.filename)
        image = image.resize((250, 250), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        panel = tk.Label(root, image = img)
        panel.image = img
#        panel.pack(side = "bottom", fill = "both", expand = "yes")
        panel.pack()
        button2 = tk.Button(root,text="Convert",bg="Red",command=huadi)
        #button2.bind("<Button-2>",convertImg)
        button2.pack()
         

    
        
root = tk.Tk()
root.title("Detection")
root.geometry("800x500")
root.configure(background='Azure')
########---------------------Manu bar-------------------######################

menu = Menu(root)
root.config(menu=menu)


######################################################
subMenu=Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Seasion..",command=create_window)
subMenu.add_command(label="Open",command=importImages2)
subMenu.add_command(label="Save..",command=huadi)
subMenu.add_command(label="Save as..",command=huadi)
subMenu.add_command(label="Exit",command=client_exit) 
##########################################################
editMenu=Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Copy",command=huadi)
editMenu.add_command(label="Paste",command=huadi)
editMenu.add_command(label="Undo",command=huadi)
editMenu.add_command(label="Redo",command=huadi)
############################################
helpMenu=Menu(menu)
menu.add_cascade(label="Help", menu=helpMenu)
helpMenu.add_command(label="About",command=huadi)

############################################################################################################

topframe =tk.Frame(root,bg="Azure")
topframe.pack()

bottomframe = tk.Frame(root)
bottomframe.pack(side=tk.BOTTOM)

label1 = tk.Label(topframe,text="Please select an image to convert(.jpg/.png)",bg='lavender',pady=10)
label1.config(font=("Courier", 15))
label1.pack()
#
#button1 = tk.Button(topframe,text="Import")
#button1.bind("<Button-1>",importImages)
#button1.pack()

button = Button(root, text="Click me!",pady=10)
img = PhotoImage(file="E:/import_test.png") # make sure to add "/" not "\"
button.config(image=img)
button.bind("<Button-1>",importImages)
button.pack() # Displaying the button


label2 = tk.Label(root,text="Preview",bg='lavender',pady=10)
label2.config(font=("Courier", 15))
label2.pack()


root.mainloop()