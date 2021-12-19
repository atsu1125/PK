import tkinter

key_name = "" #キー名称の初期値は空白（文字列）
def key_down(e): #関数を宣言（キーを押したときの処理）
    global key_name
    key_name = e.keysym #押されたキーのキー名称を代入

def key_up(e): #関数を宣言（キーを放したときの処理）
    global key_name
    key_name = "" #初期値に戻す

kx = 300 #x座標の初期値
ky = 300 #y座標の初期値
def image_move(): #関数を宣言（画像の座標を読み込んだキーに応じて変更）
    global kx, ky
    if (key_name == "Left" or key_name == "j") and kx > 0:
        kx = kx - 10
    if (key_name == "Right" or key_name == "k") and kx < 600:
        kx = kx + 10
    if (key_name == "Up" or key_name == "i") and ky > 0:
        ky = ky - 10
    if (key_name == "Down" or key_name == "m") and ky < 600:
        ky = ky + 10
    if key_name == "Escape":
        kx = 300
        ky = 300

    cvs.coords("kana",kx,ky) #kanaのtagがついた画像の座標を(kx,ky)に変更
    root.after(50,image_move) #50ミリ秒後に再度実行

root = tkinter.Tk()
root.title("PK")
root.bind("<KeyPress>", key_down) #キーが押されたときに関数key_downを実行
root.bind("<KeyRelease>", key_up) #キーが放されたときに関数key_upを実行

cvs = tkinter.Canvas(root,width=600,height=600,bg="white")
cvs.pack()

img = tkinter.PhotoImage(file="Images/kanarin2.png")
img = img.subsample(4,4)

cvs.create_image(kx,ky,image=img,tag="kana")
image_move()

root.mainloop()
