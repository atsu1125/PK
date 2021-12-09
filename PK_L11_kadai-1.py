import tkinter

x = 0 #マウスボタンをクリックした位置のx座標
y = 0 #マウスボタンをクリックした位置のy座標
s = 0 #マウスボタンを押しているか放しているかを表す変数
c = 0 #描画色を表す変数
k = 0


def mouse_press(e): #マウスボタンをクリックしたときの処理
    global x, y, s, c
    x = e.x
    y = e.y
    s = 1
    if x > 100 and x < 150 and y < 50:
        c = 0
    if x > 150 and x < 200 and y < 50:
        c = 1
    if x > 200 and x < 250 and y < 50:
        c = 2
    if x > 250 and x < 300 and y < 50:
        c = 3
    if x > 300 and x < 350 and y < 50:
        c = 4
    if x > 350 and x < 400 and y < 50:
        c = 5
    if x > 400 and x < 450 and y < 50:
        c = 6

def mouse_release(e): #マウスボタンをリリースしたときの処理
    global s
    s = 0

def mouse_move(e): #マウスカーソルを動かしたときの処理
    global x, y
    if s == 1:
        x = e.x
        y = e.y
        if y > 60:
            if k == 0:
                if c == 0:
                    cvs.create_oval(x-10,y-10,x+10,y+10,fill="black",tag="pen")
                if c == 1:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="white",outline="white",tag="pen")
                if c == 2:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="darkblue",outline="darkblue",tag="pen")
                if c == 3:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="blue",outline="blue",tag="pen")
                if c == 4:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="lightblue",outline="lightblue",tag="pen")
                if c == 5:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="darkcyan",outline="darkcyan",tag="pen")
                if c == 6:
                    cvs.create_oval(x-10,y-10,x+10,y+10,
                                    fill="cyan",outline="cyan",tag="pen")
            if k == 1:
                if c == 0:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,fill="black",tag="pen")
                if c == 1:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="white",outline="white",tag="pen")
                if c == 2:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="darkblue",outline="darkblue",tag="pen")
                if c == 3:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="blue",outline="blue",tag="pen")
                if c == 4:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="lightblue",outline="lightblue",tag="pen")
                if c == 5:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="darkcyan",outline="darkcyan",tag="pen")
                if c == 6:
                    cvs.create_rectangle(x-10,y-10,x+10,y+10,
                                    fill="cyan",outline="cyan",tag="pen")
    if c == 0:
        color="black"
    if c == 1:
        color="white"
    if c == 2:
        color="darkblue"
    if c == 3:
        color="blue"
    if c == 4:
        color="lightblue"
    if c == 5:
        color="darkcyan"
    if c == 6:
        color="cyan"
    if k == 0:
        shape="oval"
    if k == 1:
        shape="rectangle"
    cvs.delete("color")
    cvs.create_text(620,50,text="Color:"+color+"Shape:"+shape,font=("MS 明朝",20),tag="color")

def alldelete():
    cvs.delete("pen")

def oval():
    global k, shape
    k = 0
def rectangle():
    global k, shape
    k = 1
    
root = tkinter.Tk()
root.title("PK")
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知
root.bind("<ButtonRelease>",mouse_release) #マウスボタンのリリースを感知
root.bind("<Motion>",mouse_move) #マウスカーソルの動きを感知

cvs = tkinter.Canvas(root,width=800,height=800,bg="white")
cvs.pack()
cvs.create_rectangle(100,0,150,50,fill="black")
cvs.create_rectangle(150,0,200,50,fill="white")
cvs.create_rectangle(200,0,250,50,fill="darkblue")
cvs.create_rectangle(250,0,300,50,fill="blue")
cvs.create_rectangle(300,0,350,50,fill="lightblue")
cvs.create_rectangle(350,0,400,50,fill="darkcyan")
cvs.create_rectangle(400,0,450,50,fill="cyan")

bt1 = tkinter.Button(root,text="ERASE",font=("Times New Roman",14),
                    command=alldelete,width=6)
bt2 = tkinter.Button(root,text="○",font=("Times New Roman",14),
                    command=oval,width=3)
bt3 = tkinter.Button(root,text="□",font=("Times New Roman",14),
                    command=rectangle,width=3)
bt1.place(x=720,y=0)
bt2.place(x=640,y=0)
bt3.place(x=680,y=0)
root.mainloop()
