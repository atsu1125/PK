directory = "Images/imageonline-giftopng-4762753"
prefix = ""

import tkinter

n = 0 #画像番号を表す変数
def change_img():
    global n
    cvs.delete("kana")
    cvs.create_image(500,450,image=imgs[n],tag="kana")
    n = n + 1
    if n > 31:
        n = 0
    root.after(200,change_img)

root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=1000,height=900)
cvs.pack()

imgs = []
for i in range(32): #for文
    i = i + 1
    imgs.append(tkinter.PhotoImage(file=directory+"/"+prefix+str(i)+".png"))

change_img()
root.mainloop()
