directory = "Images/imageonline-giftopng-4762753"
prefix = ""
number = "12"

import tkinter

x = 0
def change_img(): #関数を宣言
    global x #変数xをグローバル変数とする
    cvs.delete("cat") #前の図形を消去
    cvs.create_image(10*x-400,450,image=imgs[0],tag="cat")
    x = x + 1 #変数xに新たな値を代入
    if x>180:
        x = 0
    root.after(50,change_img) #50ミリ秒後に再度change_img()を実行

root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=1000,height=900)
cvs.pack()

imgs = []
imgs.append(tkinter.PhotoImage(file=directory+"/"+prefix+number+".png"))

change_img() #関数change_img()を実行
root.mainloop()
