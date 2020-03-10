from tkinter import *
from tkinter.ttk import *


def say_hello():
    """ """
    global name_entry, end_label
    
    name = name_entry.get()
    
    end_label['text'] = ("Hi {}".format(name))


def main():
    """ """
    global name_entry, end_label
    window = Tk()
    prompt_label = Label(window, text="Enter a name below")
    prompt_label.grid(row=0, column=0)
    name_entry = Entry(window)
    name_entry.grid(row=1, column=0)
    button = Button(window, text="Say hello", command=say_hello, padding=10)
    button.grid(row=2, column=1, columnspan=2)
    end_label = Label(window, text="")
    end_label.grid(row=3, column=1)
    window.mainloop()
    
main()
    