import tkinter

x = 0 #マウスボタンをクリックした位置のx座標
y = 0 #マウスボタンをクリックした位置のy座標
s = 0 #マウスボタンを押しているか放しているかを表す変数
c = 0 #描画色を表す変数

def mouse_press(e): #マウスボタンをクリックしたときの処理
    global x, y, s, c
    x = e.x
    y = e.y
    s = 1
    if x > 100 and x < 150 and y < 50:
        c = 0
    if x > 150 and x < 200 and y < 50:
        c = 1

def mouse_release(e): #マウスボタンをリリースしたときの処理
    global s
    s = 0

def mouse_move(e): #マウスカーソルを動かしたときの処理
    global x, y
    if s == 1:
        x = e.x
        y = e.y
        if y > 60:
            if c == 0:
                cvs.create_oval(x-10,y-10,x+10,y+10,fill="black")
            if c == 1:
                cvs.create_oval(x-10,y-10,x+10,y+10,
                                fill="white",outline="white")
root = tkinter.Tk()
root.title("PK")
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知
root.bind("<ButtonRelease>",mouse_release) #マウスボタンのリリースを感知
root.bind("<Motion>",mouse_move) #マウスカーソルの動きを感知

cvs = tkinter.Canvas(root,width=800,height=800,bg="white")
cvs.pack()
cvs.create_rectangle(100,0,150,50,fill="black")
cvs.create_rectangle(150,0,200,50,fill="white")

root.mainloop()
