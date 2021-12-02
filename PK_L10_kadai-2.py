directory = "Images/imageonline-giftopng-4762753"
prefix = ""
number = "12"

import tkinter

x = 0
def change_img(): #関数を宣言
    global x #変数xをグローバル変数とする
    cvs.delete("dog") #前の図形を消去
    cvs.create_image(10*x-400,450,image=imgs[0],tag="dog")
    if s == 1:
        x = x + 1 #変数xに新たな値を代入
    if x>180:
        x = 0
    root.after(t,change_img) #50ミリ秒後に再度change_img()を実行
    if s ==1:
        doeswork = "動作中"
    else:
        doeswork = "停止中"
#    cvs.delete("tms")
#    cvs.create_text(800,20,text=str(t)+"ミリ秒で"+doeswork,font=("MS 明朝",20),tag="tms")

s = 1 #動画のON/OFFを表す変数
def click_bt1():
    global s
    s = 1
def click_bt2():
    global s
    s = 0

t = 50 #動画の待ち時間を表わす変数
def click_bt3():
    global t
    if t > 10:
        t = t - 10
def click_bt4():
    global t
    if t < 90:
        t = t + 10
def click_bt5():
    global t
    t = 50
    global x
    x = 0
    global s
    s = 0

root = tkinter.Tk()
root.title("いぬが１次元移動するやつ")

cvs = tkinter.Canvas(width=1000,height=900)
cvs.pack()

imgs = []
imgs.append(tkinter.PhotoImage(file=directory+"/"+prefix+number+".png"))

change_img() #関数change_img()を実行

bt1 = tkinter.Button(root,text="START",font=("Times New Roman",14),
                    command=click_bt1,width=6)
bt2 = tkinter.Button(root,text="STOP",font=("Times New Roman",14),
                    command=click_bt2,width=6)
bt3 = tkinter.Button(root,text="SPEED UP",font=("Times New Roman",14),
                    command=click_bt3,width=12)
bt4 = tkinter.Button(root,text="SPEED DOWN",font=("Times New Roman",14),
                    command=click_bt4,width=12)
bt5 = tkinter.Button(root,text="RESET",font=("Times New Roman",14),
                    command=click_bt5,width=6)
bt1.place(x=100,y=0)
bt2.place(x=200,y=0)
bt3.place(x=300,y=0)
bt4.place(x=500,y=0)
#bt5.place(x=900,y=0)

root.mainloop()
