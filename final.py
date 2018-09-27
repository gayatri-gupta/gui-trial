import newsapi
import pandas as pd 
from tkinter import *
import tkinter.messagebox

apikey = 'a27170e8ac5b45d6bf5cf58009ff9889'

from newsapi.articles import Articles
a = Articles(API_KEY=apikey)


def nw():
    ans = tkinter.messagebox.askquestion("Action","Want to Update?")

    if ans == "yes":
        print("Updated!")
        tkinter.messagebox.showinfo("Updated","Updated!")

root = Tk()
tf = Frame(root)
label = Label(tf,text="News Update")
label.pack(side=TOP)


def gr():
    print(var.get())
    data = a.get(source=var.get(), sort_by='top')
    data = pd.DataFrame.from_dict(data)
    data = pd.concat([data.drop(['articles'], axis=1),
                      data['articles'].apply(pd.Series)], axis=1)
    output.insert(END, data)

var = StringVar()
choices = ['aftenposten', 'abc-news', 'fortune',
           'football-italia', 'financial-times', 'focus']

#option = tk.
OptionMenu(root, var, *choices).grid(row=2, column=1, sticky=W)
Button(root, width=10, text="Get Results", command=gr).grid(row=2, column=0, sticky=W)

#output
Info = Label(root,text="Headlines")
Info.grid(row=3,column=0)
output = Text(root,width=30,height=10,background="sky blue")
output.grid(ipadx=240,ipady=300,row=4,sticky=W)
root.mainloop()
