import tkinter
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=600,height=600)
cvs.pack()

for i in range(10):
    cvs.create_oval(50+50*i,50,100+50*i,100,fill="orange")

root.mainloop()
