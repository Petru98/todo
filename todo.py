#!/usr/bin/python3
import time
import datetime
import tkinter as tk
import tkinter.ttk as ttk



class TodoElement:
    def __init__(self, description = "", expiration_date = datetime.datetime.now(datetime.timezone.utc)):
        self.description = description
        self.checked = False
        self.expiration_date = expiration_date



class TodoList:
    def __init__(self):
        self.elements = []

    def add(self, element):
        self.elements.append(element)

    def sort(self, attr):
        self.elements.sort(attrgetter(attr))



class TextBox(object):
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure(0, weight = 1)
        self.frame.grid_columnconfigure(0, weight = 1)

        self.view = ttk.Treeview(columns=['Description', '', ''], show="headings")
        self.view.grid(row = 0, column = 0, sticky = "nsew")

        self.xscroll = tk.Scrollbar(self.frame, orient = tk.HORIZONTAL, command = self.view.xview)
        self.xscroll.grid(row = 1, column = 0, sticky = "nsew")

        self.yscroll = tk.Scrollbar(self.frame, orient = tk.VERTICAL, command = self.view.yview)
        self.yscroll.grid(row = 0, column = 1, sticky = "nsew")

        self.view.config(xscrollcommand = self.xscroll.set)
        self.view.config(yscrollcommand = self.yscroll.set)



class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Todo")
        self.root.geometry("768x480")

        self.root.grid_rowconfigure(0, weight = 1)
        self.root.grid_rowconfigure(1, weight = 0)
        self.root.grid_columnconfigure(0, weight = 0)
        self.root.grid_columnconfigure(1, weight = 1)

        self.textbox = TextBox(self.root)
        self.textbox.frame.grid(row = 0, column = 0, sticky = "nsew", padx = 0, pady = 0, columnspan = 3)

        self.password_label = tk.Label(self.root, text = "Password: ", justify = tk.CENTER)
        self.password_label.grid(row = 1, column = 0, sticky = "nsw", padx = 8, pady = 8)

        self.keybox = tk.Entry(self.root, width = 32, show = '*', bd = 2)
        self.keybox.grid(row = 1, column = 1, sticky = "nsw", padx = 8, pady = 8)


    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    App().run()
