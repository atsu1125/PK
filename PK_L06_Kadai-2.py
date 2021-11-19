import tkinter
root = tkinter.Tk()
root.title("プログラミング基礎") 
cvs = tkinter.Canvas(width=600,height=600,bg="lightcyan") 
cvs.pack()
cvs.create_line(50,100,108,250,fill="black",width=10) #左うで
cvs.create_line(550,100,492,250,fill="black",width=10) #右うで
cvs.create_line(420,460,480,540,fill="black",width=10) #右あし
cvs.create_line(182,460,122,540,fill="black",width=10) #左あし
cvs.create_oval(100,100,500,500,fill="lime") #本体
cvs.create_oval(200,200,250,250,fill="white") #左白目
cvs.create_oval(330,200,380,250,fill="white") #右白目
cvs.create_oval(220,210,230,220,fill="black") #左目
cvs.create_oval(350,210,360,220,fill="black") #右目
cvs.create_line(45,90,550,90,fill="lime",width=15) 
cvs.create_line(545,95,580,40,fill="lime",width=15)
cvs.create_text(300,50,text="S U U M O",fill="black",
                font=("MS 明朝",50))
root.mainloop()
