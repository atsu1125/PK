import tkinter
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=1000,height=600)
cvs.pack()

img = []
img.append(tkinter.PhotoImage(file="Images/coop_0.png"))
img.append(tkinter.PhotoImage(file="Images/coop_1.png"))
img[0] = img[0].subsample(3,3) #1/3 x 1/3 に縮小
img[1] = img[1].subsample(3,3)
cvs.create_image(170,150,image=img[0])
cvs.create_image(170+330,150,image=img[0])
cvs.create_image(170+330*2,150,image=img[0])
cvs.create_image(170,150+270,image=img[1])
cvs.create_image(170+330,150+270,image=img[1])
cvs.create_image(170+330*2,150+270,image=img[1])

root.mainloop()
