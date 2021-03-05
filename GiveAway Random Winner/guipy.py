#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from time import sleep
import pandas as pd

# A dummy `csv_text` function
def csv_text():
    delay = 1.0
    
    csvfile = pd.read_csv('your list path here', engine='python',encoding='utf-8')
    print_to_gui('5')
    sleep(delay)
    print_to_gui('4')
    sleep(delay)
    print_to_gui('3')
    sleep(delay)
    print_to_gui('2')
    sleep(delay)
    print_to_gui('1')
    sleep(delay)
    print_to_gui(csvfile.sample())

# Display a string in `out_label`
def print_to_gui(text_string):
    out_label.config(text=text_string)
    # Force the GUI to update
    top.update()

# Build the GUI
top = tk.Tk()
top.wm_title("Your Give Away Title Text Here")
top.config(bg='black')
top.minsize(width=700, height=300)
top.maxsize(width=500, height=500)


b = tk.Button( text='Run', command=csv_text, fg="white", bg="black", font=('times',20,'bold'))
b.config(width=15, height=1)
b.pack()

# A Label to display output from the `csv_text` function
out_label = tk.Label(text='Click button to start',fg="white", bg="black", font=('times','20','bold'))
out_label.pack()

top.mainloop()

