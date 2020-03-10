from tkinter import *
from tkinter.ttk import *



def add_one():
    """
    """
    global label, current_count
    
    current_count += 1
    label['text'] = str(current_count)


def minus_one():
    """
    """
    global label, current_count
    
    current_count -= 1
    label['text'] = str(current_count)    


def main():
    """
    """
    global label, current_count, click_count
    
    click_count = 0    
    current_count = 0
    
    window = Tk()
    label = Label(window, text='0')
    label.grid(row=0, column=0)
    add_button = Button(window, text="+1", command=add_one)
    add_button.grid(row=1, column=0)
    minus_button = Button(window, text="-1", command=minus_one)
    minus_button.grid(row=1, column=1)
    
    window.mainloop()
    
main()
