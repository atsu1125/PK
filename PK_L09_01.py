import tkinter

x = 0
def change_img(): #関数を宣言
    global x #変数xをグローバル変数とする
    cvs.delete("ball") #前の図形を消去
    cvs.create_oval(10*x,150,10*x+50,200,fill="blue",tag="ball")
    x = x + 1 #変数xに新たな値を代入
    if x>60:
        x = 0
    root.after(50,change_img) #50ミリ秒後に再度change_img()を実行
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=600,height=300)
cvs.pack()

change_img() #関数change_img()を実行
root.mainloop()
