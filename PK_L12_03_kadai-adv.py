import tkinter

block = [ #迷路のパターン
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,1,1,1,0,1],
    [1,0,0,0,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,1,0,1],
    [1,0,0,1,0,0,1,1,0,1],
    [1,0,0,0,0,1,1,1,0,1],
    [1,0,1,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]]

n_block = 10 #一列（一行）のブロックの数

key_name = "" #キー名称の初期値（文字列）
m = 0 #マウスのエリア初期化

bx = 5 #ボールの初期のx座標
by = 5 #ボールの初期のy座標
x = 0 #マウスx初期化
y = 0 #マウスy初期化
s = 0 #マウスクリックしてない状態に初期化

def key_press(e): #関数を宣言（キーを押したときの処理）
    global key_name
    key_name = e.keysym #押されたキーのキー名称を代入

def key_release(e): #関数を宣言（キーを放したときの処理）
    global key_name
    key_name = "" #初期値に戻す

def mouse_release(e): #マウスボタンをリリースしたときの処理
    global s, m
    s = 0
    m = 0 #マウスエリア初期化

def mouse_press(e): #マウスクリック
    global s, x, y
    s = 1
    x = e.x
    y = e.y

def mouse_move(e): #マウス移動でキーボード押下の処理に
    global x, y ,m
    x = e.x
    y = e.y
    if s == 1: #クリック時
        if 0 < x < 120 and 240 < y < 360: #左にマウスあるとき
            m = 1
        elif 240 < x < 360 and 0 < y < 120: #上
            m = 2
        elif 480 < x < 600 and 240 < y < 360: #右
            m = 3
        elif  240 < x < 360 and 480 < y < 600: #下
            m = 4

def image_move(): #関数を宣言（ボールの座標を読み込んだキーに応じて変更）
    global bx, by
    if (key_name == "Left" or key_name == "j" or m == 1) and block[by][bx-1] == 0:
        bx = bx - 1
    if (key_name == "Right" or key_name == "k" or m == 3) and block[by][bx+1] == 0:
        bx = bx + 1
    if (key_name == "Up" or key_name == "i" or m == 2) and block[by-1][bx] == 0:
        by = by - 1
    if (key_name == "Down" or key_name == "m" or m == 4) and block[by+1][bx] == 0:
        by = by + 1
    if key_name == "Escape": #初期化ボタン
        bx = 5
        by = 5

    cvs.coords("ball",60*bx,60*by,60*(bx+1),60*(by+1)) #ballの座標を変更
    root.after(200,image_move) #100ミリ秒後に再度実行、重いので200

    if bx == 8 and by == 3: #OUT判定
        cvs.create_text(300,300,text="OUT",font=("MS 明朝",200),tag="out",fill="red")
    else:
        cvs.delete("out")
    if bx == 8 and by == 7: #GOAL判定
        cvs.create_text(300,300,text="GOAL",font=("MS 明朝",180),tag="goal",fill="blue")
    else:
        cvs.delete("goal")

#    cvs.delete("location") #ボールがどこ
#    cvs.create_text(300,500,text="bx="+str(bx)+",by="+str(by),font=("MS 明朝",50),tag="location",fill="blue")
#    cvs.delete("mouse") #マウスがどこ
#    cvs.create_text(300,450,text="x="+str(x)+",y="+str(y),font=("MS 明朝",50),tag="mouse",fill="blue")
#    cvs.delete("mouse_l") #マウスがどこのエリアか
#    cvs.create_text(300,400,text="m="+str(m),font=("MS 明朝",50),tag="mouse_l",fill="blue")


root = tkinter.Tk()
root.title("PK")
root.bind("<KeyPress>", key_press) #キーが押したときに関数key_downを実行
root.bind("<KeyRelease>", key_release) #キーが放したときに関数key_upを実行
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知
root.bind("<ButtonRelease>",mouse_release) #マウスボタンのリリースを感知
root.bind("<Motion>",mouse_move) #マウスカーソルの動きを感知

cvs = tkinter.Canvas(root,width=600,height=600,bg="white")
cvs.pack()

for x in range(n_block):
    for y in range(n_block):
        if block[y][x] == 1: #座標(x,y)のパターンが1のときブロックを描く
            cvs.create_rectangle(60*x,60*y,60*(x+1),60*(y+1),fill="orange4")

cvs.create_oval(60*bx,60*by,60*(bx+1),60*(by+1),fill="purple",tag="ball")
cvs.create_oval(60*8,60*3,60*(8+1),60*(3+1),fill="black",tag="hall")
cvs.create_oval(60*8,60*7,60*(8+1),60*(7+1),fill="gold",tag="hall")


image_move()

root.mainloop()
