import tkinter
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=600,height=600)
cvs.pack()

img = tkinter.PhotoImage(file="Images/KU.png")

img1 = img.zoom(2,1) #2x1に拡大
cvs.create_image(300,200,image=img1)

img2 = img.subsample(4,2) #1/4 x 1/2に縮小
cvs.create_image(300,450,image=img2)

root.mainloop()
