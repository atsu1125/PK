import tkinter

def bt1_on(): #ボタン1の機能
    root["bg"] = "blue"

def bt2_on(): #ボタン2の機能
    root["bg"] = "red"

def bt3_on(): #ボタン3の機能
    root["bg"] = "yellow"

root = tkinter.Tk()
root.title("プログラミング基礎")
root.geometry("600x400")
root.configure(bg="white")

bt1 =tkinter.Button(root,text="青",
                    font=("Times New Roman",24),bg="blue",
                    command=bt1_on) #ボタン1を作成
bt2 =tkinter.Button(root,text="赤",
                    font=("Times New Roman",24),bg="red",
                    command=bt2_on) #ボタン2を作成
bt3 =tkinter.Button(root,text="黄",
                    font=("Times New Roman",24),bg="yellow",
                    command=bt3_on) #ボタン3を作成
bt1.place(x=100,y=100) #ボタン1を配置
bt2.place(x=300,y=100) #ボタン2を配置
bt3.place(x=500,y=100) #ボタン3を配置

root.mainloop()
