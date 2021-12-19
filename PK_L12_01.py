import tkinter

key_code = 0 #キーコードの初期値は0（数値）
key_name = "" #キー名称の初期値は空白（文字列）

def key_down(e): #関数を宣言（キーを押したときの処理）
    key_code = e.keycode #押されたキーのキーコードを代入
    key_name = e.keysym #押されたキーのキー名称を代入
    cvs.delete("code") #1つ前に表示したキーコードを消去
    cvs.delete("name") #1つ前に表示したキー名称を消去
    cvs.create_text(300,200,text="KEYCODE: "+str(key_code),
        font=("MS 明朝",30),tag="code") #key_codeのテキストを表示
    cvs.create_text(300,300,text="KEYSYM: "+key_name,
        font=("MS 明朝",30),tag="name") #key_nameのテキストを表示

root = tkinter.Tk()
root.title("PK")
root.bind("<KeyPress>", key_down) #キーが押されたときに関数key_downを実行

cvs = tkinter.Canvas(root,width=600,height=400,bg="white")
cvs.pack()

cvs.create_text(300,100,text="キーを押してください",font=("MS 明朝",30))

root.mainloop()
