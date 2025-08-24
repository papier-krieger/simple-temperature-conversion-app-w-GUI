import tkinter as tk
# from tkinter import ttk 
import ttkbootstrap as ttk # Takes all ttk-widgets and adds more styling options, therefore the tkk import is redundant


# root = tk.Tk()
root = ttk.Window(themename='darkly')
# root = ttk.Window(themename='journal')
root.title('Temperature Converter')
root.geometry('400x150')

# Functions
def c_f():
    try:
        celsius = float(entry_string.get())
        fahrenheit = celsius*9/5 +32
        output_string.set(fahrenheit)
    except:
        output_string.set('ERROR')
    

def f_c():
    try:
        fahrenheit = float(entry_string.get())
        celsius = (fahrenheit -32)*5/9
        output_string.set(celsius)
    except:
        output_string.set('ERROR')
        

def clear_entry(whatever):
    entry_string.set('')

state = [(c_f, 'Celsius  -->  Fahrenheit'),(f_c, 'Fahrenheit  -->  Celsius')]
# Dynamic switch button 
def switch():
    arg = state.pop(0) 
    state.append(arg)

    button_convert.config(command = arg[0])
    title_string.set(arg[1])


# tk-Variables
title_string = tk.StringVar(value='Fahrenheit  -->  Celsius')
entry_string = tk.StringVar()
output_string = tk.StringVar()


# title 
title_button = ttk.Button(master=root, textvariable = title_string, command= switch)
title_button.pack(pady=15)


# input field
input_frame = ttk.Frame(master=root)
entry = ttk.Entry(master=input_frame, textvariable=entry_string, justify='center', width=10)
button_convert = ttk.Button(master=input_frame, text='Convert', command= f_c)

# bind left-click event to clear_entry function 
entry.bind('<Button-1>', clear_entry)

input_frame.pack()
entry.pack(side='left', padx=10)
button_convert.pack(side='left')


# output
output_label = ttk.Label(master=root, font='Calibri 14', textvariable=output_string)
output_label.pack(pady=15)


# for item in entry.keys():
    # print(item, ':', entry[item])




root.mainloop()