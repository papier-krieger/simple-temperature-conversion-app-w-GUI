import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk # Takes all ttk-widgets and adds more styling options, therefore the tkk import is redundant


# root = tk.Tk()
root = ttk.Window(themename='darkly')
# root = ttk.Window(themename='journal')
root.title('°C to °F')
root.geometry('400x150')

# Functions
def do_conversion():
    celsius = entry_int.get()
    fahrenheit = celsius*9/5 +32
    output_string.set(fahrenheit)

def do_reset():
    print('resetting')

# tk-Variables
entry_int = tk.IntVar()
output_string = tk.StringVar()


# title 
title_label = ttk.Label(master=root, text='Celsius --> Fahrenheit', font='Calibri 14 bold' )
title_label.pack(pady=15)


# input field
input_frame = ttk.Frame(master=root)
button_reset= ttk.Button(master=input_frame, text='Reset', command= do_reset)
entry = ttk.Entry(master=input_frame, textvariable=entry_int, justify='center', width=10)
button_convert = ttk.Button(master=input_frame, text='Convert', command= do_conversion)

input_frame.pack()
entry.pack(side='left', padx=10)
button_convert.pack(side='left')


# output
output_label = ttk.Label(master=root, text='Result', font='Calibri 14', textvariable=output_string)
output_label.pack(pady=15)


# for item in entry.keys():
    # print(item, ':', entry[item])




root.mainloop()