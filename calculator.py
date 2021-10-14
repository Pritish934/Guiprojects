from tkinter import *

def click(event):
    global scvar
    text = event.widget.cget("text")
    if text == "=":
        if scvar.get().isdigit():
            value = int(scvar.get())
        else:
            value = eval(scvar.get())
            scvar.set(value)
            screen.update()
    elif text == "C":
        scvar.set('')
        screen.update()
    else:
        scvar.set(scvar.get() + text)
        screen.update()


root = Tk()
root.geometry("400x500")

scvar = StringVar()
scvar.set('')

screen = Entry(root,textvariable=scvar, font="lucida 30 bold")
screen.pack(padx=5,pady=5)

f = Frame(root,bg="skyblue")
b = Button(f,text="9",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="8",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="7",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="+",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="skyblue")
b = Button(f,text="6",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="5",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="4",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="-",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="skyblue")
b = Button(f,text="3",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="2",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="1",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="*",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root,bg="skyblue")
b = Button(f,text="0",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="/",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="=",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)

b = Button(f,text="C",font="lucida 20 bold")
b.pack(side=LEFT,padx=5, pady=5)
b.bind("<Button-1>", click)
f.pack()

root.mainloop()