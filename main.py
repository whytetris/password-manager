from tkinter import *
from tkinter.ttk import Combobox
from tkinter.ttk import Checkbutton
from tkinter import Menu
from tkinter import messagebox
from tkinter import scrolledtext
import random
import sqlite3
import base64
import os


# Create, random, Copy, remove, db, password and encryption

key = ''

class Test():
    def __init__(self):
        self.window =Tk()
        self.window.geometry('300x200')

        text = Label(self.window, text="Entry KEY", font=("Arial Bold", 15))
        text.pack(anchor=CENTER,pady=10)

        text_input = Entry(self.window,font=("Arial Bold", 25), show='#')
        text_input.pack(fill=X,anchor=CENTER,pady=10)

        button = Button(self.window, text='ENTER', font=("Arial Bold", 15), command=lambda : self.quit(text_input.get()))
        button.pack(fill=X,anchor=CENTER,pady=10)
        self.window.mainloop()

    def quit(self,key):
        self.window.destroy()
        self.main_menu(key)

    def main_menu(self,key):
        self.window =Tk()
        self.window.geometry('300x300')

        status_label = Label(self.window, text="KEY: "+key, font=("Arial Bold",15))
        status_label.pack(anchor=CENTER, pady=10)

        text = Label(self.window, text="Select service", font=("Arial Bold", 15))
        text.pack(anchor=CENTER,pady=10)

        list_pas = Combobox(self.window)
        list_pas = Combobox(self.window, values=["VK","YouTube"], font=("Arial Bold",15),state="readonly")
        list_pas.pack(anchor=CENTER, pady=10, fill=X)

        button_copy = Button(self.window, text='COPY', font=("Arial Bold", 15), command=lambda : test(key))
        button_copy.pack(fill=X,anchor=CENTER, pady=5)


        button_copy = Button(self.window, text='Create NEW', font=("Arial Bold", 15), command=lambda : test(key))
        button_copy.pack(fill=X,anchor=CENTER, pady=5)

        button_remove = Button(self.window, text='Remove this', font=("Arial Bold", 15), command=lambda : test(key))
        button_remove.pack(fill=X,anchor=CENTER, pady=5)

        self.window.mainloop()

def test(key):
    print(key)



app = Test()