from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import clipboard
import validators
from pyshorteners import Shortener

def Clear():
    e.delete(0,"end")
    l.config(text="")

def Copy():
    clipboard.copy(l.cget("text"))
    c = Label(win,text="Successfully Copied",bg="green", font=(20))
    c.pack()
    win.after(2000, c.destroy)

def Paste():
    e.delete(0,"end")
    e.insert(0,clipboard.paste())

def Shorten():
    link = e.get()
    valid = validators.url("" + link)
    if (valid == True):
        short = Shortener().tinyurl.short(link)
        l.config(text=short)
    else:
        l.config(text="Invalid URL Or Address")



win = Tk()
win.title("URL Shortner")
win.geometry("780x300")

e = Entry(win, font=(20))
e.place(relwidth=0.6,relx=0.2,rely=0.2)

paste = Image.open("paste.png")
resized_paste = paste.resize((20,20),Image.ANTIALIAS)
new_paste =ImageTk.PhotoImage(resized_paste)

paste_b = Button(win,image=new_paste,command=Paste)
paste_b.place(relx=0.16,rely=0.2)

shorten_b = Button(win,text="Short_URl",command=Shorten)
shorten_b.place(relx=0.4,rely=0.37)

clear_b = Button(win,text="Clear Text",command=Clear)
clear_b.place(relx=0.55,rely=0.37)

l = Label(win,bg="white",font=(20),relief="sunken")
l.place(relwidth=0.6, relx=0.2,rely=0.7)

copy = Image.open("copy.png")
resized_copy = copy.resize((20,20),Image.ANTIALIAS)
new_copy =ImageTk.PhotoImage(resized_copy)

copy_b = Button(win,image=new_copy,command=Copy)
copy_b.place(relx=0.16,rely=0.7)

win.mainloop()