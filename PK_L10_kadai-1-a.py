directory = "Images/imageonline-giftopng-4762753"
prefix = ""

import tkinter

n = 0 #画像番号を表す変数
def change_img():
    global n
    cvs.delete("cat")
    cvs.create_image(500,450,image=imgs[n],tag="cat")
    if s == 1:
        n = n + 1
    if n > 31:
        n = 0
    root.after(200,change_img)

s = 1 #動画のON/OFFを表す変数
def click_bt1():
    global s
    if s == 1:
        s = 0
        bt1["text"] = "すたーと！"
    else:
        s = 1
        bt1["text"] = "すとっぷ！"
    
root = tkinter.Tk()
root.title("ねこがぴょんぴょんするやつ")

cvs = tkinter.Canvas(width=1000,height=900)
cvs.pack()

imgs = []
for i in range(32): #for文
    i = i + 1
    imgs.append(tkinter.PhotoImage(file=directory+"/"+prefix+str(i)+".png"))

change_img()

bt1 = tkinter.Button(root,text="すとっぷ！",font=("Times New Roman",14),
                    command=click_bt1,width=10)
bt1.place(x=100,y=0)


root.mainloop()
