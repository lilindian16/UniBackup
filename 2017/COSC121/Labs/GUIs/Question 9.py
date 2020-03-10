"""An exercise in improving layout"""
from tkinter import *
from tkinter.ttk import *

def calculate():
    """Calculate twice the number and set that answer into result"""
    global entry, result_label
    result_label['text'] = 2 * int(entry.get())

def main():
    """Every home should have one"""
    global entry, result_label
    window = Tk() 
    header = Label(window, text="Doubler", font=("Arial", 18))
    header.grid(row=0, column=0, columnspan=3, padx=(20, 0), pady=10)
    
    entry = Entry(window)
    entry.grid(row=1, column=0, padx=(20, 0), width=5, pady=10)
    times_2 = Label(window, text=" * 2 = ")
    times_2.grid(row=1, column=1)
    result_label = Label(window, text='0')
    result_label.grid(row=1, column=2, padx=(0,20), pady=10)
    button = Button(window, text="Calculate", command=calculate)
    button.grid(row=2, column=0, columnspan=3, pady=10)
    window.mainloop()

main()