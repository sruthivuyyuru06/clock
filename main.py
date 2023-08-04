# Imprting Python Modules
from tkinter import *
from time import strftime           # used to display the operating system 

root=Tk()                           # creating a Tkinter window
root.title("Digital Clock")         # giving the title 

label=Label(root,font=("areal",160,"bold"),bg="black",fg="white") # styling the windows
label.pack(anchor="center",fill="both",expand=1)

# Creating a function to display time

def Time():
    string=strftime("%H:%M:%S ")

    label.config(text=string)

    label.after(1000, Time)

# calling the function and running it 
Time()
root.mainloop()