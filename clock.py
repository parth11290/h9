import tkinter as tk
from datetime import datetime as dat
ty=tk.Tk()
tlp=tk.Label(
    ty,
    font=("Arial",80,"bold"),
    bg="black",
    fg="cyan",
)
ttp=tk.Label(
    ty,
    font=("Arial",40,"bold"),
    bg="black",
    fg="white",
)
tllp=tk.Label(
    ty,
    font=("Arial",40,"bold"),
    bg="black",
    fg="green",
)
tlp.pack()
tllp.pack(padx=2)
ttp.pack(padx=8)
ty.title("Digital Clock")
ty.geometry("2000x400")
ty.configure(bg="black")

def update():
    op=dat.now().strftime("%H:%M:%S")
    print(op)
    tlp.config(text=op)
    oppp=dat.now().strftime("%d:%B:%Y")
    print(oppp)
    ttp.config(text=oppp)
    opo=dat.now().strftime("%A")
    print(opo)
    tllp.config(text=opo)
    ty.after(1000,update)
update()
ty.mainloop()