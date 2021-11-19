import tkinter
import random

def bt0_on(): #ボタンbt0をクリック時の処理（画像img[0]の表示）
    if  bt0["text"] == "何が出るかな？":
         cvs.delete("katsudon") #katsudonのタグを持つ対象を消去
         count = random.choice([0, 1, 2])
         cvs.create_image(300,270,image=img[count],tag="katsudon")
         bt0["text"] = "リセット"
    else:
         cvs.delete("katsudon")
         bt0["text"] = "何が出るかな？"

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

bt0 =tkinter.Button(root,text="何が出るかな？",
 font=("Times New Roman",24),
 command=bt0_on) #ボタンを作成（クリック時の処理はbt0_on）

bt0.place(x=150,y=20) 

root.mainloop()
