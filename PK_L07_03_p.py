import tkinter
root = tkinter.Tk()
root.title("オセロを描こう")

cvs = tkinter.Canvas(width=600,height=600,bg="gray") 
cvs.pack()

#ボードの描画
cvs.create_rectangle(100-5,100-5,500+5,500+5,fill="orange")
cvs.create_rectangle(100,100,500,500,fill="green")
#縦線・横線の描画
for i in range(9):
    cvs.create_line(100+50*i,100,100+50*i,500) #縦線(x座標固定)
for i in range(9):
    cvs.create_line(100,100+50*i,500,100+50*i) #横線
 
#石の描画
for i in range(8):
    for j in range(8):
        if i%2==0:
            cvs.create_oval(100+5+50*i,100+5+50*j,150-5+50*i,150-5+50*j,
                            fill="white",outline="white")
        else:
            cvs.create_oval(100+5+50*i,100+5+50*j,150-5+50*i,150-5+50*j,
                            fill="blue",outline="blue")
        
root.mainloop()
