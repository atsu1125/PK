import tkinter

n = 0 #画像番号を表す変数
def change_img():
    global n
    cvs.delete("kana")
    cvs.create_image(400,300,image=imgs[n],tag="kana")
    if s == 1:
        n = n + 1
    if n > 4:
        n = 0
    root.after(t,change_img)

s = 0 #動画のON/OFFを表す変数
def click_bt1():
    global s
    s = 1

def click_bt2():
    global s
    s = 0

t=200 #動画の待ち時間を表わす変数
def click_bt3():
    global t
    if t > 20:
        t = t - 10
    
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=800,height=600)
cvs.pack()

imgs = []
for i in range(5): #for文
    imgs.append(tkinter.PhotoImage(file="Images/kanarin"+str(i)+".png"))

change_img()

bt1 = tkinter.Button(root,text="START",font=("Times New Roman",14),
                    command=click_bt1,width=6)
bt2 = tkinter.Button(root,text="STOP",font=("Times New Roman",14),
                    command=click_bt2,width=6)
bt3 = tkinter.Button(root,text="SPEED UP",font=("Times New Roman",14),
                    command=click_bt3,width=12)
bt1.place(x=100,y=0)
bt2.place(x=200,y=0)
bt3.place(x=300,y=0)

root.mainloop()
