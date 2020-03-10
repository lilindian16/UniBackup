
from tkinter import *
from tkinter.ttk import *

class CounterGui:
    """The GUI class"""

    def __init__(self, window):
        """Setup the label and button on given window"""

        self.count_label = Label(window, text='0')
        self.current_count = 0
        self.count_label.grid(row=0, column=0)
        self.add_button = Button(window,
                                   text="+1",
                                   command=self.add_one)
        self.add_button.grid(row=1, column=0)
        
        self.minus_button = Button(window,
                                   text='-1',
                                   command=self.minus_one)
        self.minus_button.grid(row=1, column=1)


    def add_one(self):
        """The event handler for clicks on the button"""
        self.current_count += 1
        self.count_label['text'] = str(self.current_count)
        
    def minus_one(self):
        self.current_count -= 1
        self.count_label['text'] = str(self.current_count)
        


def main():
    """Set up the GUI and run it."""
    window = Tk()
    counterGui = CounterGui(window)
    window.mainloop()

main()