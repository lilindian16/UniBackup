from tkinter import *
from tkinter.ttk import *

def main():
    window = Tk()       #Creates a 'root' window on screen
    label = Label(window, text='This is my own label please go away!') # Make a label (text)
    label.grid(row=0, column=0) # Put label at a grid location (0, 0)
    print("Nearly running")
    window.mainloop() # Enter the GUI main loop, exists when window is closed
    print("Done")
    
main()