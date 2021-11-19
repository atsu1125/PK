import tkinter
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=600,height=600)
cvs.pack()

img = tkinter.PhotoImage(file="Images/KU.png") #画像変数に代入
cvs.create_image(300,300,image=img) #画像を表示

root.mainloop()
