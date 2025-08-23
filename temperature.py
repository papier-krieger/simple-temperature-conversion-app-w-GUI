import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk # Takes all ttk-widgets and adds more styling options, therefore the tkk import is redundant


# root = tk.Tk()
root = ttk.Window(themename='darkly')
# root = ttk.Window(themename='journal')
root.title('°C to °F')
root.geometry('400x150')

# Functions
def c_f():
    celsius = entry_int.get()
    fahrenheit = celsius*9/5 +32
    output_string.set(fahrenheit)

def f_c():
    fahrenheit = entry_int.get()
    celsius = (fahrenheit -32)*5/9
    output_string.set(celsius)

def test():
    print('Test')


state = [(c_f, 'Celsius --> Fahrenheit', 'C/F'),(f_c, 'Fahrenheit --> Celsius', 'F/C')]
# Dynamic switch button 
def switch():
    arg = state.pop(0) 
    state.append(arg)

    button_convert.config(command = arg[0])
    title_string.set(arg[1])
    switch_string.set(arg[2])    


# tk-Variables
title_string = tk.StringVar(value='Celsius --> Fahrenheit')
entry_int = tk.IntVar()
output_string = tk.StringVar()
switch_string = tk.StringVar(value='C/F')


# title 
title_label = ttk.Label(master=root, textvariable = title_string, font='Calibri 14 bold' )
title_label.pack(pady=15)


# input field
input_frame = ttk.Frame(master=root)
button_switch= ttk.Button(master=input_frame, textvariable=switch_string , command= switch)
entry = ttk.Entry(master=input_frame, textvariable=entry_int, justify='center', width=10)
button_convert = ttk.Button(master=input_frame, text='Convert', command= c_f)

input_frame.pack()
button_switch.pack(side='left')
entry.pack(side='left', padx=10)
button_convert.pack(side='left')


# output
output_label = ttk.Label(master=root, font='Calibri 14', textvariable=output_string)
output_label.pack(pady=15)


# for item in entry.keys():
    # print(item, ':', entry[item])




root.mainloop()