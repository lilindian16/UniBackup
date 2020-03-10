from tkinter import *
from tkinter.ttk import *


def say_hello():
    global message_label, click_count
    
    click_count += 1
    if click_count >= 1:
        message_label['text'] = "Hello"
        
def say_goodbye():
    """
    """
    global click_count, message_label
    click_count += 1
    if click_count >= 1:
        message_label['text'] = "Goodbye!"

def main():
    """docstring"""
    
    global message_label, click_count
    
    click_count = 0
    
    window = Tk()
    message_label = Label(window, text="Click a button!")
    message_label.grid(row=0, column=0)
    hello_button = Button(window, text="Say hello", command=say_hello)
    hello_button.grid(row=1, column=0)
    goodbye_button = Button(window, text="Say goodbye", command=say_goodbye)
    goodbye_button.grid(row=1, column=1)
    window.mainloop()
    
main()
