import tkinter

def bt_on(): #ボタンの機能
    lb["bg"] = "green"

root = tkinter.Tk()
root.title("プログラミング基礎")

root.geometry("600x400")

lb =tkinter.Label(root,text="ラベル",font=("System",24))

lb.place(x=200,y=150)

bt =tkinter.Button(root,text="ここをクリック",
                   font=("Times New Roman",24),
                   bg="yellow",command=bt_on) #ボタンの作成

bt.place(x=200,y=100)

root.mainloop()
