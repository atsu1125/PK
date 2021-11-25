import tkinter

n = 0 #画像番号を表す変数
def change_img(): #関数を宣言
    global n #変数nをグローバル変数とする
    cvs.delete("kana") #前の画像を消去
    cvs.create_image(400,300,image=imgs[n],tag="kana")
    n = n + 1 #変数nに新たな値を代入
    if n > 1:
        n = 0
    root.after(200,change_img) #200ミリ秒後に再度change_img()を実行

root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=800,height=600)
cvs.pack()

imgs = [] #リストを宣言し，初期化
imgs.append(tkinter.PhotoImage(file="Images/kanarin0.png")) #画像を追加
imgs.append(tkinter.PhotoImage(file="Images/kanarin1.png")) #画像を追加

change_img() #関数change_img()を実行
root.mainloop()
