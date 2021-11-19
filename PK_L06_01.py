import tkinter
root = tkinter.Tk()
root.title("プログラミング基礎")

cvs = tkinter.Canvas(width=600,height=400)
cvs.pack()
cvs.create_text(150,50,text="あいうえお",fill="blue",
                font=("MS 明朝",28))
cvs.create_text(150,100,text="ABCDE",fill="red",
                font=("Times New Roman",28,"bold"))

root.mainloop()
