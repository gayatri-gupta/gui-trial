from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
win = Tk()
win.title("Converter: Feet to Meters ")

window = ttk.Frame(win)
window.grid(column=0, row=0)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(window, width=7, textvariable=feet)
feet_entry.grid(column=1, row=0)

ttk.Label(window, textvariable=meters,background ="sky blue" ).grid(column=1, row=1)
ttk.Button(window, text="Convert", command = calculate).grid(column=1, row=2)
ttk.Label(window, text="Enter Value in feet:").grid(column=0, row=0)
ttk.Label(window, text="Value in meters:").grid(column=0, row=1)
for child in window.winfo_children(): child.grid_configure(padx=8, pady=8) 

win.mainloop()
