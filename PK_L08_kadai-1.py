import tkinter
root = tkinter.Tk()
root.title("かつやのメニュー")

cvs = tkinter.Canvas(width=1000,height=600)
cvs.pack()

img = []
img.append(tkinter.PhotoImage(file="Images/katsudon-take.png"))
img.append(tkinter.PhotoImage(file="Images/katsudon-ume.png"))
img.append(tkinter.PhotoImage(file="Images/katsudon-matsu.png"))
img[0] = img[0].subsample(3,3)
img[1] = img[1].subsample(3,3)
img[2] = img[2].subsample(3,3)
cvs.create_image(170,350,image=img[0])
cvs.create_image(170+330,350,image=img[1])
cvs.create_image(170+330*2,350,image=img[2])

cvs.create_text(500,50,text="好きなかつやのメニューベスト３",font=("MS 明朝",50))
cvs.create_text(170,150,text="１位",font=("MS 明朝",50))
cvs.create_text(170+330,150,text="２位",font=("MS 明朝",50))
cvs.create_text(170+330*2,150,text="３位",font=("MS 明朝",50))

root.mainloop()
