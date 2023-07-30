from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            #Typecasting the value into integer
            value = int(scvalue.get())
        else:
            #Eval evaluates a string
            value= eval(screen.get())
        scvalue.set(value)
        screen.update()


    elif text =="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
       #Update function forces updates(screen value gets updates with scvalue)

root = Tk()


root.geometry("400x550")
root.title("Python Calculator")

scvalue= StringVar()
#Setting its  value
scvalue.set("")
screen = Entry(root,textvar=scvalue,font="lucida 20 bold")
#ipadx is internal padding
screen.pack(fill=X,ipadx=8,pady=10,padx=10 )
f = Frame(root,bg="grey")
b = Button(f,text="9",padx=15,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="8",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text="7",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()


f = Frame(root,bg="grey")
b = Button(f,text="6",padx=15,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="5",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text="4",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()
f = Frame(root,bg="grey")
b = Button(f,text="3",padx=15,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="2",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text="1",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()
f = Frame(root,bg="grey")
b = Button(f,text="0",padx=16,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="-",padx=16,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text="*",padx=16,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()
f = Frame(root,bg="grey")
b = Button(f,text="/",padx=15,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="+",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text="=",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()
f = Frame(root,bg="grey")
b = Button(f,text="C",padx=15,pady=10,font="lucida 15 bold")

b.pack(side=LEFT,padx=15,pady=5)
#Binding functions with click function
b.bind("<Button-1>",click)

b = Button(f,text="(",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)


b = Button(f,text=")",padx=15,pady=10,font="lucida 15 bold")
b.pack(side=LEFT,padx=15,pady=5)
b.bind("<Button-1>",click)

f.pack()
root.mainloop()