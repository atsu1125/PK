import tkinter

def bt0_on(): #ボタンbt0をクリック時の処理（画像img[0]の表示）
 cvs.delete("katsudon") #katsudonのタグを持つ対象を消去
 cvs.create_image(300,270,image=img[0],tag="katsudon")

def bt1_on(): #ボタンbt1をクリック時の処理（画像img[1]の表示）
 cvs.delete("katsudon") #katsudonのタグを持つ対象を消去
 cvs.create_image(300,270,image=img[1],tag="katsudon")

def bt2_on(): #ボタンbt2をクリック時の処理（画像img[2]の表示）
 cvs.delete("katsudon") #katsudonのタグを持つ対象を消去
 cvs.create_image(300,270,image=img[2],tag="katsudon")

def btdel_on():
 cvs.delete("katsudon")

root = tkinter.Tk()
root.title("PK") 
root.geometry("600x500")
root.configure(bg="white") 

cvs = tkinter.Canvas(width=600,height=500,bg="white")
cvs.pack()

img = []
for i in range(3): #リストimgに画像を追加
 img.append(tkinter.PhotoImage(file="Images/katsudon_"+str(i)+".png"))
 img[i] = img[i].subsample(2,2) #画像を縦1/2，横1/2に縮小

bt0 =tkinter.Button(root,text="１",
 font=("Times New Roman",24),
 command=bt0_on) #ボタンを作成（クリック時の処理はbt0_on）
bt1 =tkinter.Button(root,text="２",
 font=("Times New Roman",24),
 command=bt1_on) #ボタンを作成（クリック時の処理はbt1_on）
bt2 =tkinter.Button(root,text="３",
 font=("Times New Roman",24),
 command=bt2_on) #ボタンを作成（クリック時の処理はbt2_on）
btdel =tkinter.Button(root,text="消去",
 font=("Times New Roman",10),
 command=btdel_on) #ボタンを作成（クリック時の処理はbtdel_on）

bt0.place(x=150,y=0) 
bt1.place(x=250,y=0)
bt2.place(x=350,y=0)
btdel.place(x=550,y=0)

root.mainloop()
