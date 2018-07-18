from tkinter import *

def generate():
    pass
def create():
    pass

mw = Tk()

mw.title('The nononogram game')
#You can set the geometry attribute to change the root windows size
mw.geometry("200x150") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction


#Changed variables so you don't have these set to None from .pack()
info = Label(text='Welcome to the nonono application !', fg='black')
info.pack(fill="both")
go = Button(text='Generate', command=generate)
go.pack(side=LEFT, padx=10, pady=5)
go = Button(text='Create', command=create)
go.pack(side=RIGHT, padx=10, pady=5)
close = Button(text='quit', command=mw.destroy)
close.pack(side=BOTTOM, padx=5, pady=10)
info.pack()

mw.mainloop()