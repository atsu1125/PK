import tkinter

def bt_on(): #ボタンの機能
    bt["text"] = "クリックしました"

root = tkinter.Tk()
root.title("プログラミング基礎")

root.geometry("600x400")

bt =tkinter.Button(root,text="ここをクリック",
                   font=("Times New Roman",24),
                   bg="yellow",command=bt_on) #ボタンの作成

bt.place(x=200,y=100)

root.mainloop()
