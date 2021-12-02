import tkinter

n = 0 #画像番号を表す変数
def change_img():
    global n
    cvs.delete("kana")
    cvs.create_image(400,300,image=imgs[n],tag="kana")
    n = n + 1
    if n > 4:
        n = 0
    root.after(200,change_img)
    
root = tkinter.Tk()
root.title("PK")

cvs = tkinter.Canvas(width=800,height=600)
cvs.pack()

imgs = []
for i in range(5): #for文
    imgs.append(tkinter.PhotoImage(file="Images/kanarin"+str(i)+".png"))

change_img()
root.mainloop()
