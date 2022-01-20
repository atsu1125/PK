directory = "Images/imageonline-giftopng-4762753" #ディレクトリ１の相対パス
directory2 = "Images/imageonline-giftopng-5598698" #ディレクトリ２の相対パス
prefix = "" #ファイル名の接頭辞

import random
import tkinter

block = [ #迷路のパターン
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,1],
    [1,0,1,1,0,0,1,0,1,1],
    [1,0,1,0,0,0,1,0,1,1],
    [1,0,1,1,0,0,1,0,1,1],
    [1,0,1,0,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,1,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,1,1,1,1]]

n_block = 10 #一列（一行）のブロックの数

key_name = "" #キー名称の初期値（文字列）
m = 0 #マウスのエリア初期化

bx = random.randint(1,8) #ボールの初期のx座標　ランダムに配置
by = random.randint(1,8) #ボールの初期のy座標　ランダムに配置
x = 0 #マウスx初期化
y = 0 #マウスy初期化
s = 0 #マウスクリックしてない状態に初期化
n = 0 #何枚目の画像かを初期化

def change_img(): #関数を宣言
    global n #変数nをグローバル変数とする　画像が何枚目かを表す
    cvs.delete("dog") #前の図形を消去
    if imaged == 0: #imagedが０の場合はディレクトリ１
        cvs.create_image(900,450,image=imgs[n],tag="dog")
    elif imaged == 1: #imagedが１の場合はディレクトリ２
        cvs.create_image(900,450,image=imgs2[n],tag="dog")
    if images == 1:
        n = n + 1 #変数nに新たな値を代入
    else:
        cvs.delete("dog")
    if n > 31: #画像の枚数最後まで行ったら戻る
        n = 0
    root.after(t,change_img) #tミリ秒後に再度change_img()を実行
    if images == 1: #再生されてるかどうか
        doeswork = "再生中"
    else:
        doeswork = "停止中"
    cvs.delete("tms")
    cvs.create_text(900,50,text=str(t)+"ミリ秒で"+doeswork+"おかしくなったらRESETをクリック",font=("MS 明朝",20),tag="tms") #何秒で再生してるか

images = 0 #動画のON/OFFを表す変数
imaged = 0 #動画のディレクトリを表す変数

t = 200 #動画の待ち時間を表わす変数
def click_bt3(): #speed up
    global t
    if t > 100: #100ミリ秒より大きい限り許可
        t = t - 10
def click_bt4(): #speed down
    global t
    if t < 300: #300ミリ秒より小さい限り許可
        t = t + 10
def click_bt5(): #reset
    global t
    t = 200 #待ち時間初期化
    global n
    n = 0 #画像の何枚目か初期化
    global m, bx, by
    m = 0 #マウスのエリア初期化　ときどきマウスの認識がバグるのでリセット用
    bx = random.randint(1,8) #ボールの初期のx座標　ときどきブロックの中に入るのでリセット用
    by = random.randint(1,8) #ボールの初期のy座標

def key_press(e): #関数を宣言（キーを押したときの処理）
    global key_name
    key_name = e.keysym #押されたキーのキー名称を代入

def key_release(e): #関数を宣言（キーを放したときの処理）
    global key_name
    key_name = "" #キーボードの押された場所を初期値に戻す

def mouse_release(e): #マウスボタンをリリースしたときの処理（ダミー）
    global s
    s = 0

def mouse_press(e): #マウスクリックの処理（ダミー） 本来クリック時のみ動けばいいがスムーズにいかないので
    global s, x, y
    s = 1
    x = e.x
    y = e.y

def mouse_move(e): #マウス移動でキーボード押下の処理に渡すだけ
    global x, y ,m
    x = e.x
    y = e.y
    if 0 < x < 120 and 240 < y < 360: #左にマウスあるとき
        m = 1
    elif 240 < x < 360 and 0 < y < 120: #上
        m = 2
    elif 480 < x < 600 and 240 < y < 360: #右
        m = 3
    elif  240 < x < 360 and 480 < y < 600: #下
        m = 4
    else: #エリア外
        m = 0

def image_move(): #関数を宣言（ボールの座標を読み込んだキーとマウスオーバーした場所に応じて変更）
    global bx, by, images, imaged
    if (key_name == "Left" or key_name == "j" or m == 1) and block[by][bx-1] == 0:
        bx = bx - 1
    if (key_name == "Right" or key_name == "k" or m == 3) and block[by][bx+1] == 0: 
        bx = bx + 1
    if (key_name == "Up" or key_name == "i" or m == 2) and block[by-1][bx] == 0:
        by = by - 1
    if (key_name == "Down" or key_name == "m" or m == 4) and block[by+1][bx] == 0:
        by = by + 1
    if key_name == "Escape": #ボール位置初期化用、そもそもランダムに配置してるが
        bx = 5
        by = 5

    cvs.coords("ball",60*bx,60*by,60*(bx+1),60*(by+1)) #ballの座標を変更
    root.after(200,image_move) #100ミリ秒後に再度実行、重いので200ミリ秒にした

    if bx == 4 and by == 7: #OUT判定でディレクトリ２の画像を動画再生
        cvs.create_text(300,300,text="OUT",font=("MS 明朝",200),tag="out",fill="red")
        images = 1
        imaged = 1
    elif bx == 8 and by == 7: #GOAL判定でディレクトリ１の画像を動画再生
        cvs.create_text(300,300,text="GOAL!",font=("MS 明朝",180),tag="goal",fill="orange")
        images = 1
        imaged = 0
    else: #OUTでもGOALでもない場合は動画を停止する、実際は画面から消去される
        cvs.delete("goal")
        cvs.delete("out")
        images = 0

    #デバッグ用
    #cvs.delete("location") #ボールがどこ
    #cvs.create_text(300,500,text="bx="+str(bx)+",by="+str(by),font=("MS 明朝",50),tag="location",fill="blue")
    #cvs.delete("mouse") #マウスがどこ
    #cvs.create_text(300,450,text="x="+str(x)+",y="+str(y),font=("MS 明朝",50),tag="mouse",fill="blue")
    #cvs.delete("mouse_l") #マウスがどこのエリアか
    #cvs.create_text(300,400,text="m="+str(m),font=("MS 明朝",50),tag="mouse_l",fill="blue")

root = tkinter.Tk()
root.title("プログラミング基礎最終課題")
root.bind("<KeyPress>", key_press) #キーが押したときに関数key_downを実行
root.bind("<KeyRelease>", key_release) #キーが放したときに関数key_upを実行
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知
root.bind("<ButtonRelease>",mouse_release) #マウスボタンのリリースを感知
root.bind("<Motion>",mouse_move) #マウスカーソルの動きを感知

cvs = tkinter.Canvas(root,width=1200,height=600,bg="white")
cvs.pack()

imgs = []
for i in range(32): #for文
    i = i + 1
    imgs.append(tkinter.PhotoImage(file=directory+"/"+prefix+str(i)+".png"))
imgs2 = []
for i in range(32): #for文
    i = i + 1
    imgs2.append(tkinter.PhotoImage(file=directory2+"/"+prefix+str(i)+".png"))

change_img() #関数change_img()を実行

bt3 = tkinter.Button(root,text="SPEED UP",font=("Times New Roman",14), #速度変更ボタン
                    command=click_bt3,width=12)
bt4 = tkinter.Button(root,text="SPEED DOWN",font=("Times New Roman",14),
                    command=click_bt4,width=12)
bt5 = tkinter.Button(root,text="RESET",font=("Times New Roman",14),
                    command=click_bt5,width=6)

bt3.place(x=800,y=0) #スピードアップ
bt4.place(x=950,y=0) #スピードダウン
bt5.place(x=1120,y=0) #リセット

for x in range(n_block):
    for y in range(n_block):
        if block[y][x] == 1: #座標(x,y)のパターンが1のときブロックを描く
            cvs.create_rectangle(60*x,60*y,60*(x+1),60*(y+1),fill="orange4")

cvs.create_oval(60*bx,60*by,60*(bx+1),60*(by+1),fill="purple",tag="ball") #ボール
cvs.create_oval(60*4,60*7,60*(4+1),60*(7+1),fill="black",tag="hall") #アウト穴
cvs.create_oval(60*8,60*7,60*(8+1),60*(7+1),fill="gold",tag="hall") #ゴール穴
cvs.create_polygon(0,300, #leftのマウス位置目安
                   60,270,
                   60,330,
                   fill="#0000ff",
                   activefill="#ff0000",tag="pol")
cvs.create_polygon(300,0, #up
                   270,60,
                   330,60,
                   fill="#0000ff",
                   activefill="#ff0000",tag="pol")
cvs.create_polygon(600,300, #right
                   540,270,
                   540,330,
                   fill="#0000ff",
                   activefill="#ff0000",tag="pol")
cvs.create_polygon(300,600, #down
                   270,540,
                   330,540,
                   fill="#0000ff",
                   activefill="#ff0000",tag="pol")


image_move()

root.mainloop()
