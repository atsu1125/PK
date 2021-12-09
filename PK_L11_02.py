import tkinter

x = 0 #マウスボタンをクリックした位置のx座標
y = 0 #マウスボタンをクリックした位置のy座標
s = 0 #マウスボタンを押しているか放しているかを表す変数

def mouse_press(e): #マウスボタンをクリックしたときの処理
    global s
    s = 1

def mouse_release(e): #マウスボタンをリリースしたときの処理
    global s
    s = 0

def mouse_move(e): #マウスカーソルを動かしたときの処理
    global x, y
    if s == 1:
        x = e.x #クリックした位置のx座標を変数xに代入
        y = e.y #クリックした位置のy座標を変数yに代入
        cvs.create_oval(x-10,y-10,x+10,y+10,fill="black")

root = tkinter.Tk()
root.title("PK")
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知
root.bind("<ButtonRelease>",mouse_release) #マウスボタンのリリースを感知
root.bind("<Motion>",mouse_move) #マウスカーソルの動きを感知

cvs = tkinter.Canvas(root,width=800,height=800,bg="white")
cvs.pack()

root.mainloop()
