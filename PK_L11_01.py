import tkinter

x = 0 #マウスボタンをクリックした位置のx座標の初期値
y = 0 #マウスボタンをクリックした位置のy座標の初期値

def mouse_press(e): #マウスボタンをクリックしたときの処理
    global x, y
    x = e.x #クリックした位置のx座標を変数xに代入
    y = e.y #クリックした位置のy座標を変数yに代入
    cvs.create_oval(x-10,y-10,x+10,y+10,fill="black")

root = tkinter.Tk()
root.title("PK")
root.bind("<ButtonPress>",mouse_press) #マウスボタンのクリックを感知

cvs = tkinter.Canvas(root,width=800,height=800,bg="white")
cvs.pack()

root.mainloop()
