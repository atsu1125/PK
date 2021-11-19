import tkinter
root = tkinter.Tk()
root.title("プログラミング基礎")

cvs = tkinter.Canvas(width=600,height=600)
cvs.pack()
cvs.create_rectangle(100,50,300,150,fill="blue")
cvs.create_oval(300,150,500,250,outline="orange",width=5)
cvs.create_polygon(100,300,500,300,500,400,
                   fill="pink",outline="red",width=10)
root.mainloop()
