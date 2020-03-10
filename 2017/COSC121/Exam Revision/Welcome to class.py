from tkinter import *
from tkinter.ttk import *

def main():
    """docstring"""
    window = Tk()
    label = Label(window, text="COSC121")
    label.grid(row=0, column=0)
    window.mainloop()
    
main()