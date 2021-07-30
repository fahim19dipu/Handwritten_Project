# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 10:35:19 2019

@author: fahim
"""
from tkinter import filedialog
from tkinter import *
from tkinter import ttk

def importImages2():
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("png files","*.png"),("all files","*.*")))
        print(root.filename)

def startTrain():
    print("sadas") 
def stopTrain():
    print("sadas")
root =Tk() 
root.title("Train")
root.geometry("800x500")
root.configure(background='Azure')


label1= Label(root,text="Hidden layers of the Nural network:",bg='lavender')
entry_1 =Entry(root)

label2= Label(root,text="Number of nurons in each hidden layer:",bg='lavender')
entry_2=Entry(root)

label3= Label(root,text="Select the Train dataset :",bg='lavender')

browse_button=Button(root,text="Browse",command=importImages2)

start_button=Button(root,command=startTrain)
imgw = PhotoImage(file="E:/start.png") # make sure to add "/" not "\"
start_button.config(image=imgw)

stop_button=Button(root,text="Stop",command=stopTrain)
img = PhotoImage(file="E:/stop.png") # make sure to add "/" not "\"
stop_button.config(image=img)

label1.grid(row=0,sticky=W)
entry_1.grid(row=0,column=2,sticky=W)

label2.grid(row=1,sticky=W)
entry_2.grid(row=1,column=2,sticky=W)

label3.grid(row=2,sticky=W)
browse_button.grid(row=2,column=2,sticky=W)

start_button.grid(row=4,column=0,sticky=W,pady=20)
stop_button.grid(row=5,column=2,sticky=E)


progressBar =ttk.Progressbar(orient="horizontal",length=286,mode="determinate")
progressBar.grid(column=0,row=5,pady=10)

root.grid_columnconfigure(4, minsize=10000)
root.mainloop()