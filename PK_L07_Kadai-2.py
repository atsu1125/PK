import tkinter
root = tkinter.Tk()
root.title("チェック柄の服を描け")

cvs = tkinter.Canvas(width=600,height=600,bg="gray") 
cvs.pack()

for i in range(10):
    for j in range(8):
        if i%2==0:
            if j%2==0:
                cvs.create_rectangle(50+50*i,50+50*j,100+50*i,100+50*j,fill="white",outline="white")
            else :
                cvs.create_rectangle(50+50*i,50+50*j,100+50*i,100+50*j,fill="orange",outline="orange")
        else:
            if j%2==0:
                cvs.create_rectangle(50+50*i,50+50*j,100+50*i,100+50*j,fill="orange",outline="orange")
            else :
                cvs.create_rectangle(50+50*i,50+50*j,100+50*i,100+50*j,fill="white",outline="white")

cvs.create_oval(225,0,375,110, fill="grey",outline="grey")

cvs.create_rectangle(0,200,140,450,fill="grey",outline="grey")

cvs.create_rectangle(460,200,550,450,fill="grey",outline="grey")

root.mainloop()
