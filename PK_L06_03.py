import tkinter
root = tkinter.Tk()
root.title("プログラミング基礎") 
cvs = tkinter.Canvas(width=600,height=600) 
cvs.pack()
cvs.create_oval(150,150,250,250,fill="orange4") #左耳
cvs.create_oval(350,150,450,250,fill="orange4") #右耳
cvs.create_oval(160,170,440,430,fill="orange4") #顔
cvs.create_oval(230,260,260,290,fill="black") #左目
cvs.create_oval(340,260,370,290,fill="black") #右目
cvs.create_oval(250,300,350,390,fill="wheat2") #鼻口部
cvs.create_oval(280,310,320,330,fill="orange4") #鼻
root.mainloop()
